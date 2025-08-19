def measure_qubits(qc, qubit_indices, clbit_indices):
    for q, c in zip(qubit_indices, clbit_indices):
        qc.measure(q, c)
