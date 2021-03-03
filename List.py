
# List

Scores = [70,85,67.5,90,80] # Creatin List
# e.g 1) Printing list
print(Scores)
# # o/p
# # [70, 85, 67.5, 90, 80]
#
# # e.g 2) Accessing elements of list
# print(Scores[1])
# # o/p
# # 85
#
# # e.g 3) To access last element of list
# print(Scores[-1])
# # o/p
# # 80
#
# # e.g 4) To Access multiple elements of list using list index ( In specific range)
# print(Scores[1:4])
# # o/p
# # [85,67.5,90]
#
# # e.g 5) To Access whole list untill last element of list without knowing last index
# print(Scores[1:]) # After start index use only colon
# # o/p
# # [85,67.5,90,80]
#
# # e.g 6) To Assign new value to the element of list
# Scores[0] = 75 # To Assign new value use index no of list
# print(Scores)
# # o/p
# # [70, 85, 67.5, 90, 80] - before
# # [75, 85, 67.5, 90, 80] - after
#
# # e.g
# Scores[0] = ["Hello","World"]
# print(Scores)
# # o/p
# # [['Hello', 'World'], 85, 67.5, 90, 80]
#
# print(Scores[0][1]) # To Access elements of list under list
# o/p
# World

# e.g 7) To remove elements from list (replace them elements with empty list
# Scores[1:4] = []
# print(Scores)
# # o/p
# # [75, 85, 67.5, 90, 80] - before
# # [75,80] - after
#
# # e.g
# Scores[0] = []
# print(Scores)
# # o/p
# [[], 80]

# e.g 8) To append last element in list
Scores.append(85)
print(Scores)
# o/p
# [70, 85, 67.5, 90, 80] - Before
# [70, 85, 67.5, 90, 80, 85] - After
