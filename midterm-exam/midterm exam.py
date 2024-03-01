#1
a = 10

a = a + 2

print(a*2)

a = 19

print(a+3)

a = a // 2

print((3+10**2/2) or 70.0)
----- #2
import datetime

a = 3
b = 4
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year
------ #3
print(a)
print(b)
c = a + b
print(c)
d = "abc" * (c // 3)
print(d)
------#4

def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
#Example usage
print(palindrome("racecar"))
-------#5
def count_un_an_patterns(text):
    # Define the start and end of the pattern
    pattern_start = "un"
    pattern_end = "an"
    count = 0

    # Split the text into words
    words = text.split()

    # Loop through each word in the text
    for word in words:
        # Check if the word starts with 'un' and ends with 'an'
        if word.startswith(pattern_start) and word.endswith(pattern_end):
            count += 1

    return count
# Example text
text = "The unusual man had an unclean plan in the urban area."
print(count_un_an_patterns(text))
-----#6
my_list = [1, 2, 3]
print(my_list) # Output: [1, 2, 3]
# Modify the list
my_list.append(4) # Add an item
print(my_list.append) # Output: [0, 2, 3, 4]

my_string = "hello"
print(my_string)  # Output: "hello"

# Attempt to modify the string
my_string = my_string + " world"  # Concatenation creates a new string
print(my_string)  # Output: "hello world"

------#7
import random
# Initialize list
random_numbers = [1,2,98,56,48,28]
# Generate and append 10 random numbers between 1 and 100
for i in range(10):
    random_numbers.append(random.randint(1, 100))
# Create a new list based on the condition.
modified_numbers = [] #Modified Numbers includes XX for numbers less than 50
for number in random_numbers:
    if number > 50:
        continue  # Skip numbers greater than 50
    else:
        modified_numbers.append("XX")  # Replace numbers 50 or less with "XX"

# Print the modified list
print(modified_numbers)
http_scheme = "http://"  # Identifies valid URLs
https_scheme = "https://"

-------#8
def is_valid_url(url):  # creates funtion
    # Initially assume both http and https are not matched
    scheme_matched = False
    dot_found = False

    # Manually check for http:// or https:// prefix using slicing
    if url[:7] == http_scheme or url[
                                 :8] == https_scheme:  # includes to an approximate character index of 7 to 8 characters, giving enough space to identify proper URL syntax.
        scheme_matched = True

    # If scheme matched, look for a dot in the remainder of the URL
    if scheme_matched:
        for i in range(scheme_length, len(url)):  # Start checking after the scheme
            if url[i] == '.':
                dot_found = True
                break  # Exit loop once a dot is found

    return scheme_matched and dot_found


# Example usage:
print(is_valid_url("http://www.example.com"))  # Expected to return True
print(is_valid_url("www.example.com"))  # Expected to return False

-----#9
def days_since_birthday(birthday):
    # Split the birthday string into day, month, and year
    day, month, year = birthday.split("-")

    # Convert the year to an integer
    birth_year = int(year)

    # Get the current year
    # Since we're not using any imports or external functions to get the current date,
    # let's assume we're calculating for the year 2023 for demonstration purposes.
    current_year = 2024

    # Calculate the number of full years since the birthday
    full_years = current_year - birth_year - 1  # Exclude the birth year and the current year

    # Calculate the number of days (assuming 365 days per year for simplicity)
    days = full_years * 365

    return days


# Example usage
print(days_since_birthday("01-01-2000"))