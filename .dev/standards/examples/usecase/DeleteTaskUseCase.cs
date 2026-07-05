using System.Threading.Tasks;

namespace Example.Plans.UseCases;

public interface IDeleteTaskUseCase : ICommand<DeleteTaskInput, CqrsOutput>
{
    Task<CqrsOutput> Execute(DeleteTaskInput input);
}

public sealed class DeleteTaskInput : IInput
{
    public string? PlanId { get; set; }
    public string? ProjectName { get; set; }
    public string? TaskId { get; set; }
}
