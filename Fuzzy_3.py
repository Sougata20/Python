# Function to check if a fuzzy set is normal
def is_normal(fuzzy_set):
    # Check if the maximum membership value is 1
    return max(fuzzy_set) == 1

# Example fuzzy sets
fuzzy_set_1 = [0.1, 0.5, 0.7, 1.0]
fuzzy_set_2 = [0.3, 0.6, 0.8, 0.9]

# Check if fuzzy sets are normal
print("Fuzzy set 1 is normal:", is_normal(fuzzy_set_1))  # Expected: True
print("Fuzzy set 2 is normal:", is_normal(fuzzy_set_2))  # Expected: False
