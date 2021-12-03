# Dictionary, Set, Tuple
# Given the following three scenarios, choose the best data structure (between a dictionary, set, or tuple) to efficiently store the data.
# Each scenario ties directly to one data structure. Each data structure will be used only once.
# You will need to determine which data structure is best for which scenario, and then implement the data structure in Python.
#a. Store the months of the year. Determine the month in the data structure which Pi Day exists and print that month to the console.
#b. Store five fruits or vegetables.
    #i. Add two of your favorite fruits and two of your favorite vegetables to the collection.
    #ii. Iterate over the collection and print each one to the console.
#c. Store information about a user profile. Use literal string interpolation to print the user’s profile information to the console. The profile should consist of the following information:
    #i. First Name
    #ii. Last Name
    #iii. Email Address
    #iv. Phone Number
#d. Use a list to store the dictionary of your immediate family members, with each index of the list storing its own dictionary. Dictionary should contain the following keys:
    #a. First name
    #b. Last name
    #c. Relation to you

#&Tuple
months_of_year = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
print(f'\nPi Day: {months_of_year[2]} 14\n')

#&Set
fruits_and_veggies = {'Apple', 'Pear', 'Strawberry', 'Kiwi', 'Banana', 'Tomato', 'Carrot', 'Cucumber', 'Lettuce', 'Broccoli'}

fruits_and_veggies.add('Blueberry')
fruits_and_veggies.add('Raspberry')
fruits_and_veggies.add('Zucchini')
fruits_and_veggies.add('Eggplant')

for item in fruits_and_veggies:
    print(item)

#&Dictionary
user = {
    'firstName': 'Audrey',
    'lastName': 'Schmidt',
    'emailAddress': 'audsch05@gmail.com',
    'phoneNumber': '414-588-9313'
}

print ('\nUsername: ', user['firstName'], user['lastName'], '\nEmail Address: ', user['emailAddress'], '\nPhone Number: ', user['phoneNumber'], '\n')

#&List and Dictionary
family_members = [
    {'firstName': 'Andrew', 'lastName': 'Schmidt', 'relation': 'Father'},
    {'firstName': 'Maureen', 'lastName': 'Kusz-Schmidt', 'relation': 'Mother'},
    {'firstName': 'Anna', 'lastName': 'Schmidt', 'relation': 'Sister'},
    {'firstName': 'Josephine', 'lastName': 'Schmidt', 'relation': 'Sister'}
                  ]

for index in range(len(family_members)):
    print('Family Member:')
    for key in family_members[index]:
        print(f'{key}: {family_members[index][key]}')
    print('\n')