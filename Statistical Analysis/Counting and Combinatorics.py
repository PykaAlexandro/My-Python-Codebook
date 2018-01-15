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