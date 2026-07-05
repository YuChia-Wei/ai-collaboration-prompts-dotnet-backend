using System;
using System.Threading.Tasks;
using Example.Plans.Domain;

namespace Example.Plans.UseCases;

public sealed class CreateTaskService : ICreateTaskUseCase
{
    private readonly IAggregateRepository<Plan, PlanId> _planRepository;

    public CreateTaskService(IAggregateRepository<Plan, PlanId> planRepository)
    {
        Contract.RequireNotNull("PlanRepository", planRepository);
        _planRepository = planRepository;
    }

    public async Task<CqrsOutput> Execute(CreateTaskInput input)
    {
        try
        {
            var output = CqrsOutput.Create();

            Contract.RequireNotNull("Input", input);
            Contract.RequireNotNull("Plan id", input.PlanId);
            Contract.RequireNotNull("Project name", input.ProjectName);
            Contract.RequireNotNull("Task name", input.TaskName);

            var plan = await _planRepository.FindByIdAsync(input.PlanId!);
            if (plan == null)
            {
                output.SetId(input.PlanId!.Value)
                      .SetExitCode(ExitCode.Failure)
                      .SetMessage($"Create task failed: plan not found, plan id = {input.PlanId!.Value}");
                return output;
            }

            var taskId = plan.CreateTask(input.ProjectName!, TaskId.Create(), input.TaskName!);
            await _planRepository.SaveAsync(plan);

            output.SetId(taskId.Value)
                  .SetExitCode(ExitCode.Success);
            return output;
        }
        catch (Exception ex)
        {
            throw new UseCaseFailureException(ex);
        }
    }

    // Wolverine handler entry point
    public Task<CqrsOutput> Handle(CreateTaskInput input) => Execute(input);
}
