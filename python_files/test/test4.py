# import json

# with open('car_data.json', 'w') as fp:
    
#     fp.write('super')




# my_details = {  
#     'name': 'John Doe',
#     'age': 29
# }

# with open('personal.json', 'x') as json_file:  
#     json.dump(my_details, json_file)


def roundup(x):
    return x if x % 100 == 0 else x + 100 - x % 100


print (roundup(17361))