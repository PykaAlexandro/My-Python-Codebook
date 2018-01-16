# Size of a set
NewSet = {1, 2}
print(len(NewSet))

# Smallest element in a set
NewSet = {2, 1, 3}
print(min(NewSet))

# Largest element in a set
NewSet = {-9, -1, -7}
print(max(NewSet))

# Print the sum of elements of a set
A = {1, 5, 2, -10, 19}
print(sum(A))

# Verify the above using a 'for' loop
total=0
for i in A:
    total += i
print(total)

A = {3, 4, 5}
B = {6, 7, 8}
print(len(A),len(B))

# Disjoint Unions
C = A | B
print(C, "\n", len(C))

A = {1, 2, 3}
B = {1, 3, 5}
print(len(A),len(B))

# Unions
C = A | B
print(C, "\n", len(C), "\n", len(A) + len(B) - len(C))

# Intersections
C = A & B
print(C, "\n", len(C))

# Differences
E = A-B
print(E, "\n", len(E))

# Cartesian Products
import itertools
A = {1, 2, 3}
B = {4, 5}
cartesian_product = set([i for i in itertools.product(A, B)])
print("Ordered pairs in %s x %s:  " %(A,B))
for i in cartesian_product:
    print(i)
print;print("Size = %i" %len(cartesian_product))

# |A X B| directly
print(len(cartesian_product))

# |A X B| using product rule
print(len(A)*len(B))

# Cartesian Powers
A = {1, 2, 3}
k = 2

# Prints k'th cartesian power of A
print(set(itertools.product(A, repeat = k)))

# Finds |A|^k
print(len(A)**k)

# Homework Problem 1
A = {1, 2, 3}
B = {3, -6, 2, 0}

# Exercise 1: Write a function union that determines first A∪B and then evaluates the union's size. Output the ordered pair (A∪B,|A∪B|)
def union(A, B):
    x = A | B
    return x, len(x)

#Exercise 2: Write a function inclusion_exclusion that first deterimines |A|, |B|, A∩B, and |A∩B|, and then uses the inclusion-exclusion formula to determine |A∪B|. Output the tuple (|A|,|B|,|A∩B|,|A∪B|)
def inclusion_exclusion(A, B):
    return len(A), len(B), len(A & B), len(A | B)

# Homework Problem 2:
A = {1, 2, 3, 4, 5}
B = {0, 2, -6, 5, 8, 9}
C = {2, 10}

#Exercise 1: Write a function union3 that first determines A∪B∪C and then evaluates the size of this union. Output the tuple (A∪B∪C,|A∪B∪C|).
def union3(A, B, C):
    return A | B | C, len(A | B | C)

#Exercise 2: Write a function inclusion_exclusion3 that first deterimines the sizes of  A, B, C and their mutual intersections, and then uses the inclusion-exclusion principle to determine the size of the union. Output the tuple (|A∩B∩C|,|A∪B∪C|)
def inclusion_exclusion3(A, B, C):
    return len(A & B & C), len(A | B | C)