using System.Collections.Immutable;
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using Microsoft.CodeAnalysis.Diagnostics;

namespace DotnetBackendAnalyzers;

[DiagnosticAnalyzer(LanguageNames.CSharp)]
public sealed class UseCaseServiceProviderInjectionAnalyzer : DiagnosticAnalyzer
{
    public override ImmutableArray<DiagnosticDescriptor> SupportedDiagnostics =>
        ImmutableArray.Create(RuleDescriptors.UseCaseServiceProviderInjection);

    public override void Initialize(AnalysisContext context)
    {
        context.ConfigureGeneratedCodeAnalysis(GeneratedCodeAnalysisFlags.None);
        context.EnableConcurrentExecution();
        context.RegisterSyntaxNodeAction(AnalyzeConstructor, SyntaxKind.ConstructorDeclaration);
    }

    private static void AnalyzeConstructor(SyntaxNodeAnalysisContext context)
    {
        var constructor = (ConstructorDeclarationSyntax)context.Node;

        if (constructor.Parent is not ClassDeclarationSyntax classDeclaration || !LooksLikeUseCaseOrHandler(classDeclaration))
        {
            return;
        }

        foreach (var parameter in constructor.ParameterList.Parameters)
        {
            var parameterType = parameter.Type is null
                ? null
                : context.SemanticModel.GetTypeInfo(parameter.Type, context.CancellationToken).Type;

            if (parameterType?.ToDisplayString(SymbolDisplayFormat.FullyQualifiedFormat) == "global::System.IServiceProvider")
            {
                context.ReportDiagnostic(Diagnostic.Create(
                    RuleDescriptors.UseCaseServiceProviderInjection,
                    parameter.GetLocation(),
                    classDeclaration.Identifier.ValueText));
            }
        }
    }

    private static bool LooksLikeUseCaseOrHandler(ClassDeclarationSyntax classDeclaration)
    {
        var name = classDeclaration.Identifier.ValueText;
        if (name.EndsWith("UseCase", System.StringComparison.Ordinal) || name.EndsWith("Handler", System.StringComparison.Ordinal))
        {
            return true;
        }

        var namespaceName = GetNamespaceName(classDeclaration);
        return namespaceName.IndexOf(".UseCases", System.StringComparison.Ordinal) >= 0
            || namespaceName.IndexOf(".Handlers", System.StringComparison.Ordinal) >= 0;
    }

    private static string GetNamespaceName(SyntaxNode node)
    {
        for (var current = node.Parent; current is not null; current = current.Parent)
        {
            if (current is NamespaceDeclarationSyntax namespaceDeclaration)
            {
                return namespaceDeclaration.Name.ToString();
            }

            if (current is FileScopedNamespaceDeclarationSyntax fileScopedNamespace)
            {
                return fileScopedNamespace.Name.ToString();
            }
        }

        return string.Empty;
    }
}
