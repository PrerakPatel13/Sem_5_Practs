# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
set_union = set1.union(set2)
print(f"Set Union: {set_union}")

# Intersection
set_intersection = set1.intersection(set2)
print(f"Set Intersection: {set_intersection}")

# Difference
set_difference = set1.difference(set2)
print(f"Set Difference: {set_difference}")

# Tuple operations
tuple1 = (1, 2, 3, 4)
tuple2 = (3, 4, 5, 6)

# Union
tuple_union = set(tuple1 + tuple2)
print(f"Tuple Union: {tuple_union}")

# Intersection (Note: Intersection doesn't directly apply to tuples, so we'll use a set)
tuple_intersection = set(tuple1).intersection(set(tuple2))
print(f"Tuple Intersection: {tuple_intersection}")

# Difference (Note: Difference doesn't directly apply to tuples, so we'll use a set)
tuple_difference = set(tuple1).difference(set(tuple2))
print(f"Tuple Difference: {tuple_difference}")

# List operations
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

# Union
list_union = set(list1 + list2)
print(f"List Union: {list_union}")

# Intersection (Note: Intersection doesn't directly apply to lists, so we'll use a set)
list_intersection = set(list1).intersection(set(list2))
print(f"List Intersection: {list_intersection}")

# Difference (Note: Difference doesn't directly apply to lists, so we'll use a set)
list_difference = set(list1).difference(set(list2))
print(f"List Difference: {list_difference}")

# Dictionary operations
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'c': 3, 'd': 4, 'e': 5}

# Union
dict_union = {**dict1, **dict2}
print(f"Dictionary Union: {dict_union}")

# Intersection (Note: Intersection doesn't directly apply to dictionaries, so we'll use a set)
dict_intersection = set(dict1.keys()).intersection(set(dict2.keys()))
print(f"Dictionary Intersection: {dict_intersection}")

# Difference (Note: Difference doesn't directly apply to dictionaries, so we'll use a set)
dict_difference = set(dict1.keys()).difference(set(dict2.keys()))
print(f"Dictionary Difference: {dict_difference}")
