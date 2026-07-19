#!/usr/bin/env bash

set -euo pipefail

echo "Installing Python dependencies..."

python -m pip install --upgrade pip

if [[ -f requirements.txt ]]; then
    python -m pip install -r requirements.txt
else
    echo "requirements.txt not found; skipping Python dependency installation."
fi

echo "Restoring .NET projects..."

if [[ -d tools ]]; then
    while IFS= read -r -d '' project; do
        echo "Restoring ${project}"
        dotnet restore "${project}"
    done < <(find tools -type f -name '*.csproj' -print0)
else
    echo "tools directory not found; skipping .NET restore."
fi

echo "Development environment initialization completed."