# Function to find the alpha-cut of a fuzzy set
def alpha_cut(fuzzy_set, alpha):
    # Create a crisp set containing elements whose membership degree is >= alpha
    return [i for i, membership in enumerate(fuzzy_set) if membership >= alpha]

# Example fuzzy set
fuzzy_set = [0.1, 0.5, 0.7, 1.0, 0.3, 0.8]

# Define alpha values
alpha1 = 0.5
alpha2 = 0.3

# Find alpha-cuts for different alpha values
alpha_cut1 = alpha_cut(fuzzy_set, alpha1)
alpha_cut2 = alpha_cut(fuzzy_set, alpha2)

# Display the results
print(f"Alpha-cut for alpha = {alpha1}: {alpha_cut1}")
print(f"Alpha-cut for alpha = {alpha2}: {alpha_cut2}")
