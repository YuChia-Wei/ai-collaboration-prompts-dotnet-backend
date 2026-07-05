# Code Templates (.NET)

This document contains C# templates and patterns commonly used in the .NET stack.

## Command Handler Template (Wolverine)

```csharp
public sealed record CreateTaskInput(string PlanId, string ProjectName, string TaskName);

public sealed class CreateTaskHandler
{
    private readonly IAggregateRepository<Plan, PlanId> _repository;

    public CreateTaskHandler(IAggregateRepository<Plan, PlanId> repository)
    {
        Contract.RequireNotNull(nameof(repository), repository);
        _repository = repository;
    }

    public async Task<CqrsOutput> Handle(CreateTaskInput input)
    {
        // 1) Contracts validation (outside try-catch)
        Contract.RequireNotNull(nameof(input), input);
        Contract.RequireNotNull(nameof(input.PlanId), input.PlanId);

        try
        {
            var output = CqrsOutput.Create();

            // Step 1: Load aggregate
            var plan = await _repository.FindByIdAsync(PlanId.ValueOf(input.PlanId));
            if (plan == null)
            {
                return output.Fail("Plan not found");
            }

            // Step 2: Execute business logic
            plan.CreateTask(ProjectName.ValueOf(input.ProjectName), TaskName.ValueOf(input.TaskName));

            // Step 3: Save aggregate
            await _repository.SaveAsync(plan);

            // Step 4: Return success
            return output.Ok(plan.Id.Value);
        }
        catch (Exception ex)
        {
            throw new UseCaseFailureException(ex.Message);
        }
    }
}
```

## Query Handler Template (Projection)

```csharp
public sealed record GetRecordInput(string RecordId);
public sealed record GetRecordOutput(RecordDto Record, ExitCode ExitCode, string? Message);

public sealed class GetRecordHandler
{
    private readonly IRecordProjection _projection;

    public GetRecordHandler(IRecordProjection projection)
    {
        Contract.RequireNotNull(nameof(projection), projection);
        _projection = projection;
    }

    public async Task<GetRecordOutput> Handle(GetRecordInput input)
    {
        Contract.RequireNotNull(nameof(input), input);

        try
        {
            var dto = await _projection.FindByIdAsync(input.RecordId);
            if (dto == null)
            {
                return new GetRecordOutput(default!, ExitCode.FAILURE, "Record not found");
            }

            return new GetRecordOutput(dto, ExitCode.SUCCESS, null);
        }
        catch (Exception ex)
        {
            throw new UseCaseFailureException(ex.Message);
        }
    }
}
```

## Validation Pattern

### Aggregate Root Validation
```csharp
Contract.RequireNotNull(nameof(recordId), recordId);
Contract.Require(name.Length <= 100, "name exceeds maximum length");
```

### Entity & Value Object Validation
```csharp
Objects.RequireNotNull(pbiId, "pbiId cannot be null");
Objects.RequireNotNull(name, "name cannot be null");
```

### Constructor Validation
```csharp
public CreateRecordHandler(IAggregateRepository<Record, RecordId> repository)
{
    Contract.RequireNotNull(nameof(repository), repository);
    _repository = repository;
}
```

## Aggregate Constructor Template

```csharp
public sealed class Record : AggregateRoot<RecordId>
{
    public Record(RecordId recordId, RecordName name)
    {
        Contract.RequireNotNull(nameof(recordId), recordId);
        Contract.RequireNotNull(nameof(name), name);
        Apply(new RecordCreated(recordId, name, metadata: new Dictionary<string, string>(), DateProvider.Now()));
    }
}

// ❌ WRONG: Static factory hides event sourcing rules
// public static Record Create(...) { ... }
```

## Domain Event Template

```csharp
public sealed record RecordCreated(
    RecordId RecordId,
    RecordName Name,
    IReadOnlyDictionary<string, string> Metadata,
    Guid Id,
    DateTimeOffset OccurredOn
)
{
    public RecordCreated
    {
        Contract.RequireNotNull(nameof(RecordId), RecordId);
        Contract.RequireNotNull(nameof(Name), Name);
        Contract.RequireNotNull(nameof(Metadata), Metadata); // Required
        Contract.RequireNotNull(nameof(Id), Id);
        Contract.RequireNotNull(nameof(OccurredOn), OccurredOn);
    }
}
```

## Use Case Interface Pattern (Optional)

```csharp
public interface ICreateRecordUseCase
{
    Task<CqrsOutput> Execute(CreateRecordInput input);
}
```

## Repository Usage Template

```csharp
public sealed class CreateRecordHandler
{
    private readonly IAggregateRepository<Record, RecordId> _repository;

    public CreateRecordHandler(IAggregateRepository<Record, RecordId> repository)
    {
        _repository = repository;
    }
}

// Compatibility is allowed only for existing products and must preserve the same contract:
// public interface IDomainRepository<TAggregate, TId>
//     : IAggregateRepository<TAggregate, TId> { }
```

## Query Repository Template (EF Core adapter example)

```csharp
public interface IRecordQueryRepository : IQueryRepository
{
    Task<RecordDto?> FindByIdAsync(string recordId);
    Task<IReadOnlyList<RecordDto>> FindAllAsync();
}

public sealed class EfRecordQueryRepository : IRecordQueryRepository
{
    private readonly AppDbContext _db;

    public EfRecordQueryRepository(AppDbContext db)
    {
        _db = db;
    }

    public async Task<RecordDto?> FindByIdAsync(string recordId)
    {
        return await _db.Records
            .Where(p => p.RecordId == recordId)
            .Select(RecordMapper.ToDto)
            .FirstOrDefaultAsync();
    }
}
```

## Mapper Template

```csharp
public static class RecordMapper
{
    public static RecordDto ToDto(Record record)
        => new(record.Id.Value, record.Name.Value);
}
```
