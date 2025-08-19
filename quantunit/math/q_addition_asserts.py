from unittest import result
from qiskit_aer import Aer
from qiskit import transpile
from qiskit_aer.noise import NoiseModel
from qiskit_ibm_runtime.fake_provider import FakeManilaV2

def q_addition_asserts(circuit, a, b, shots=1024, threshold=0.9):
    n_a = max(a.bit_length(), 1)
    n_b = max(b.bit_length(), 1)
    n = max(n_a, n_b)
    string_length = n + 1  # n sum bits + 1 carry-out bit

    simulator = Aer.get_backend('aer_simulator')
    measured_circuit = circuit.copy()
    if not measured_circuit.num_clbits:
        measured_circuit.measure_all()

    tqc = transpile(measured_circuit, simulator)
    noise_model = NoiseModel.from_backend(FakeManilaV2())
    job = simulator.run(tqc, shots=shots, noise_model=noise_model)
    result = job.result()
    counts = result.get_counts()
    print("Observed bitstrings:", counts)

    # Bitstrings are right-to-left (little endian): [sum bits][carry out], so use total string_length
    expected_sum = a + b
    expected_sum_str = format(expected_sum, f'0{string_length}b')

    appearances = sum(count for bitstring, count in counts.items()
                     if bitstring[-string_length:] == expected_sum_str)
    fraction = appearances / shots
    print(f"Fraction with correct sum {expected_sum_str}: {fraction:.2f}")

    if fraction < threshold:
        raise AssertionError(
            f"Expected sum {expected_sum_str} in output, "
            f"but found in only {fraction*100:.1f}% of results."
        )