using System.Collections.Immutable;
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.Diagnostics;

namespace DotnetBackendAnalyzers;

[DiagnosticAnalyzer(LanguageNames.CSharp)]
public sealed class UseCaseServiceProviderInjectionAnalyzer : DiagnosticAnalyzer
{
    public override ImmutableArray<DiagnosticDescriptor> SupportedDiagnostics =>
        ImmutableArray.Create(
            RuleDescriptors.UseCaseServiceProviderInjection,
            RuleDescriptors.UseCaseDependencyResolution,
            RuleDescriptors.MixedCommandQueryHandler,
            RuleDescriptors.UseCaseDirectRepositoryConstruction);

    public override void Initialize(AnalysisContext context)
    {
        context.ConfigureGeneratedCodeAnalysis(GeneratedCodeAnalysisFlags.None);
        context.EnableConcurrentExecution();
        context.RegisterSymbolAction(AnalyzeNamedType, SymbolKind.NamedType);
        context.RegisterSyntaxNodeAction(AnalyzeObjectCreation, Microsoft.CodeAnalysis.CSharp.SyntaxKind.ObjectCreationExpression);
    }

    private static void AnalyzeNamedType(SymbolAnalysisContext context)
    {
        var type = (INamedTypeSymbol)context.Symbol;
        if (type.TypeKind != TypeKind.Class || !LooksLikeUseCaseOrHandler(type))
        {
            return;
        }

        var handlesCommand = false;
        var handlesQuery = false;

        foreach (var member in type.GetMembers())
        {
            if (member is IFieldSymbol field)
            {
                ReportForbiddenMemberType(context, type, field.Type, field.Locations, field.Name);
                continue;
            }

            if (member is IPropertySymbol property)
            {
                ReportForbiddenMemberType(context, type, property.Type, property.Locations, property.Name);
                ReportInjectionAttributes(context, type, property);
                continue;
            }

            if (member is not IMethodSymbol method)
            {
                continue;
            }

            foreach (var parameter in method.Parameters)
            {
                ReportForbiddenMemberType(context, type, parameter.Type, parameter.Locations, parameter.Name);
            }

            if (method.Name != "Handle" || method.Parameters.Length == 0)
            {
                continue;
            }

            handlesCommand |= ImplementsMarker(method.Parameters[0].Type, "ICommand");
            handlesQuery |= ImplementsMarker(method.Parameters[0].Type, "IQuery");
        }

        if (handlesCommand && handlesQuery)
        {
            context.ReportDiagnostic(Diagnostic.Create(
                RuleDescriptors.MixedCommandQueryHandler,
                type.Locations[0],
                type.Name));
        }
    }

    private static void AnalyzeObjectCreation(SyntaxNodeAnalysisContext context)
    {
        var creation = (Microsoft.CodeAnalysis.CSharp.Syntax.ObjectCreationExpressionSyntax)context.Node;
        var containingType = context.ContainingSymbol?.ContainingType;
        if (containingType is null || !LooksLikeUseCaseOrHandler(containingType))
        {
            return;
        }

        var createdType = context.SemanticModel.GetTypeInfo(creation, context.CancellationToken).Type;
        if (createdType is null || !createdType.Name.EndsWith("Repository", System.StringComparison.Ordinal))
        {
            return;
        }

        context.ReportDiagnostic(Diagnostic.Create(
            RuleDescriptors.UseCaseDirectRepositoryConstruction,
            creation.Type.GetLocation(),
            containingType.Name,
            createdType.Name));
    }

    private static void ReportForbiddenMemberType(
        SymbolAnalysisContext context,
        INamedTypeSymbol containingType,
        ITypeSymbol memberType,
        ImmutableArray<Location> locations,
        string memberName)
    {
        var location = locations.Length > 0 ? locations[0] : containingType.Locations[0];
        if (memberType.ToDisplayString(SymbolDisplayFormat.FullyQualifiedFormat) == "global::System.IServiceProvider")
        {
            context.ReportDiagnostic(Diagnostic.Create(
                RuleDescriptors.UseCaseServiceProviderInjection,
                location,
                containingType.Name));
        }
        else if (memberType.Name.EndsWith("ServiceLocator", System.StringComparison.Ordinal))
        {
            context.ReportDiagnostic(Diagnostic.Create(
                RuleDescriptors.UseCaseDependencyResolution,
                location,
                containingType.Name,
                memberName));
        }
    }

    private static void ReportInjectionAttributes(
        SymbolAnalysisContext context,
        INamedTypeSymbol containingType,
        IPropertySymbol property)
    {
        foreach (var attribute in property.GetAttributes())
        {
            var attributeName = attribute.AttributeClass?.Name;
            if (attributeName is not "Inject" and not "InjectAttribute"
                and not "FromServices" and not "FromServicesAttribute")
            {
                continue;
            }

            context.ReportDiagnostic(Diagnostic.Create(
                RuleDescriptors.UseCaseDependencyResolution,
                property.Locations[0],
                containingType.Name,
                attributeName));
        }
    }

    private static bool ImplementsMarker(ITypeSymbol type, string markerPrefix)
    {
        if (type.TypeKind == TypeKind.Interface && type.Name == markerPrefix)
        {
            return true;
        }

        foreach (var contract in type.AllInterfaces)
        {
            if (contract.Name == markerPrefix)
            {
                return true;
            }
        }

        return false;
    }

    private static bool LooksLikeUseCaseOrHandler(INamedTypeSymbol type)
    {
        var name = type.Name;
        if (name.EndsWith("UseCase", System.StringComparison.Ordinal) || name.EndsWith("Handler", System.StringComparison.Ordinal))
        {
            return true;
        }

        var namespaceName = type.ContainingNamespace?.ToDisplayString() ?? string.Empty;
        return namespaceName.IndexOf(".UseCases", System.StringComparison.Ordinal) >= 0
            || namespaceName.IndexOf(".Handlers", System.StringComparison.Ordinal) >= 0;
    }
}
