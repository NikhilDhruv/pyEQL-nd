import sys
import os

# Add the path to the pyEQL package if it's not installed as a package yet
# Replace '/path/to/pyEQL-nd' with the actual path to your pyEQL-nd directory
sys.path.append('/Users/Nikhil/Documents/GitHub/pyEQL-nd ')

from pyEQL.solution import Solution

# Test Cases
def test_solution_init_with_supported_units():
    try:
        # Initialize with a valid unit
        s = Solution({'Ca+2': '1000 ppb'})
        print("Test 1: Passed - Solution initialized with 'ppb'")
    except Exception as e:
        print("Test 1: Failed -", e)

def test_get_amount_with_different_units():
    try:
        # Initialize the solution
        s = Solution({'Ca+2': '1 ppm'})
        
        # Get amount in 'ppb'
        ppb_amount = s.get_amount('Ca+2', 'ppb')
        print("Test 2: Passed - Amount in 'ppb':", ppb_amount)
        
        # Get amount in '%'
        percent_amount = s.get_amount('Ca+2', '%')
        print("Test 3: Passed - Amount in '%':", percent_amount)
    except Exception as e:
        print("Test 2/3: Failed -", e)

# Run tests
if __name__ == "__main__":
    print("Running tests for pyEQL Solution class...\n")
    
    test_solution_init_with_supported_units()
    test_get_amount_with_different_units()
