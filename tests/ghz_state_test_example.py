#

from quantunit import quantum_test, assert_probs
from qiskit import QuantumCircuit

@quantum_test
def ghz_state_test(qubits=6, expected={'000': 0.5, '111': 0.5}):
    n_shots = 4096
    qc = QuantumCircuit(qubits)
    qc.h(0)
    for q in range(qubits - 1):
        if q < qubits - 1:
            qc.cx(q, q+1)

    # Assert only '000' and '111'
    expected = {'000': 0.5, '111':0.5}
    assert_probs(qc, expected, shots=n_shots, tolerance=0.06)

if __name__ == "__main__":
    from quantunit.decorators import run_all_tests
    run_all_tests()