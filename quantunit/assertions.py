from qiskit_aer import Aer
from qiskit import transpile

def assert_probs(circuit, expected_probs, shots=1024, tolerance=0.1):
    simulator = Aer.get_backend('aer_simulator')
    # Ensure measurement: add if missing
    # If circuit already has measurement(s), this is a no-op.
    measured_circuit = circuit.copy()
    if not measured_circuit.num_clbits:
        measured_circuit.measure_all()
    t_circ = transpile(measured_circuit, simulator)
    # Run the circuit
    result = simulator.run(t_circ, shots=shots).result()

    try:
        counts = result.get_counts()
    except Exception as e:
        print("Error: result does not have counts. Details:", e)
        print("Result object:", result)
        raise AssertionError("Simulation did not return measurement counts. Does your circuit contain measurements?") from e

    # Convert counts to probabilities
    prob_counts = {k: v / shots for k, v in counts.items()}

    errors = []
    for key, expected in expected_probs.items():
        actual = prob_counts.get(key, 0.0)
        if abs(actual - expected) > tolerance:
            errors.append(f"Key {key}: got {actual:.3f}, wanted {expected:.3f} (tolerance {tolerance})")
    if errors:
        raise AssertionError("Probabilities not close!\n" + "\n".join(errors))