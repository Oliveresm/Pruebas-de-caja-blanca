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

# ============================================================================
# 3. Path Coverage (Caminos para lista de tamaño 2 -> 4^2 = 16 caminos)
# ============================================================================
@pytest.mark.path_coverage
@pytest.mark.parametrize(
    "input_values, expected_output",
    [
        ([2, 2], ["positivo", "par", "positivo", "par"]),  # C1 - C1
        ([2, 3], ["positivo", "par", "positivo"]),         # C1 - C2
        ([2, -2], ["positivo", "par", "par"]),             # C1 - C3
        ([2, -1], ["positivo", "par"]),                    # C1 - C4
        ([3, 2], ["positivo", "positivo", "par"]),         # C2 - C1
        ([3, 3], ["positivo", "positivo"]),                # C2 - C2
        ([3, -2], ["positivo", "par"]),                    # C2 - C3
        ([3, -1], ["positivo"]),                           # C2 - C4
        ([-2, 2], ["par", "positivo", "par"]),             # C3 - C1
        ([-2, 3], ["par", "positivo"]),                    # C3 - C2
        ([-2, -2], ["par", "par"]),                        # C3 - C3
        ([-2, -1], ["par"]),                               # C3 - C4
        ([-1, 2], ["positivo", "par"]),                    # C4 - C1
        ([-1, 3], ["positivo"]),                           # C4 - C2
        ([-1, -2], ["par"]),                               # C4 - C3
        ([-1, -1], []),                                    # C4 - C4
    ],
)
def test_path_coverage(input_values, expected_output):
    assert process_values(input_values) == expected_output