### LISTS IN PYTHON

# A BUILT-IN DATATYPE THAT STORES SET OF VALUES
# IT CAN STORE THE ELEMENTS OF DIFFERENT TYPES ( INT, FLOAT, STRING, ETC...)

#================================================#
# marks = [1, True, False, 2, 5, 9, 3, 8, 2, 2]
# marks[0] = marks[1] and marks[2]
# print(marks[0])  # OUTPUT = 10
#================================================#


#================================================#
# List Slicing

# Similar to String Slicing
# list_name[starting_idx : ending_idx] >>> {{#ending idx is not included}}
# marks = [87, 64, 33, 95, 76]
# marks[1:4] is [64, 33, 95]
# marks[ :4] is same as marks[0:4]
# marks[1: ] is same as marks[ 1 : len(marks) ]
# marks[-3:-1] is [33, 95]
#================================================#


#================================================#
# marks = [87, 64, 33, 95, 76]
# print(marks[:])  # OUTPUT = [87, 64, 33, 95, 76]
#================================================#



#================================================#

# List Methods

# Ex: list = [2, 1, 3]
# list.append(4) #adds one element at the end [2, 1, 3, 4]
# list.sort() #sorts in ascending order [1, 2, 3]
# list.sort(reverse=True) #sorts in descending order [3, 2, 1]
# list.reverse() #reverses list [3, 1, 2]
# list.insert(idx, el) #insert element at index
#Ex: ↓↓
# list = [1,3,5]

# list.append(4)
# print(list) # OUTPUT = [1, 3, 5, 4]

# list.sort()
# print(list) # OUTPUT = [1, 3, 4, 5]

# list.sort(reverse=True)
# print(list) # OUTPUT = [5, 4, 3, 1]

# list.reverse()
# print(list) # OUTPUT = [1, 3, 4, 5]

# list.insert(2, "Hello")
# print(list) # OUTPUT = [1, 3, 'Hello', 4, 5]

#================================================#
