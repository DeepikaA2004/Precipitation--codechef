def categorize_rainfall(X):
    if X < 3:
        return "LIGHT"
    elif X < 7:
        return "MODERATE"
    else:
        return "HEAVY"

# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read X for each test case
    X = int(input())
    
    # Categorize the rainfall
    result = categorize_rainfall(X)
    
    # Print the result
    print(result)
