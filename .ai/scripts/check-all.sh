#!/bin/bash

# ====================================================================
# Comprehensive Project Check Script (.NET)
# 
# Purpose: 執行所有專案檢查腳本，提供完整的專案健康報告
# Usage: ./check-all.sh [--quick | --full | --critical]
# ====================================================================

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

# Parse arguments
MODE="full"
if [ "$1" == "--quick" ]; then
    MODE="quick"
elif [ "$1" == "--critical" ]; then
    MODE="critical"
elif [ "$1" == "--full" ]; then
    MODE="full"
elif [ "$1" == "--help" ] || [ "$1" == "-h" ]; then
    echo "Usage: $0 [--quick | --full | --critical]"
    echo ""
    echo "Modes:"
    echo "  --quick    : Only run fast, critical checks"
    echo "  --critical : Only run the most important checks"
    echo "  --full     : Run all available checks (default)"
    echo ""
    exit 0
fi

# Track results
TOTAL_CHECKS=0
PASSED_CHECKS=0
FAILED_CHECKS=0
SKIPPED_CHECKS=0
WARNINGS=0

# Function to run a check script
run_check() {
    local script_name=$1
    local description=$2
    local is_critical=$3
    local is_quick=$4
    shift 4
    local args=("$@")
    
    # Skip logic based on mode
    if [ "$MODE" == "critical" ] && [ "$is_critical" != "true" ]; then
        echo -e "${YELLOW}⊖${NC} Skipping: $description (non-critical)"
        SKIPPED_CHECKS=$((SKIPPED_CHECKS + 1))
        return
    fi
    
    if [ "$MODE" == "quick" ] && [ "$is_quick" != "true" ]; then
        echo -e "${YELLOW}⊖${NC} Skipping: $description (not quick)"
        SKIPPED_CHECKS=$((SKIPPED_CHECKS + 1))
        return
    fi
    
    TOTAL_CHECKS=$((TOTAL_CHECKS + 1))
    
    echo ""
    echo -e "${CYAN}▶ Running:${NC} $description"
    echo "  Script: $script_name"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    
    if [ -f "$SCRIPT_DIR/$script_name" ]; then
        if [ -x "$SCRIPT_DIR/$script_name" ]; then
            # Run the script and capture exit code
            if "$SCRIPT_DIR/$script_name" "${args[@]}" 2>&1; then
                echo -e "${GREEN}✓ PASSED${NC}: $description"
                PASSED_CHECKS=$((PASSED_CHECKS + 1))
            else
                echo -e "${RED}✗ FAILED${NC}: $description"
                FAILED_CHECKS=$((FAILED_CHECKS + 1))
            fi
        else
            echo -e "${YELLOW}⚠ WARNING${NC}: $script_name is not executable"
            echo "  Run: chmod +x $SCRIPT_DIR/$script_name"
            WARNINGS=$((WARNINGS + 1))
        fi
    else
        echo -e "${RED}✗ ERROR${NC}: $script_name not found"
        FAILED_CHECKS=$((FAILED_CHECKS + 1))
    fi
    
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
}

run_command_check() {
    local command_text=$1
    local description=$2
    local is_critical=$3
    local is_quick=$4

    if [ "$MODE" == "critical" ] && [ "$is_critical" != "true" ]; then
        echo -e "${YELLOW}⊖${NC} Skipping: $description (non-critical)"
        SKIPPED_CHECKS=$((SKIPPED_CHECKS + 1))
        return
    fi

    if [ "$MODE" == "quick" ] && [ "$is_quick" != "true" ]; then
        echo -e "${YELLOW}⊖${NC} Skipping: $description (not quick)"
        SKIPPED_CHECKS=$((SKIPPED_CHECKS + 1))
        return
    fi

    TOTAL_CHECKS=$((TOTAL_CHECKS + 1))

    echo ""
    echo -e "${CYAN}▶ Running:${NC} $description"
    echo "  Command: $command_text"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

    if (cd "$PROJECT_ROOT" && eval "$command_text"); then
        echo -e "${GREEN}✓ PASSED${NC}: $description"
        PASSED_CHECKS=$((PASSED_CHECKS + 1))
    else
        echo -e "${RED}✗ FAILED${NC}: $description"
        FAILED_CHECKS=$((FAILED_CHECKS + 1))
    fi

    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
}

# Function to mark a check as pending dotnet-native replacement
run_check_pending() {
    local script_name=$1
    local description=$2
    local is_critical=$3
    local is_quick=$4
    local reason=${5:-"dotnet-native replacement pending"}

    # Skip logic based on mode
    if [ "$MODE" == "critical" ] && [ "$is_critical" != "true" ]; then
        echo -e "${YELLOW}⊖${NC} Skipping: $description (non-critical)"
        SKIPPED_CHECKS=$((SKIPPED_CHECKS + 1))
        return
    fi

    if [ "$MODE" == "quick" ] && [ "$is_quick" != "true" ]; then
        echo -e "${YELLOW}⊖${NC} Skipping: $description (not quick)"
        SKIPPED_CHECKS=$((SKIPPED_CHECKS + 1))
        return
    fi

    echo -e "${YELLOW}⊖${NC} TODO: $description ($reason)"
    SKIPPED_CHECKS=$((SKIPPED_CHECKS + 1))
}

run_spec_compliance_check() {
    local spec_file="${SPEC_FILE:-}"
    local task_name="${TASK_NAME:-}"

    if [ -z "$spec_file" ] || [ -z "$task_name" ]; then
        echo -e "${YELLOW}⊖${NC} Skipping: Spec Implementation Compliance (SPEC_FILE/TASK_NAME not set)"
        SKIPPED_CHECKS=$((SKIPPED_CHECKS + 1))
        return
    fi

    run_check "check-spec-compliance.sh" \
        "Spec Implementation Compliance (.NET)" \
        "false" "true" "$spec_file" "$task_name"
}

# Header
echo ""
echo -e "${MAGENTA}╔════════════════════════════════════════╗${NC}"
echo -e "${MAGENTA}║    Comprehensive Project Check         ║${NC}"
echo -e "${MAGENTA}║    Mode: ${YELLOW}$MODE${MAGENTA}                          ║${NC}"
echo -e "${MAGENTA}╚════════════════════════════════════════╝${NC}"
echo ""
echo -e "${BLUE}Starting checks at $(date '+%Y-%m-%d %H:%M:%S')${NC}"

# ====================================================================
# Critical Checks (always run in quick and critical modes)
# ====================================================================

echo ""
echo -e "${MAGENTA}════ Critical Checks ════${NC}"

run_command_check "python .ai/scripts/validate-workflow-artifacts.py" \
    "Workflow Artifact Metadata" \
    "true" "true"

run_command_check "python .ai/scripts/validate-ai-context.py" \
    "AI Context Navigation and Runtime Contracts" \
    "true" "true"

run_command_check "python .ai/scripts/validate-shell-assets.py" \
    "Shell Asset Classification And Git Modes" \
    "true" "true"

# Coding standards are fundamental for AI context and standards docs
run_check "check-coding-standards.sh" \
    "Coding Standards Compliance" \
    "true" "true"

run_command_check "dotnet test tools/DotnetBackendAnalyzers.Tests/DotnetBackendAnalyzers.Tests.csproj" \
    "Dotnet Backend Analyzer Template Tests" \
    "true" "true"

run_command_check "dotnet test tools/DotnetBackendValidation.Tests/DotnetBackendValidation.Tests.csproj" \
    "Dotnet Backend Configuration Validation Tests" \
    "true" "true"

# Repository source validation is covered by DBA1001 in analyzer tests.
# Mapper source validation is covered by DBA1007-DBA1008 in analyzer tests.

# ====================================================================
# Important Checks (run in full and quick modes)
# ====================================================================

if [ "$MODE" != "critical" ]; then
    echo ""
    echo -e "${MAGENTA}════ Important Checks ════${NC}"
    
    # Aggregate and UseCase source validation is covered by DBA1002-DBA1003 and DBA1009-DBA1012.
    
    # Controller compliance is covered by DBA1004-DBA1006 in analyzer tests.

    # Projection source and EF model registration are covered by DBA1013 and configuration validation tests.
    
    # Spec compliance is important
    run_spec_compliance_check
    
    # Dependencies check (dotnet-native replacement not yet available)
    run_check_pending "check-dependencies.sh" \
        "Dependencies and Versions" \
        "false" "true" "dotnet-native replacement not yet available"
fi

# ====================================================================
# Additional Checks (only in full mode)
# ====================================================================

if [ "$MODE" == "full" ]; then
    echo ""
    echo -e "${MAGENTA}════ Additional Checks ════${NC}"
    
    # Test compliance
    run_check "check-test-compliance.sh" \
        "Test Standards Compliance" \
        "false" "false"
    
    # Test DI compliance helper remains transitional
    run_check_pending "check-test-di-compliance.sh" \
        "Test DI Compliance" \
        "true" "false" "replace with analyzer or test architecture rules"
    
    # Archive compliance
    run_check "check-archive-compliance.sh" \
        "Archive Pattern Compliance" \
        "false" "false"
    
    # Template sync check (dotnet-native replacement not yet available)
    run_check_pending "check-template-sync.sh" \
        "Template Synchronization" \
        "false" "false" "dotnet-native replacement not yet available"
    
    # ADR index update (dotnet-native replacement not yet available)
    run_check_pending "update-adr-index.sh" \
        "ADR Index Update" \
        "false" "false" "dotnet-native replacement not yet available"
    
    # Add ADR script (if needed)
    if [ -f "$SCRIPT_DIR/add-adr.sh" ]; then
        echo -e "${CYAN}ℹ${NC} add-adr.sh is available for creating new ADRs"
    fi
fi

# ====================================================================
# Results Summary
# ====================================================================

echo ""
echo -e "${MAGENTA}╔════════════════════════════════════════╗${NC}"
echo -e "${MAGENTA}║           Check Results Summary        ║${NC}"
echo -e "${MAGENTA}╚════════════════════════════════════════╝${NC}"
echo ""

# Calculate statistics
if [ $TOTAL_CHECKS -gt 0 ]; then
    PASS_RATE=$((PASSED_CHECKS * 100 / TOTAL_CHECKS))
else
    PASS_RATE=0
fi

# Display results with colors
echo -e "Total Checks Run: ${CYAN}$TOTAL_CHECKS${NC}"
echo -e "Passed: ${GREEN}$PASSED_CHECKS${NC}"
echo -e "Failed: ${RED}$FAILED_CHECKS${NC}"
echo -e "Skipped: ${YELLOW}$SKIPPED_CHECKS${NC}"
echo -e "Warnings: ${YELLOW}$WARNINGS${NC}"
echo -e "Pass Rate: ${CYAN}${PASS_RATE}%${NC}"

echo ""
echo -e "${BLUE}Completed at $(date '+%Y-%m-%d %H:%M:%S')${NC}"
echo ""

# Overall status
if [ $FAILED_CHECKS -eq 0 ] && [ $WARNINGS -eq 0 ]; then
    echo -e "${GREEN}╔════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║    ✓ All Checks Passed Successfully!   ║${NC}"
    echo -e "${GREEN}╚════════════════════════════════════════╝${NC}"
    exit 0
elif [ $FAILED_CHECKS -eq 0 ]; then
    echo -e "${YELLOW}╔════════════════════════════════════════╗${NC}"
    echo -e "${YELLOW}║  ⚠ Passed with $WARNINGS Warning(s)          ║${NC}"
    echo -e "${YELLOW}╚════════════════════════════════════════╝${NC}"
    exit 0
else
    echo -e "${RED}╔════════════════════════════════════════╗${NC}"
    echo -e "${RED}║    ✗ $FAILED_CHECKS Check(s) Failed!              ║${NC}"
    echo -e "${RED}╚════════════════════════════════════════╝${NC}"
    
    # Provide helpful next steps
    echo ""
    echo -e "${YELLOW}Next Steps:${NC}"
    echo "1. Review the failed checks above"
    echo "2. Run individual scripts for detailed errors"
    echo "3. Fix the issues and run this check again"
    echo ""
    
    exit 1
fi
