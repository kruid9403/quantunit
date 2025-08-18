from quantunit import quantum_test, assert_probs
from qiskit import QuantumCircuit

@quantum_test
def test_bell_state():
   qc = QuantumCircuit(2)
   qc.h(0)
   qc.cx(0,1)
   # Assertion handles measurements

   # Bell state: should see'00' and '11' about equally likely
   expected = {'00':0.5, '11':0.5}
   assert_probs(qc, expected, shots=1024, tolerance=0.1)

if __name__ == "__main__":
    from quantunit.decorators import run_all_tests
    run_all_tests()