import numpy as np
import pandas as pd
import psycopg2
from collections import Counter

# Define the colors for each day of the week
monday_colors = ['green', 'yellow', 'green', 'brown', 'blue', 'pink', 'blue', 'yellow', 'orange', 'cream', 'orange', 'red', 'white', 'blue', 'white', 'blue', 'blue', 'blue', 'green']
tuesday_colors = ['arsh', 'brown', 'green', 'brown', 'blue', 'blue', 'blew', 'pink', 'pink', 'orange', 'orange', 'red', 'white', 'blue', 'white', 'white', 'blue', 'blue', 'blue']
wednesday_colors = ['green', 'yellow', 'green', 'brown', 'blue', 'pink', 'red', 'yellow', 'orange', 'red', 'orange', 'red', 'blue', 'blue', 'white', 'blue', 'blue', 'white', 'white']
thursday_colors = ['blue', 'blue', 'green', 'white', 'blue', 'brown', 'pink', 'yellow', 'orange', 'cream', 'orange', 'red', 'white', 'blue', 'white', 'blue', 'blue', 'blue', 'green']
friday_colors = ['green', 'white', 'green', 'brown', 'blue', 'blue', 'black', 'white', 'orange', 'red', 'red', 'red', 'white', 'blue', 'white', 'blue', 'blue', 'blue', 'white']

# Combine the colors for all days of the week
all_colors = monday_colors + tuesday_colors + wednesday_colors + thursday_colors + friday_colors

# Calculate the mean color
mean_color = np.mean(all_colors)

# Calculate the mode color
mode_color = Counter(all_colors).most_common(1)[0][0]

# Calculate the median color
median_color = np.median(all_colors)

# Calculate the variance of the colors
variance = np.var(all_colors)

# Calculate the frequency of each color
color_counts = Counter(all_colors)

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="Interviewdb",
    user="Bincom",
    password="mypassword123"
)

# Create a table to store the colors and their frequencies
cur = conn.cursor()
cur.execute("CREATE TABLE colors (color VARCHAR(255), frequency INTEGER)")

# Insert the colors and their frequencies into the table
for color, count in color_counts.items():
    cur.execute("INSERT INTO colors (color, frequency) VALUES (%s, %s)", (color, count))

# Commit the changes and close the connection
conn.commit()
cur.close()
conn.close()

# Define a recursive function to search for a number in a list
def search_number(number, numbers):
    if not numbers:
        return False
    elif numbers[0] == number:
        return True
    else:
        return search_number(number, numbers[1:])

# Generate a random 4-digit number of 0s and 1s and convert it to base 10
binary_number = ''.join(str(np.random.randint(0, 2)) for _ in range(4))
decimal_number = int(binary_number, 2)

# Calculate the sum of the first 50 Fibonacci sequence
fibonacci_sequence = [0, 1]
for i in range(2, 51):
    fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])
fibonacci_sum = sum(fibonacci_sequence)

# Print the results
print("Mean color:", mean_color)
print("Mode color:", mode_color)
print("Median color:", median_color)
print("Variance of colors:", variance)
print("Probability of choosing red color:", color_counts['red'] / len(all_colors))
print("Recursive search for number 5:", search_number(5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print("Random binary number:", binary_number)
print("Random decimal number:", decimal_number)
print("Sum of first 50 Fibonacci sequence:", fibonacci_sum)
