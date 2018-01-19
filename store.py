# ## Store Manager

# ### Instructions

# modules

import os 
import csv

# file path 

file_path = os.path.join('resources','store_items.csv')

# open 
with open(file_path, newline='') as csvfile:

    # read

    csv_reader = csv.reader(csvfile, delimiter = ',')

    my_dictionary = {}

    for row in csv_reader:
        my_dictionary[row[0]] = row[1]

# disply it in a dictionary 
# print(my_dictionary)
# * Create a dictionary that has a few items already stored.

# * Prompt the user is they would like to add a new item, remove an existing one, or to display all the items currently in stock.
# add new items

# * If the user would like to add a new item, ask what they would like to add and how many. Add the results to your dictionary.

move_on = 'y'

while move_on == 'y':

    ask_this = input('What would you like to do? (A)dd or (R)emove an item or (S)tore inventory ')

    if ask_this == 'A':

        input_key = input('What is the new sport ')
        input_value = input('What is the value of the sport ')

        my_dictionary[input_key] = input_value

        print(my_dictionary)

    elif ask_this == 'R':

        delete_item = input(f'What would you like to delete from {my_dictionary} ')

        if delete_item in my_dictionary:
         
            del my_dictionary[delete_item]
            print(my_dictionary)
        else:
            print('The {ask_this} is not in the list ')

    elif ask_this == 'S':

        print('Store inventory ')
        print('..........................')

        for key, value in my_dictionary.items():
            print(key, value)

        print('..........................')

    else:
        print('Sorry, the action is not available ')

    move_on = input('Would you like to add more items? (y)es or (n)o ')


# delete an item


# * If the user wants to remove and item, first check if that item is available then remove that item from the dictionary.

# * If the user want to display the result print out an easy to read list of all the items and amount to the console.


