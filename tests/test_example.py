from quantunit import quantum_test, assert_probs
# import qiskit will be needed for real tests

@quantum_test
def test_bell_state():
    # (stub; replace with real Qiskit code later!)
    assert_probs({}, {'00': 0.5, '11': 0.5})  # this will fail, as expected for placeholder

if __name__ == "__main__":
    from quantunit.decorators import run_all_tests
    run_all_tests()