import sys
import os

# Add the parent directory to the Python path so 'src' can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from solution import Solution

def test_solution():
    """
    Test the Solution class for handling units like 'ppb' and '%'.
    """
    try:
        # Create a Solution instance with a solute using 'ppb'
        s = Solution({'Ca+2': '1000 ppb'})
        print("Solution initialized successfully with 'ppb'.")

        # Test get_amount for ppb
        amount_ppb = s.get_amount('Ca+2', 'ppb')
        print(f"Amount in ppb: {amount_ppb}")

        # Test get_amount for %
        amount_percent = s.get_amount('Ca+2', '%')
        print(f"Amount in %: {amount_percent}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    test_solution()
