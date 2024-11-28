# Function to implement Maxima Method
def maxima_method(fuzzy_set):
    # Find the element with the maximum membership value
    max_element = max(fuzzy_set, key=fuzzy_set.get)
    return max_element, fuzzy_set[max_element]

# Function to implement Centroid Method
def centroid_method(fuzzy_set):
    numerator = 0
    denominator = 0
    for element, membership in fuzzy_set.items():
        numerator += membership * float(element)  # Assuming the element is numeric
        denominator += membership
    if denominator != 0:
        centroid = numerator / denominator
        return centroid
    else:
        return None  # Handle case where denominator is 0

# Function to implement Weighted Average Method
def weighted_average_method(fuzzy_set):
    numerator = 0
    denominator = 0
    for element, membership in fuzzy_set.items():
        numerator += membership * float(element)  # Assuming the element is numeric
        denominator += membership
    if denominator != 0:
        weighted_avg = numerator / denominator
        return weighted_avg
    else:
        return None  # Handle case where denominator is 0

# Function to get user input for fuzzy set
def get_user_fuzzy_set():
    fuzzy_set = {}
    print("Enter the elements of the fuzzy set. Type 'done' to finish.")
    
    while True:
        element = input("Enter element (numeric value): ")
        if element.lower() == 'done':
            break
        membership_value = float(input(f"Enter membership value for {element} (between 0 and 1): "))
        
        # Ensure the membership value is valid
        if 0 <= membership_value <= 1:
            fuzzy_set[element] = membership_value
        else:
            print("Invalid membership value. Please enter a value between 0 and 1.")
    
    return fuzzy_set

# Get user-defined fuzzy set
user_fuzzy_set = get_user_fuzzy_set()

# De-fuzzify using Maxima Method
maxima_value, max_membership = maxima_method(user_fuzzy_set)
print(f"Maxima Method: Element with max membership is '{maxima_value}' with membership degree {max_membership}.")

# De-fuzzify using Centroid Method
centroid_value = centroid_method(user_fuzzy_set)
if centroid_value is not None:
    print(f"Centroid Method: The centroid value is {centroid_value}.")
else:
    print("Centroid Method: No valid centroid (denominator is 0).")

# De-fuzzify using Weighted Average Method
weighted_avg_value = weighted_average_method(user_fuzzy_set)
if weighted_avg_value is not None:
    print(f"Weighted Average Method: The weighted average value is {weighted_avg_value}.")
else:
    print("Weighted Average Method: No valid weighted average (denominator is 0).")
