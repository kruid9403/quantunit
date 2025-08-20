from qiskit_aer import Aer
from qiskit.circuit import QuantumRegister, QuantumCircuit
from qiskit_aer.noise import NoiseModel
from qiskit_ibm_runtime.fake_provider import FakeManilaV2
import random

width = 8
max_weight = 10  # Example max weight, adjust as needed
shots = 2048

list_length = 10
max_weight = 100
max_value = 150

noise = NoiseModel.from_backend(FakeManilaV2())

class Knapsack:
    def __init__(self, item_list, shots, max_weight, noise):
        self.item_list = item_list
        self.register_size = len(item_list)
        self.register = QuantumRegister(len(item_list), 'included')
        self.qc = QuantumCircuit(len(item_list))
        self.backend = Aer.get_backend('aer_simulator')
        self.shots = shots
        self.counts = None
        self.max_weight = max_weight
        self.noise = noise
        self.create_superposition()
        self.measure_circuit()
        self.clean_counts()
        self.calculate_value()

    def create_superposition(self):
        for i in range(self.register_size):
            self.qc.h(i)
    
    def measure_circuit(self):
        measured = self.qc.copy()
        measured.measure_all()
        result = self.backend.run(measured, shots=self.shots, noise_model=self.noise).result()
        self.counts = result.get_counts()
        print(self.counts)

    def clean_counts(self):
        if self.counts is None:
            print("No measurement results available.")
            return

        # Remove any bitstrings that exceed the max weight
        self.counts = {
            bitstring: count
            for bitstring, count in self.counts.items()
            if sum(self.item_list[i][0] for i in range(len(bitstring)) if bitstring[i] == '1') <= self.max_weight
        }

    def calculate_value(self):
        if self.counts is None:
            print("No measurement results available.")
            return

        for bitstring, count in self.counts.items():
            value = sum(self.item_list[i][1] for i in range(len(bitstring)) if bitstring[i] == '1')
            weight = sum(self.item_list[i][0] for i in range(len(bitstring)) if bitstring[i] == '1')
            print(f"Value of {bitstring} {weight} : {value} : {count}")

def generate_item_list(list_length, max_weight, max_value):
    """Generates a list of length `list_length` of (weight, value) tuples,
       each with random int 1..max_weight and 1..max_value."""
    return [
        (random.randint(1, max_weight), random.randint(1, max_value))
        for _ in range(list_length)
    ]


if __name__ == "__main__":
    item_list = generate_item_list(list_length, max_weight, max_value)
    print("Random Items:", item_list)
    
    sack = Knapsack(
        item_list = item_list, 
        shots=shots, 
        max_weight=max_weight, 
        noise=noise,
    )

    print(item_list)

