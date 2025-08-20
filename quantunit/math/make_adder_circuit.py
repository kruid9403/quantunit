from qiskit import QuantumCircuit
from qiskit.circuit.library import CDKMRippleCarryAdder
from quantunit.helpers.bitstrings import int_to_bitstring
from quantunit.helpers.quantum_init import initialize_register

def make_adder_circuit(a, b, n=None):
    n_a = max(a.bit_length(), 1)
    n_b = max(b.bit_length(), 1)
    n = n or max(n_a, n_b)  # allow explicit override

    # Qubit layout: [cin][a0..a_{n-1}][b0..b_{n-1}][cout]
    qc = QuantumCircuit(2*n + 2, n+1)

    # Prepare a and b (little-endian, qubits [1..n], [n+1..2n])
    a_bits = int_to_bitstring(a, n)
    b_bits = int_to_bitstring(b, n)
    initialize_register(qc, range(1, 1+n), a_bits)
    initialize_register(qc, range(1+n, 1+2*n), b_bits)

    rc_adder = CDKMRippleCarryAdder(n)
    qc.append(rc_adder, qc.qubits)

    # Measure sum (b-reg) to clbits 0..n-1, carry-out to clbit n
    for i in range(n):
        qc.measure(1+n+i, i)
    qc.measure(2*n+1, n)
    return qc
