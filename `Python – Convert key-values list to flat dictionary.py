# Python3 code to demonstrate working of
# Convert key-values list to flat dictionary
# Using dict() + zip()
from itertools import product

# initializing dictionary
test_dict = {'month' : [1, 2, 3],
			'name' : ['Jan', 'Feb', 'March']}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Convert key-values list to flat dictionary
# Using dict() + zip()
res = dict(zip(test_dict['month'], test_dict['name']))

# printing result
print("Flattened dictionary : " + str(res))
