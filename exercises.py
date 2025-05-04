# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
# print_greeting()

# ------------------------------------------------------------------------------------------------------------------------

# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

#define the function
def check_letter():
    # Prompt the user to enter a letter
    letter = input("Enter a letter (a-z or A-Z): ")

    # Check if the input is a single alphabetical character
    # .isalpha() method checks if the string contains only letters
    # len() function checks the length of the string
    if len(letter) == 1 and letter.isalpha():
        # Convert the letter to a lowercase letter to make comparison easier
        # .lower() method converts the letter to lowercase
        lower_letter = letter.lower()

        # Check if the letter is a vowel
        if lower_letter in 'aeiou':
            print(f"The letter {letter} is a vowel.")
        else:
            print(f"The letter {letter} is a consonant.")
    else:
        # Handle invalid input for non-alphabetical characters or multiple characters like symbols and numbers
        print("Invalid input. Please enter a single alphabetical character.")


# Call the function
# check_letter()

# ------------------------------------------------------------------------------------------------------------------------

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    # Set the minimum voting age
    voting_age = 18

    # Prompt the user to enter their age
    # input() function captures user input as a string
    age_input = input("Please enter your age: ")

    # Convert the input to an integer and handle any conversion errors if the input is not a valid number
    # This is done by using try-except block to catch ValueError
    try:
        age = int(age_input)
        # We use int() to convert the input string to an integer
        # If the conversion is successful, we can proceed to check the age

        # Check if the age is a valid positive number (no negative numbers)
        # This is done by checking if age is less than 0
        # If age is less than 0, print an error message
        if age < 0:
            print("Invalid input. Age cannot be negative.")
        elif age >= voting_age:
            # If age is greater than or equal to voting age, print eligible message
            print("You are eligible to vote.")
        else:
            # If age is less than voting age, print not eligible message
            print("You are not eligible to vote yet.")
        
    except ValueError:
        # Handle the case where the input cannot be converted to an integer
        print("Invalid input. Please enter a valid number for your age.")
        

# Call the function
# check_voting_eligibility()

# ------------------------------------------------------------------------------------------------------------------------

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    # Prompt the user to enter a dog's age
    age_input = input("Input a dog's age: ")

    # Convert the input to an integer and handle any conversion errors
    try:
        dog_age = int(age_input)

        # Check if the age is a valid positive number (no negative numbers)
        if dog_age < 0:
            print("Invalid input. Age cannot be negative.")
        elif dog_age == 0:
            print("A dog that is 0 years old is a newbord!")
        elif dog_age == 1:
            print("The dog's age in dog years is 10.")
        elif dog_age == 2:
            print("The dog's age in dog years is 20.")
        else:
            # First 2 years = 10 dog years each (20 dog years), rest of the years = 7 dog years each
            dog_years = 20 + (dog_age - 2) * 7
            print(f"The dog's age in dog years is {dog_years}.")

    except ValueError:
        # Handle the case where the input cannot be converted to an integer
        print("Invalid input. Please enter a valid number for the dog's age.")

# Call the function
# calculate_dog_years()

# ------------------------------------------------------------------------------------------------------------------------

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    # Prompt the user to answer if it is cold (yes/no)
    # input() function shows a message and captures user input as a string
    # .strip() method removes extra spaces at the beginning and end of the input
    # .lower() method converts the input to lowercase for easier comparison
    cold = input("Is it cold? (yes/no): ").strip().lower()

    # Prompt the user to answer if it is raining (yes/no)
    raining = input("Is it raining? (yes/no): ").strip().lower()

    # Validate the input to ensure it is either 'yes' or 'no'
    valid_answers = ["yes", "no"]

    # If they are not valid answers, print an error message and exit the function
    if cold not in valid_answers or raining not in valid_answers:
        print("Invalid input. Please answer with 'yes' or 'no'.")
        return
    
    # Determine clothing advice based on the conditions
    # Use logical operators to check the conditions
    if cold == "yes" and raining == "yes":
        print("Wear a waterproof coat.")
    elif cold == "yes" and raining == "no":
        print("Wear a warm coat.")
    elif cold == "no" and raining == "yes":
        print("Carry an umbrella.")
    else: # cold == "no" and raining == "no"
        print("Wear light clothing.")

# Call the function
# weather_advice()

# ------------------------------------------------------------------------------------------------------------------------

# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    # List of valid 3-letter month abbreviations
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    # Prompt the user to enter the month
    # .strip() method removes extra spaces at the beginning and end of the input
    # .capitalize() method converts the first character to uppercase and the rest to lowercase to ensure consistent casing format
    month = input("Enter the month of the year (Jan - Dec): ").strip().capitalize()

    # Check if the month is valid
    # We check if the month is in the list of valid months
    # If the month is not in the list, print an error message and exit the function
    # return statement is used to exit the function
    if month not in months:
        print("Invalid month. Please enter a valid month abbreviation (Jan - Dec).")
        return
    
    # Prompt the user to enter the day
    day_input = input("Enter the day of the month: ").strip()

    # Try converting day to an integer
    try:
        day = int(day_input)
        if day < 1 or day > 31:
            print("Invalid day. Please enter a valid day of the month (1-31).")
            return
    
    except ValueError:
        print("Invalid input. Please enter a valid number for the day.")
        return
    
    # Determine the season based on the month and day
    if (month == "Dec" and day >=21) or month in ["Jan", "Feb"] or (month == "Mar" and day <= 19):
        season = "Winter"
    elif (month == "Mar" and day >= 20) or month in ["Apr", "May"] or (month == "Jun" and day <= 20):
        season = "Spring"
    elif (month == "Jun" and day >= 21) or month in ["Jul", "Aug"] or (month == "Sep" and day <= 21):
        season = "Summer"
    else:
        season = "Fall"

    # Print the result
    # Use f-string to include values dynamically in the output string
    print(f"{month} {day} is in {season}.")

# Call the function
# determine_season()

# ------------------------------------------------------------------------------------------------------------------------

# Exercise 6: Number Guessing Game
#
# Write a Python function named `guess_number` that allows a user to guess a predetermined number within a range.
#
# Requirements:
# - Set a fixed number as the target for guessing (e.g., 42).
# - Prompt the user to guess a number within a range (e.g., 1 to 100).
# - Allow the user to guess up to five times.
# - After each guess, use conditional statements with AND, OR, and NOT to give the user hints like:
#   - "Guess is too low" or "Guess is too high."
#   - "Last chance!" when they are on their fifth guess.
# - Print "Congratulations, you guessed correctly!" if they guess the number.
# - Print "Sorry, you failed to guess the number in five attempts." if they do not succeed.
#
# Hints:
# - Use a for loop with a range to limit guesses to five.
# - Use logical AND, OR, and NOT to check conditions and provide appropriate feedback.

def guess_number():
    # Set up a fixed number as the target for guessing
    target = 42

    print("I'm thinking of a number between 1 and 100. You have 5 attempts to guess it!")

    # Allow the user to guess up to five times
    for attempt in range(1,6): # range(1,6) generates numbers from 1 to 5 so it gives us 5 attempts
        guess_input = input(f"Attempt {attempt}: Enter your guess: ")

        try:
            guess = int(guess_input)

            if guess == target:
                print("Congratulations, you guessed correctly!")
                break

            elif guess < target:
                print ("Guess is too low.")
            elif guess > target:
                print ("Guess is too high.")

            # Print a message for the last chance
            if attempt == 5 and guess != target:
                print("Last chance. Game over!")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # If the user fails to guess the number in five attempts
    if guess != target:
        print("Sorry, you failed to guess the number in five attempts.The number was {target}.")
        
# Call the function
# guess_number()

# ------------------------------------------------------------------------------------------------------------------------









