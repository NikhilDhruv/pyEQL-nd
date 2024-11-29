from pyEQL.solution import Solution

# Test initialization with 'ppb'
try:
    s = Solution({"Ca+2": "1000 ppb"})
    print(f"Amount of Ca+2 in ppb: {s.get_amount('Ca+2', 'ppb')}")
except Exception as e:
    print(f"Test failed for 'ppb': {e}")

# Test initialization with '%'
try:
    s = Solution({"Na+": "0.5%"})
    print(f"Amount of Na+ in percent: {s.get_amount('Na+', 'percent')}")
except Exception as e:
    print(f"Test failed for '%': {e}")
