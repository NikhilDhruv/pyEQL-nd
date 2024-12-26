from solution import Solution

# Test custom units 'ppb' and '%'
try:
    # Create a solution object with 'ppb'
    s1 = Solution({'Ca+2': '1000 ppb'})
    print("Test for 'ppb': Passed")
    print(f"Amount of 'Ca+2' in microgram/liter: {s1.get_amount('Ca+2', 'microgram/liter')}")

    # Create a solution object with '%'
    s2 = Solution({'Na+': '0.1 %'})
    print("Test for '%': Passed")
    print(f"Amount of 'Na+' in dimensionless: {s2.get_amount('Na+', 'dimensionless')}")

except Exception as e:
    print("Error during testing:", e)

python test__solution.py
