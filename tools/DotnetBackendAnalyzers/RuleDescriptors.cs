using Microsoft.CodeAnalysis;

namespace DotnetBackendAnalyzers;

internal static class RuleDescriptors
{
    public static readonly DiagnosticDescriptor RepositoryQueryMethod = new(
        id: "DBA1001",
        title: "Domain repository should not expose query methods",
        messageFormat: "Repository member '{0}' looks like a query method; use projection, inquiry, archive, or query-side services instead",
        category: DiagnosticCategories.Architecture,
        defaultSeverity: DiagnosticSeverity.Warning,
        isEnabledByDefault: true,
        description: "Domain repositories are write-side aggregate access ports. Query behavior should live on the read side.");

    public static readonly DiagnosticDescriptor UseCaseServiceProviderInjection = new(
        id: "DBA1002",
        title: "Use case or handler should not inject IServiceProvider",
        messageFormat: "Use case or handler '{0}' injects IServiceProvider; inject explicit dependencies instead",
        category: DiagnosticCategories.Architecture,
        defaultSeverity: DiagnosticSeverity.Warning,
        isEnabledByDefault: true,
        description: "Use cases should declare explicit dependencies and avoid service locator style access.");

    public static readonly DiagnosticDescriptor AggregateInfrastructureDependency = new(
        id: "DBA1003",
        title: "Aggregate should not depend on infrastructure types",
        messageFormat: "Aggregate/entity '{0}' references infrastructure type '{1}'",
        category: DiagnosticCategories.Architecture,
        defaultSeverity: DiagnosticSeverity.Warning,
        isEnabledByDefault: true,
        description: "Domain aggregates and entities must remain independent from infrastructure concerns such as EF Core DbContext.");
}
