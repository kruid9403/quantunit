# Simple test registry and decorator

_registered_tests = []

def quantum_test(fn):
    _registered_tests.append(fn)
    return fn

def run_all_tests():
    print("Running quantum tests...\n")
    passed, failed = 0, 0
    for test_fn in _registered_tests:
        try:
            test_fn()
            print(f"PASS: {test_fn.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"FAIL: {test_fn.__name__} - {e}")
            failed += 1
    print(f"\nSummary: {passed} passed, {failed} failed.")
