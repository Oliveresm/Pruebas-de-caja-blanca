import pytest
from process import process_values

# ============================================================================
# 1. Statement Coverage
# ============================================================================
@pytest.mark.statement_coverage
@pytest.mark.parametrize(
    "input_values, expected_output",
    [
        ([2], ["positivo", "par"]),  # Ejecuta todos los statements de append
    ],
)
def test_statement_coverage(input_values, expected_output):
    assert process_values(input_values) == expected_output

# ============================================================================
# 2. Branch Coverage (Decision Coverage)
# ============================================================================
@pytest.mark.branch_coverage
@pytest.mark.parametrize(
    "input_values, expected_output",
    [
        ([2], ["positivo", "par"]),  # D1: V, D2: V
        ([-3], []),                  # D1: F, D2: F
    ],
)
def test_branch_coverage(input_values, expected_output):
    assert process_values(input_values) == expected_output

