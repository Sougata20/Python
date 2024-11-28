def is_convex_fuzzy_set(fuzzy_set):
    membership_degrees = list(fuzzy_set.values())
    
    for i in range(1, len(membership_degrees) - 1):
        if membership_degrees[i] < min(membership_degrees[i - 1], membership_degrees[i + 1]):
            return False
    
    return True

# Example fuzzy set
fuzzy_set = {
    'a': 1.0,
    'b': 0.8,
    'c': 0.6,
    'd': 0.8,
    'e': 1.0
}

# Check if the fuzzy set is convex
if is_convex_fuzzy_set(fuzzy_set):
    print("The fuzzy set is convex.")
else:
    print("The fuzzy set is not convex.")
