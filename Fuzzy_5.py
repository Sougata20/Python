# Function to check if a fuzzy set is a singleton
def is_singleton(fuzzy_set):
    # Count how many elements have membership degree equal to 1
    return fuzzy_set.count(1) == 1 and all(x <= 1 for x in fuzzy_set)

# Example fuzzy sets
fuzzy_set_1 = [0.0, 0.0, 1.0, 0.0]
fuzzy_set_2 = [0.0, 0.5, 0.7, 0.9]
fuzzy_set_3 = [0.0, 0.0, 0.5, 0.0]

# Check if fuzzy sets are singleton
print("Fuzzy set 1 is singleton:", is_singleton(fuzzy_set_1))  # Expected: True
print("Fuzzy set 2 is singleton:", is_singleton(fuzzy_set_2))  # Expected: False
print("Fuzzy set 3 is singleton:", is_singleton(fuzzy_set_3))  # Expected: False
