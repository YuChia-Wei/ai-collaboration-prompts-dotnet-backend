using DotnetBackendAnalyzers;
using Xunit;

namespace DotnetBackendAnalyzers.Tests;

public sealed class UseCaseServiceProviderInjectionAnalyzerTests
{
    [Fact]
    public async Task Reports_service_provider_injection_on_use_case()
    {
        var diagnostics = await AnalyzerTestHelper.GetDiagnosticsAsync(
            new UseCaseServiceProviderInjectionAnalyzer(),
            """
            using System;

            public sealed class PlaceOrderUseCase
            {
                public PlaceOrderUseCase(IServiceProvider serviceProvider)
                {
                }
            }
            """);

        var diagnostic = Assert.Single(diagnostics);
        Assert.Equal("DBA1002", diagnostic.Id);
    }
}
