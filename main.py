# Start with a string of names separated by commas and spaces
names_string = "John, Jane, Bob, Molly, Chris, Angela, Tom"

# Split the string into a list where each name is an individual element
names = names_string.split(", ")

# Import the 'random' library which contains functions for generating random numbers
import random

# Calculate the number of items (or names) in the 'names' list
num_items = len(names)

# Generate a random number between 0 and one less than the number of items in the list
# This corresponds to the indices of the list of names
random_choice = random.randint(0, num_items - 1)

# Select the name at the index of the random number chosen
person_who_will_pay = names[random_choice]

# Print the name of the person along with a message indicating they will pay for the meal
print(person_who_will_pay + " is going to buy the meal today!") 
