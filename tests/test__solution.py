from pyEQL.solution import Solution
from pyEQL import ureg

try:
    # Test 1: Initialize with 'ppb'
    sol = Solution({"Ca+2": "1000 ppb"})
    print("Test 1: Passed")
except Exception as e:
    print(f"Test 1: Failed - {e}")

try:
    # Test 2: Get amount in 'ppb'
    sol = Solution({"Ca+2": "1 ppm"})
    amount = sol.get_amount("Ca+2", "ppb")
    print(f"Test 2: Passed - Amount in 'ppb': {amount}")
except Exception as e:
    print(f"Test 2: Failed - {e}")

try:
    # Test 3: Get amount in '%'
    sol = Solution({"Ca+2": "1 ppm"})
    amount = sol.get_amount("Ca+2", "%")
    print(f"Test 3: Passed - Amount in '%': {amount}")
except Exception as e:
    print(f"Test 3: Failed - {e}")
