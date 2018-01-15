# A set of numbers, sets in Python have no duplicates and are not in order
X = set([1,2,30])
S = {1, 2, 30}
print(X)
print(S)
print(len(X))

# Create an empty set
A = set()
B = set({})
type(A), type(B)
print(A), print(B)
print(len(A) == 0)
not A, not S

# Add elements to an empty set
A = set()
A.update({0, 10})
print(A)

# Delete an element from a set
A = {1, 2, 3}
A.remove(2)       # Works only if the element to be deleted is present in the set
A.discard(4)      # Works even if the element to be deleted is not present in the set
A.discard(3)      
print(A)

# Remove a random element from a set
A = {1, 2, 3}
A.pop()
print(A)

# Get a sorted list from a set
A = {1, 10, 4, -9, 7, 8, -6, 3, 2}
print(sorted(A))

# Elements can be tuples
set([(1,2),(1,3),(3,1)])

# But cannot be lists
set([[1,2],[1,3],[3,1]])

# Operations on sets
A=set(range(0,3)) # all integers between 0 and 2
B=set(range(0,6,2)) # even integers between 0 and 2
C=set(range(0,6))   # all integers between 0 and 5
'A=',A,'B=',B,'C=',C

# Checking if an element is in a set:
1 in A, 1 in B, 3 not in B

# Checking if a set is a subset/superset of another set
A.issubset(C), A<=C
C.issuperset(B),C>=B

# Union and intersection of sets
A.union(B),A | B
A.intersection(B), A&B

# The difference between A and B contains all elements that are in A but not in B
A.difference(B), A-B

# The symetric difference contains all elements that are in one of the two sets, but not in both
A.symmetric_difference(B), A^B

# Computing the cartesian products
A=set(['a','b','c'])
B=set([1,2])
C=set()
for x in A:
    for y in B:
        C.add((x,y))
C

# Homework Problem 1
A = {1, 2, 3}
B = {3, -6, 2, 0}
U = {-10, -9, -8, -7, -6, 0, 1, 2, 3, 4}

# Exercise 1: Write the function complement_of_union that first determines A∪B and then evaluates the complement of this set. Output the tuple:  (A∪B,(A∪B)c)
def complement_of_union(A, B, U):
    x = A | B
    y = U - x
    return x, y

# Exercise 2: Write the function intersection_of_complements that first determines Ac and Bc and then evaluates the intersection of their complements. Output the tuple:  (Ac,Ac∩Bc)
def intersection_of_complements(A, B, U):
    x = U - A
    z = U - B
    y = x & z
    return x, y

# Homework Problem 2:
A = {1, 2}
B = {1, 3}
S = {-1, 0}
T = {0, 10}

# Exercise 1: Write function product_of_unions that first determines (A∪B) and (S∪T) and then evaluates the cartesian products of these unions. Output the tuple  ((A∪B),(A∪B)×(S∪T)) 
def product_of_unions(A, B, S, T):
    x = A | B
    y = S | T
    z = set()
    for a in x:
        for b in y:
            z.add((a,b))
    return x, z

# Exercise 2: Write a function union_of_products that first determines (A×S) and the other three cartesian products that appear on the right hand side of the identity above, then evaluates the union of these cartesian products. Output the tuple  ((A×S),(A×S)∪(A×T)∪(B×S)∪(B×T))
def union_of_products(A, B, S, T):
    a = set()
    for i in A:
        for j in S:
            a.add((i, j))
    b = set()
    for i in A:
        for j in T:
            b.add((i, j))
    c = set()
    for i in B:
        for j in S:
            c.add((i, j))
    d = set()
    for i in B:
        for j in T:
            d.add((i, j))
    z = a | b | c | d
    return a, z
