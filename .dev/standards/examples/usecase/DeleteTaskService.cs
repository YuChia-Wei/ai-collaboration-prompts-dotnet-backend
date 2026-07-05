using Example.Plans.Domain;
using System.Threading.Tasks;

namespace Example.Plans.UseCases;

public sealed class DeleteTaskService : IDeleteTaskUseCase
{
    private readonly IAggregateRepository<Plan, PlanId> _repository;

    public DeleteTaskService(IAggregateRepository<Plan, PlanId> repository)
    {
        Contract.RequireNotNull("Repository", repository);
        _repository = repository;
    }

    public async Task<CqrsOutput> Execute(DeleteTaskInput input)
    {
        Contract.RequireNotNull("Input", input);
        Contract.RequireNotNull("Plan id", input.PlanId);
        Contract.RequireNotNull("Project name", input.ProjectName);
        Contract.RequireNotNull("Task id", input.TaskId);

        var plan = await _repository.FindByIdAsync(PlanId.ValueOf(input.PlanId!))
                   ?? throw new ArgumentException($"Plan not found: {input.PlanId}");

        var projectName = ProjectName.ValueOf(input.ProjectName!);
        var taskId = TaskId.ValueOf(input.TaskId!);

        Contract.Require("Project exists", () => plan.HasProject(projectName));
        Contract.Require("Task exists", () => plan.GetProject(projectName)?.HasTask(taskId) == true);

        plan.DeleteTask(projectName, taskId);
        await _repository.SaveAsync(plan);

        return CqrsOutput.Create()
            .SetExitCode(ExitCode.Success);
    }

    // Wolverine handler entry point
    public Task<CqrsOutput> Handle(DeleteTaskInput input) => Execute(input);
}
