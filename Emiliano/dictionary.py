# What is a disctionary 
# dictionaries are defined by using curly braces, dictionaries can take any data type
# Keys = the naming aspect and the value. CAnnot have duplicate key names
# When would you use a list vs a dictionary. 
# When there are a lot of specific data in one place. 
color_dict = {'color': 'red', 'another':'orange'}
               #key    #value  #reassinment #value
print(color_dict['color'])

user_account = {'username': 'Deshwan', 'balance': 100}

user_account['balance'] = 200
print(user_account['balance'])
user_account.pop('balance')
print(user_account)
