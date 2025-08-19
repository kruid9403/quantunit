def initialize_register(qc, qubit_indices, bitstring):
    """Set qubits to the bitstring value by applying X where needed."""
    for q, bit in zip(qubit_indices, bitstring):
        if bit == "1":
            qc.x(q)
