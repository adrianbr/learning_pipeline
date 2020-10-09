"""
the basic python data structures:
tuple (1,2)

a tuple cannot be modified (immutable) so it is typically encountered when reading or writing without transform

list [1,2]
this is the most commonly used - it can be modified.

dictionary {'number1': 1, 'other number': 2}
it's like a json and allows you to retrieve a value by the key name

below are some nested examples that represent tables
"""

#the last value is not missing - it's totally valid tuple syntax
table_tuple = ((1, 2),
               (2,))

#variable names are created on the fly

#iterating:
for row in table_tuple:
    print(row)
    for value in row:
        print(value)

#accessing
table_tuple[0]

table_list = [[1,2],
              [1]]

#lists are the same but additionally
table_list[0][0] == 5 #this will set the first element of the first row to 5

#list comprehension
#another way to iterate over lists and generate new lists - here we grab the first column (so the values '1')
first_col_list = [row[0] for row in table_list]
print('first_col_list', first_col_list)

