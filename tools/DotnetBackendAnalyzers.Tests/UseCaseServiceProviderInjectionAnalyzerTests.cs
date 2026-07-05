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

    [Fact]
    public async Task Reports_service_provider_in_primary_constructor()
    {
        var diagnostics = await AnalyzerTestHelper.GetDiagnosticsAsync(
            new UseCaseServiceProviderInjectionAnalyzer(),
            """
            using System;

            public sealed class PlaceOrderHandler(IServiceProvider serviceProvider)
            {
            }
            """);

        var diagnostic = Assert.Single(diagnostics);
        Assert.Equal("DBA1002", diagnostic.Id);
    }

    [Fact]
    public async Task Reports_attribute_property_injection()
    {
        var diagnostics = await AnalyzerTestHelper.GetDiagnosticsAsync(
            new UseCaseServiceProviderInjectionAnalyzer(),
            """
            using System;

            public sealed class InjectAttribute : Attribute { }

            public sealed class PlaceOrderHandler
            {
                [Inject]
                public object Repository { get; set; } = new();
            }
            """);

        var diagnostic = Assert.Single(diagnostics);
        Assert.Equal("DBA1010", diagnostic.Id);
    }

    [Fact]
    public async Task Reports_handler_that_mixes_command_and_query_markers()
    {
        var diagnostics = await AnalyzerTestHelper.GetDiagnosticsAsync(
            new UseCaseServiceProviderInjectionAnalyzer(),
            """
            public interface ICommand<T> { }
            public interface IQuery<T> { }
            public sealed class CreateOrder : ICommand<string> { }
            public sealed class GetOrder : IQuery<string> { }

            public sealed class OrderHandler
            {
                public string Handle(CreateOrder command) => "";
                public string Handle(GetOrder query) => "";
            }
            """);

        var diagnostic = Assert.Single(diagnostics);
        Assert.Equal("DBA1011", diagnostic.Id);
    }

    [Fact]
    public async Task Reports_direct_repository_construction()
    {
        var diagnostics = await AnalyzerTestHelper.GetDiagnosticsAsync(
            new UseCaseServiceProviderInjectionAnalyzer(),
            """
            public sealed class SqlOrderRepository { }

            public sealed class PlaceOrderHandler
            {
                public object Handle() => new SqlOrderRepository();
            }
            """);

        var diagnostic = Assert.Single(diagnostics);
        Assert.Equal("DBA1012", diagnostic.Id);
    }

    [Fact]
    public async Task Allows_explicit_dependency_and_single_cqrs_role()
    {
        var diagnostics = await AnalyzerTestHelper.GetDiagnosticsAsync(
            new UseCaseServiceProviderInjectionAnalyzer(),
            """
            public interface ICommand<T> { }
            public interface IOrderRepository { }
            public sealed class CreateOrder : ICommand<string> { }

            public sealed class PlaceOrderHandler(IOrderRepository repository)
            {
                public string Handle(CreateOrder command) => "";
            }
            """);

        Assert.Empty(diagnostics);
    }

    [Fact]
    public async Task Does_not_treat_command_bus_as_command_marker()
    {
        var diagnostics = await AnalyzerTestHelper.GetDiagnosticsAsync(
            new UseCaseServiceProviderInjectionAnalyzer(),
            """
            public interface ICommandBus { }
            public interface IQueryBus { }

            public sealed class BusHandler
            {
                public void Handle(ICommandBus commandBus) { }
                public void Handle(IQueryBus queryBus) { }
            }
            """);

        Assert.Empty(diagnostics);
    }
}
