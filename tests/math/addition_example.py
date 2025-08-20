from quantunit import quantum_test
from quantunit.math.q_addition_asserts import q_addition_asserts
from quantunit.math.make_adder_circuit import make_adder_circuit
import random
from quantunit.helpers.random_utils import random_nbit_int

@quantum_test
def test_q_addition():
    n = 8  # test 4-bit adders; adjust as needed
    rng = random.Random(4)  # for reproducibility
    for _ in range(2):
        a = random_nbit_int(n, rng=rng)
        b = random_nbit_int(n, rng=rng)
        print(f"a {a}, b {b}, sum {a + b}")
        circuit = make_adder_circuit(a, b, n=n)
        q_addition_asserts(circuit, a, b)


if __name__ == "__main__":
    from quantunit.decorators import run_all_tests
    run_all_tests()