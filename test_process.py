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


