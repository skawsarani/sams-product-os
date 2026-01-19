#!/bin/bash

# PM Co-Pilot Evaluation Runner
# Validates backlog processing workflow against expected outputs

set -e

EVALS_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(dirname "$EVALS_DIR")"
FIXTURES_DIR="$EVALS_DIR/fixtures/test-backlogs"
EXPECTED_DIR="$EVALS_DIR/expected/outputs"
RESULTS_DIR="$EVALS_DIR/results/$(date +%Y-%m-%d-%H%M%S)"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Create results directory
mkdir -p "$RESULTS_DIR"

# Initialize counters
TOTAL_TESTS=0
PASSED_TESTS=0
FAILED_TESTS=0

echo "========================================="
echo "PM Co-Pilot Evaluation Suite"
echo "========================================="
echo ""
echo "Results will be saved to: $RESULTS_DIR"
echo ""

# Backup existing data
backup_existing_data() {
    echo "Backing up existing data..."
    if [ -d "$PROJECT_ROOT/tasks" ]; then
        cp -r "$PROJECT_ROOT/tasks" "$RESULTS_DIR/backup_tasks" 2>/dev/null || true
    fi
    if [ -d "$PROJECT_ROOT/knowledge/initiatives" ]; then
        cp -r "$PROJECT_ROOT/knowledge/initiatives" "$RESULTS_DIR/backup_initiatives" 2>/dev/null || true
    fi
    if [ -d "$PROJECT_ROOT/knowledge/references" ]; then
        cp -r "$PROJECT_ROOT/knowledge/references" "$RESULTS_DIR/backup_references" 2>/dev/null || true
    fi
    if [ -d "$PROJECT_ROOT/knowledge/notes" ]; then
        cp -r "$PROJECT_ROOT/knowledge/notes" "$RESULTS_DIR/backup_notes" 2>/dev/null || true
    fi
}

# Clean test data
clean_test_data() {
    echo "Cleaning test data..."
    rm -f "$PROJECT_ROOT/tasks"/*.md 2>/dev/null || true
    rm -rf "$PROJECT_ROOT/knowledge/initiatives" 2>/dev/null || true
    rm -f "$PROJECT_ROOT/knowledge/references"/*.md 2>/dev/null || true
    rm -rf "$PROJECT_ROOT/knowledge/notes" 2>/dev/null || true
    rm -f "$PROJECT_ROOT/BACKLOG.md" 2>/dev/null || true
}

# Restore backup
restore_backup() {
    echo "Restoring backup..."
    if [ -d "$RESULTS_DIR/backup_tasks" ]; then
        cp -r "$RESULTS_DIR/backup_tasks"/* "$PROJECT_ROOT/tasks/" 2>/dev/null || true
    fi
    if [ -d "$RESULTS_DIR/backup_initiatives" ]; then
        cp -r "$RESULTS_DIR/backup_initiatives" "$PROJECT_ROOT/knowledge/initiatives" 2>/dev/null || true
    fi
    if [ -d "$RESULTS_DIR/backup_references" ]; then
        cp -r "$RESULTS_DIR/backup_references"/* "$PROJECT_ROOT/knowledge/references/" 2>/dev/null || true
    fi
    if [ -d "$RESULTS_DIR/backup_notes" ]; then
        cp -r "$RESULTS_DIR/backup_notes" "$PROJECT_ROOT/knowledge/notes" 2>/dev/null || true
    fi
}

# Validate task count
validate_task_count() {
    local expected=$1
    local actual=$(find "$PROJECT_ROOT/tasks" -name "*.md" ! -name "README.md" 2>/dev/null | wc -l | tr -d ' ')

    if [ "$actual" -eq "$expected" ]; then
        echo -e "${GREEN}✓${NC} Task count: $actual (expected: $expected)"
        return 0
    else
        echo -e "${RED}✗${NC} Task count: $actual (expected: $expected)"
        return 1
    fi
}

# Validate initiative count
validate_initiative_count() {
    local expected=$1
    local actual=$(find "$PROJECT_ROOT/knowledge/initiatives" -name "*.md" 2>/dev/null | wc -l | tr -d ' ')

    if [ "$actual" -eq "$expected" ]; then
        echo -e "${GREEN}✓${NC} Initiative count: $actual (expected: $expected)"
        return 0
    else
        echo -e "${RED}✗${NC} Initiative count: $actual (expected: $expected)"
        return 1
    fi
}

# Validate reference count
validate_reference_count() {
    local expected=$1
    local actual=$(find "$PROJECT_ROOT/knowledge/references" -name "*.md" ! -name ".gitkeep" 2>/dev/null | wc -l | tr -d ' ')

    if [ "$actual" -eq "$expected" ]; then
        echo -e "${GREEN}✓${NC} Reference count: $actual (expected: $expected)"
        return 0
    else
        echo -e "${RED}✗${NC} Reference count: $actual (expected: $expected)"
        return 1
    fi
}

# Validate task category
validate_task_category() {
    local task_pattern=$1
    local expected_category=$2

    local task_file=$(grep -l "$task_pattern" "$PROJECT_ROOT/tasks"/*.md 2>/dev/null | head -1)
    if [ -z "$task_file" ]; then
        echo -e "${RED}✗${NC} Task matching '$task_pattern' not found"
        return 1
    fi

    local actual_category=$(grep "^category:" "$task_file" | awk '{print $2}')
    if [ "$actual_category" = "$expected_category" ]; then
        echo -e "${GREEN}✓${NC} Task '$task_pattern' category: $actual_category"
        return 0
    else
        echo -e "${RED}✗${NC} Task '$task_pattern' category: $actual_category (expected: $expected_category)"
        return 1
    fi
}

# Validate task priority
validate_task_priority() {
    local task_pattern=$1
    local expected_priority=$2

    local task_file=$(grep -l "$task_pattern" "$PROJECT_ROOT/tasks"/*.md 2>/dev/null | head -1)
    if [ -z "$task_file" ]; then
        echo -e "${RED}✗${NC} Task matching '$task_pattern' not found"
        return 1
    fi

    local actual_priority=$(grep "^priority:" "$task_file" | awk '{print $2}')
    if [ "$actual_priority" = "$expected_priority" ]; then
        echo -e "${GREEN}✓${NC} Task '$task_pattern' priority: $actual_priority"
        return 0
    else
        echo -e "${RED}✗${NC} Task '$task_pattern' priority: $actual_priority (expected: $expected_priority)"
        return 1
    fi
}

# Run test
run_test() {
    local test_name=$1
    local test_file="$FIXTURES_DIR/${test_name}.md"

    if [ ! -f "$test_file" ]; then
        echo -e "${RED}Test file not found: $test_file${NC}"
        return 1
    fi

    echo "----------------------------------------"
    echo "Running test: $test_name"
    echo "----------------------------------------"

    # Copy test backlog
    cp "$test_file" "$PROJECT_ROOT/BACKLOG.md"

    # Save test snapshot
    cp "$test_file" "$RESULTS_DIR/${test_name}-input.md"

    echo ""
    echo "✋ MANUAL STEP REQUIRED:"
    echo "1. Process the backlog by telling your AI: '/backlog'"
    echo "2. Review the output"
    echo "3. Press ENTER when done to validate results"
    echo ""
    read -p "Press ENTER after processing backlog..."

    # Save outputs
    mkdir -p "$RESULTS_DIR/${test_name}"
    cp -r "$PROJECT_ROOT/tasks" "$RESULTS_DIR/${test_name}/" 2>/dev/null || true
    if [ -d "$PROJECT_ROOT/knowledge/initiatives" ]; then
        cp -r "$PROJECT_ROOT/knowledge/initiatives" "$RESULTS_DIR/${test_name}/" 2>/dev/null || true
    fi
    if [ -d "$PROJECT_ROOT/knowledge/references" ]; then
        cp -r "$PROJECT_ROOT/knowledge/references" "$RESULTS_DIR/${test_name}/" 2>/dev/null || true
    fi

    return 0
}

# Main test execution
echo "Starting evaluation suite..."
echo ""

# Backup existing data
backup_existing_data

# Test 1: Basic Categorization
clean_test_data
TOTAL_TESTS=$((TOTAL_TESTS + 1))
if run_test "basic-categorization"; then
    echo ""
    echo "Validating basic-categorization results..."
    TEST_PASSED=true

    validate_task_count 2 || TEST_PASSED=false
    validate_initiative_count 1 || TEST_PASSED=false
    validate_reference_count 1 || TEST_PASSED=false
    validate_task_category "authentication" "technical" || TEST_PASSED=false
    validate_task_category "Email Sarah" "outreach" || TEST_PASSED=false

    if [ "$TEST_PASSED" = true ]; then
        echo -e "${GREEN}✓ Test PASSED: basic-categorization${NC}"
        PASSED_TESTS=$((PASSED_TESTS + 1))
    else
        echo -e "${RED}✗ Test FAILED: basic-categorization${NC}"
        FAILED_TESTS=$((FAILED_TESTS + 1))
    fi
else
    echo -e "${RED}✗ Test FAILED: basic-categorization${NC}"
    FAILED_TESTS=$((FAILED_TESTS + 1))
fi

# Test 2: Auto-Categorization
clean_test_data
TOTAL_TESTS=$((TOTAL_TESTS + 1))
if run_test "auto-categorization"; then
    echo ""
    echo "Validating auto-categorization results..."
    TEST_PASSED=true

    validate_task_count 5 || TEST_PASSED=false
    validate_task_category "API bug" "technical" || TEST_PASSED=false
    validate_task_category "Email John" "outreach" || TEST_PASSED=false
    validate_task_category "Research user" "research" || TEST_PASSED=false
    validate_task_category "Write release" "writing" || TEST_PASSED=false
    validate_task_category "Schedule offsite" "admin" || TEST_PASSED=false

    if [ "$TEST_PASSED" = true ]; then
        echo -e "${GREEN}✓ Test PASSED: auto-categorization${NC}"
        PASSED_TESTS=$((PASSED_TESTS + 1))
    else
        echo -e "${RED}✗ Test FAILED: auto-categorization${NC}"
        FAILED_TESTS=$((FAILED_TESTS + 1))
    fi
else
    echo -e "${RED}✗ Test FAILED: auto-categorization${NC}"
    FAILED_TESTS=$((FAILED_TESTS + 1))
fi

# Test 3: Priority Caps (manual validation)
clean_test_data
TOTAL_TESTS=$((TOTAL_TESTS + 1))
echo "----------------------------------------"
echo "Running test: priority-caps"
echo "----------------------------------------"
echo ""
echo "This test validates priority cap enforcement."
echo "When you process the backlog, the AI should:"
echo "1. Identify 4 P0-priority items"
echo "2. Warn that P0 cap (3) would be exceeded"
echo "3. Ask you to deprioritize one task"
echo ""
cp "$FIXTURES_DIR/priority-caps.md" "$PROJECT_ROOT/BACKLOG.md"
echo "✋ MANUAL VALIDATION REQUIRED:"
echo "1. Process with '/backlog'"
echo "2. Verify AI warns about P0 cap"
echo "3. Answer the deprioritization question"
echo ""
read -p "Did AI enforce priority cap correctly? (y/n): " priority_cap_enforced

if [ "$priority_cap_enforced" = "y" ]; then
    echo -e "${GREEN}✓ Test PASSED: priority-caps${NC}"
    PASSED_TESTS=$((PASSED_TESTS + 1))
else
    echo -e "${RED}✗ Test FAILED: priority-caps${NC}"
    FAILED_TESTS=$((FAILED_TESTS + 1))
fi

# Clean up and restore
clean_test_data
restore_backup

# Summary
echo ""
echo "========================================="
echo "Evaluation Summary"
echo "========================================="
echo "Total tests: $TOTAL_TESTS"
echo -e "Passed: ${GREEN}$PASSED_TESTS${NC}"
echo -e "Failed: ${RED}$FAILED_TESTS${NC}"
echo ""
echo "Results saved to: $RESULTS_DIR"
echo ""

if [ $FAILED_TESTS -eq 0 ]; then
    echo -e "${GREEN}All tests passed! ✓${NC}"
    exit 0
else
    echo -e "${RED}Some tests failed. Review results above.${NC}"
    exit 1
fi
