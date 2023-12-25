# Q.Write a Python program to Cloning or Copying a list.


# 1. Using the Slice Operator
original_list = [1, 2, 3, 4, 5]
cloned_list = original_list[:]
print(cloned_list)

print('\n')

# 2. Using the list() constructor
original_list = [1, 2, 3, 4, 5]
cloned_list = list(original_list)
print(cloned_list)

print('\n')

# 3. Using List Comprehension
original_list = [1, 2, 3, 4, 5]
cloned_list = [item for item in original_list]
print(cloned_list)
