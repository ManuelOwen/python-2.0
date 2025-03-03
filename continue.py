# Example: Using the continue statement in a for loop

# Loop through numbers from 1 to 10
for num in range(1, 11):
    # If the number is divisible by 2, skip the rest of the loop and move to the next iteration
    if num % 2 == 0:
        continue
    # Print the number if it's not divisible by 2
    print("Odd number:", num)

print("Loop ended.")
