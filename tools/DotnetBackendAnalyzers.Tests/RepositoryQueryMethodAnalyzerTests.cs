using DotnetBackendAnalyzers;
using Xunit;

namespace DotnetBackendAnalyzers.Tests;

public sealed class RepositoryQueryMethodAnalyzerTests
{
    [Fact]
    public async Task Reports_query_method_on_domain_repository()
    {
        var diagnostics = await AnalyzerTestHelper.GetDiagnosticsAsync(
            new RepositoryQueryMethodAnalyzer(),
            """
            using System.Threading.Tasks;

            public interface IOrderRepository
            {
                Task<object?> GetByCustomerIdAsync(string customerId);
            }
            """);

        var diagnostic = Assert.Single(diagnostics);
        Assert.Equal("DBA1001", diagnostic.Id);
    }

    [Fact]
    public async Task Allows_identity_lookup_on_domain_repository()
    {
        var diagnostics = await AnalyzerTestHelper.GetDiagnosticsAsync(
            new RepositoryQueryMethodAnalyzer(),
            """
            using System.Threading.Tasks;

            public interface IOrderRepository
            {
                Task<object?> FindByIdAsync(string id);
            }
            """);

        Assert.Empty(diagnostics);
    }
}
