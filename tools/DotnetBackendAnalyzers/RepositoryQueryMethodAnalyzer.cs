using System.Collections.Immutable;
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using Microsoft.CodeAnalysis.Diagnostics;

namespace DotnetBackendAnalyzers;

[DiagnosticAnalyzer(LanguageNames.CSharp)]
public sealed class RepositoryQueryMethodAnalyzer : DiagnosticAnalyzer
{
    private static readonly ImmutableHashSet<string> AllowedMethods =
        ImmutableHashSet.Create("FindByIdAsync", "FindByIdsAsync", "SaveAsync", "SaveAllAsync", "DeleteAsync");

    private static readonly string[] QueryPrefixes = { "GetBy", "FindBy", "QueryBy", "SearchBy" };

    public override ImmutableArray<DiagnosticDescriptor> SupportedDiagnostics =>
        ImmutableArray.Create(RuleDescriptors.RepositoryQueryMethod);

    public override void Initialize(AnalysisContext context)
    {
        context.ConfigureGeneratedCodeAnalysis(GeneratedCodeAnalysisFlags.None);
        context.EnableConcurrentExecution();
        context.RegisterSyntaxNodeAction(AnalyzeMethod, SyntaxKind.MethodDeclaration);
    }

    private static void AnalyzeMethod(SyntaxNodeAnalysisContext context)
    {
        var method = (MethodDeclarationSyntax)context.Node;

        if (method.Parent is not InterfaceDeclarationSyntax interfaceDeclaration)
        {
            return;
        }

        var interfaceName = interfaceDeclaration.Identifier.ValueText;
        if (!IsDomainRepositoryInterface(interfaceName))
        {
            return;
        }

        var methodName = method.Identifier.ValueText;
        if (AllowedMethods.Contains(methodName) || !LooksLikeQueryMethod(methodName))
        {
            return;
        }

        context.ReportDiagnostic(Diagnostic.Create(
            RuleDescriptors.RepositoryQueryMethod,
            method.Identifier.GetLocation(),
            methodName));
    }

    private static bool IsDomainRepositoryInterface(string name)
    {
        return name.Contains("Repository")
            && !name.Contains("QueryRepository")
            && !name.Contains("ReadRepository");
    }

    private static bool LooksLikeQueryMethod(string methodName)
    {
        foreach (var prefix in QueryPrefixes)
        {
            if (methodName.StartsWith(prefix, System.StringComparison.Ordinal))
            {
                return true;
            }
        }

        return false;
    }
}
