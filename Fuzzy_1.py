# Define fuzzy set operations without using numpy
def union(set1, set2):
    return [max(a, b) for a, b in zip(set1, set2)]

def intersection(set1, set2):
    return [min(a, b) for a, b in zip(set1, set2)]

def complement(fuzzy_set):
    return [1 - a for a in fuzzy_set]

def difference(set1, set2):
    return [max(a - b, 0) for a, b in zip(set1, set2)]

# Verify De Morgan's Law for fuzzy sets A and B
def de_morgan_law(set1, set2):
    lhs1 = complement(intersection(set1, set2))
    rhs1 = union(complement(set1), complement(set2))
    lhs2 = complement(union(set1, set2))
    rhs2 = intersection(complement(set1), complement(set2))
    
    is_valid = (lhs1 == rhs1) and (lhs2 == rhs2)
    return is_valid, lhs1, rhs1, lhs2, rhs2

# Create a fuzzy relation by Cartesian product
def fuzzy_relation(set1, set2):
    return [[min(a, b) for b in set2] for a in set1]

# Perform max-min composition on two fuzzy relations R1 and R2
def max_min_composition(R1, R2):
    result = []
    for i in range(len(R1)):
        row = []
        for j in range(len(R2[0])):
            max_min_val = max([min(R1[i][k], R2[k][j]) for k in range(len(R2))])
            row.append(max_min_val)
        result.append(row)
    return result

# Example fuzzy sets
A = [0.2, 0.5, 0.7, 1.0]
B = [0.4, 0.6, 0.8, 0.9]

# Operations
print("Union of A and B:", union(A, B))
print("Intersection of A and B:", intersection(A, B))
print("Complement of A:", complement(A))
print("Difference (A - B):", difference(A, B))

# Verify De Morgan's Law
de_morgan_valid, lhs1, rhs1, lhs2, rhs2 = de_morgan_law(A, B)
print("De Morgan's Law is", "valid" if de_morgan_valid else "not valid")
print("Complement of Intersection (A ∩ B):", lhs1)
print("Union of Complements (A' ∪ B'):", rhs1)
print("Complement of Union (A ∪ B):", lhs2)
print("Intersection of Complements (A' ∩ B'):", rhs2)

# Create fuzzy relation by Cartesian product
R1 = fuzzy_relation(A, B)
R2 = fuzzy_relation(B, A)
print("Fuzzy relation R1 (A x B):\n", R1)
print("Fuzzy relation R2 (B x A):\n", R2)

# Perform max-min composition
composition_result = max_min_composition(R1, R2)
print("Max-Min Composition of R1 and R2:\n", composition_result)
