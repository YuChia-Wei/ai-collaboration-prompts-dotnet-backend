# CORS Setup (Dotnet)

## Quick Fix
Configure CORS in `src/Api/Program.cs` (or `src/Api/Extensions/CorsExtensions.cs`).

- AllowedOrigins: `${FRONTEND_ORIGIN}`
- ExposedHeaders: `Location`, `Operation-Id`, `traceId`

Example:
```csharp
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddCors(options =>
{
    options.AddPolicy("Frontend", policy =>
    {
        policy.WithOrigins("${FRONTEND_ORIGIN}")
            .AllowAnyHeader()
            .AllowAnyMethod()
            .WithExposedHeaders("Location", "Operation-Id", "traceId");
    });
});

var app = builder.Build();
app.UseCors("Frontend");
```

See: `.ai/assets/tech-stacks/dotnet-backend/shared/common-rules.md` for shared rules.

## Status
✅ Implemented in this project (verify if port differs).
