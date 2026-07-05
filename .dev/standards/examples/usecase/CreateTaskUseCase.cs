using Example.Plans.Domain;
using System.Threading.Tasks;

namespace Example.Plans.UseCases;

public interface ICreateTaskUseCase : ICommand<CreateTaskInput, CqrsOutput>
{
    Task<CqrsOutput> Execute(CreateTaskInput input);
}

public sealed class CreateTaskInput : IInput
{
    public PlanId? PlanId { get; set; }
    public ProjectName? ProjectName { get; set; }
    public string? TaskName { get; set; }

    public static CreateTaskInput Create() => new();
}
