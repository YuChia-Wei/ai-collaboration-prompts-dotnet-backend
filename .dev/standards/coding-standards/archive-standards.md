# Archive Coding Standards (.NET)

This document defines coding standards for the Archive Pattern, which handles database write requirements for Query Models.

---

## 📌 Overview

The Archive Pattern is used for soft deletion and historical data management and is dedicated to Query Model writes in a CQRS architecture.

- **Query Model writes**: An Archive handles database write requirements for a Query Model.
- **Distinction from Repository**: A Repository is limited to writing a single Aggregate in the Command Model.
- **Event-driven**: A Reactor invokes an Archive when it receives a Domain Event.

---

## 🏷️ Pattern Markers (for Automated Checks)

The following markers are used by automated code review scripts:

```yaml
# Archive rules (soft-delete support)
Pattern (required, any): IsDeleted|IsArchived|ArchivedAt

# Forbidden rules (no hard deletion)
Pattern (forbidden): HardDelete
```

---

## 📌 Core Concept

An **Archive** is a database write pattern dedicated to Query Models in a CQRS architecture:

- Its interface resembles a Write Model Repository, but an Archive handles database write requirements for a Query Model.
- A Repository is limited to writing a single Aggregate in the Command Model.
- It may write to one table or across multiple tables.
- A Reactor in the Handler layer invokes the Archive after receiving a Domain Event and writes the data to the database.

---

## 🔴 Mandatory Rules (MUST FOLLOW)

### 1. Archive Interface Design

#### Namespace

```csharp
// ✅ Correct: define the Archive interface in the Application layer
namespace YourProject.Application.Users.Archives;

// ❌ Incorrect: do not place it in the Infrastructure layer
namespace YourProject.Infrastructure.Persistence;  // Incorrect!
```

#### Interface Naming Rules

```csharp
// ✅ Correct: use the singular I[Entity]Archive naming pattern
public interface IUserArchive { }

// ❌ Incorrect: do not use other naming patterns
public interface IUserRepository { }  // Do not use Repository for a Read Model
public interface UserArchive { }      // Add the I prefix
public interface IUserDtoArchive { }  // Do not use DtoArchive
```

#### Interface Definition

```csharp
// ✅ Correct: define an Archive interface
public interface IUserArchive
{
    Task<UserData?> FindByIdAsync(string userId, CancellationToken ct = default);
    Task SaveAsync(UserData userData, CancellationToken ct = default);
    Task DeleteAsync(UserData userData, CancellationToken ct = default);
}

// ❌ Incorrect: do not return a domain object
public interface IUserArchive
{
    Task<User?> FindByIdAsync(string userId);  // Incorrect! Return UserData instead
}

// ❌ Incorrect: do not return a DTO
public interface IUserArchive
{
    Task<UserDto?> FindByIdAsync(string userId);  // Incorrect! Return UserData instead
}
```

---

### 2. Archive Implementation

#### Implementation Location

```csharp
// ✅ Correct: place the implementation in the Infrastructure layer
namespace YourProject.Infrastructure.Persistence.Archives;
```

#### EF Core Archive Implementation

```csharp
// ✅ Correct: EF Core implementation
namespace YourProject.Infrastructure.Persistence.Archives;

public class EfCoreUserArchive : IUserArchive
{
    private readonly ApplicationDbContext _context;

    public EfCoreUserArchive(ApplicationDbContext context)
    {
        _context = context;
    }

    public async Task<UserData?> FindByIdAsync(string userId, CancellationToken ct = default)
    {
        ArgumentNullException.ThrowIfNull(userId);
        
        return await _context.Users
            .AsNoTracking()
            .FirstOrDefaultAsync(x => x.Id == userId, ct);
    }

    public async Task SaveAsync(UserData userData, CancellationToken ct = default)
    {
        ArgumentNullException.ThrowIfNull(userData);
        
        var existing = await _context.Users
            .FirstOrDefaultAsync(x => x.Id == userData.Id, ct);
        
        if (existing is null)
        {
            await _context.Users.AddAsync(userData, ct);
        }
        else
        {
            _context.Entry(existing).CurrentValues.SetValues(userData);
        }
    }

    public async Task DeleteAsync(UserData userData, CancellationToken ct = default)
    {
        ArgumentNullException.ThrowIfNull(userData);
        
        var existing = await _context.Users
            .FirstOrDefaultAsync(x => x.Id == userData.Id, ct);
        
        if (existing is not null)
        {
            _context.Users.Remove(existing);
        }
    }
}
```

---

### 3. DI Registration

```csharp
// ✅ Correct: register in ServiceExtensions
public static class ArchiveServiceExtensions
{
    public static IServiceCollection AddArchives(this IServiceCollection services)
    {
        services.AddScoped<IUserArchive, EfCoreUserArchive>();
        // Other Archive registrations...
        
        return services;
    }
}
```

---

## 🎯 Usage Guide

### When to Use an Archive

- ✅ Query Model CRUD operations
- ✅ Reference-data synchronization across Bounded Contexts
- ✅ Event-driven Read Model writes
- ❌ Write Model CRUD operations (use a Repository)

### Difference from a Repository

```csharp
// Repository: persistence for a Write Model Aggregate
IAggregateRepository<Product, ProductId> repository;
await repository.FindByIdAsync(id);  // Returns a Product domain object
await repository.SaveAsync(product); // Persists a domain object

// Archive: persistence for Read Model Data
IUserArchive archive;
await archive.FindByIdAsync(userId);   // Returns UserData
await archive.SaveAsync(userData);     // Persists a Data object
```

---

## 🎯 Event-Driven Write Example

### A Reactor Uses an Archive

```csharp
// ✅ Correct: use WolverineFx to handle a Domain Event
public class UserCreatedReactor
{
    private readonly IUserArchive _archive;

    public UserCreatedReactor(IUserArchive archive)
    {
        _archive = archive;
    }

    public async Task Handle(UserCreated @event, CancellationToken ct)
    {
        var userData = new UserData
        {
            Id = @event.UserId.Value,
            Name = @event.Name,
            Email = @event.Email,
            CreatedAt = @event.OccurredOn
        };

        await _archive.SaveAsync(userData, ct);
    }
}
```

---

## 🔍 Checklist

### Archive Interface
- [ ] Defined in the `Application` layer.
- [ ] Uses the `I[Entity]Archive` naming pattern.
- [ ] Returns Data (a Persistence Object), not a domain object or DTO.
- [ ] Has `FindByIdAsync`, `SaveAsync`, and `DeleteAsync` methods.
- [ ] Supports `CancellationToken`.

### Archive Implementation
- [ ] Implemented in `Infrastructure.Persistence.Archives`.
- [ ] If the adapter uses EF Core, it follows EF Core tracking/materialization guidance.
- [ ] Uses `ArgumentNullException.ThrowIfNull`.
- [ ] Registered through DI.

---

## 📂 Code Examples

For more complete examples, see:

| Example | Path |
|------|------|
| Inquiry + Archive examples | [../examples/inquiry-archive/](../examples/inquiry-archive/) |
| Usage guide | [../examples/inquiry-archive/USAGE-GUIDE.md](../examples/inquiry-archive/USAGE-GUIDE.md) |

---

## Related Documents

- [repository-standards.md](repository-standards.md)
- [projection-standards.md](projection-standards.md)
- [usecase-standards.md](usecase-standards.md)
