# Inquiry and Archive Usage Guide (.NET)

## Inquiry

### 1) Define an Inquiry

```csharp
public interface IFindWorkItemsByIterationIdInquiry
{
    IReadOnlyList<string> FindByIterationId(IterationId sprintId);
}
```

### 2) Implement with EF Core

```csharp
public sealed class EfFindWorkItemsByIterationIdInquiry : IFindWorkItemsByIterationIdInquiry
{
    private readonly ReadDbContext _db;

    public IReadOnlyList<string> FindByIterationId(IterationId sprintId)
        => _db.WorkItems.Where(p => p.IterationId == sprintId.Value && !p.Deleted)
                  .OrderBy(p => p.OrderId)
                  .Select(p => p.WorkItemId)
                  .ToList();
}
```

### 3) Use in a Reactor

```csharp
public sealed class NotifyWorkItemWhenIterationStartedService : IWhenIterationStartedNotifyWorkItemReactor
{
    private readonly IFindWorkItemsByIterationIdInquiry _inquiry;
    private readonly IStartWorkItemUseCase _useCase;

    public void Handle(DomainEventData message)
    {
        if (message == null) return;

        var domainEvent = DomainEventMapper.ToDomain(message);
        if (domainEvent is IterationStarted started)
        {
            var pbiIds = _inquiry.FindByIterationId(IterationId.ValueOf(started.IterationId));
            foreach (var pbiId in pbiIds)
            {
                _useCase.Execute(new StartWorkItemInput { WorkItemId = pbiId });
            }
        }
    }
}
```

## Archive

### 1) Define Archive Interface

```csharp
public interface IProductArchive
{
    void Archive(Product product, string reason, string archivedBy);
    ArchivedProduct? FindArchivedById(ProductId productId);
}
```

### 2) Define Archived Data

```csharp
public sealed record ArchivedProduct(
    string ProductId,
    string Name,
    string Goal,
    DateTimeOffset ArchivedAt,
    string ArchivedBy,
    string Reason,
    string OriginalDataJson
);
```

### 3) Implement Archive with EF Core

```csharp
public sealed class EfProductArchive : IProductArchive
{
    private readonly ReadDbContext _db;

    public void Archive(Product product, string reason, string archivedBy)
    {
        // TODO: serialize full aggregate state as JSON
        var archived = new ArchivedProduct(...);
        _db.ArchivedProducts.Add(archived);
        _db.SaveChanges();
    }
}
```

## Checklist

- [ ] Inquiry names follow `Find[What]By[Condition]Inquiry`
- [ ] Each inquiry handles one query only
- [ ] Archive stores metadata (who/when/why)
- [ ] Soft delete or archived tables are indexed
