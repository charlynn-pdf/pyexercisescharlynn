"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the user's answer to "Do you want to continue? (yes/no)", typed at each attempt.
# 2. Process:a while loop asks the question again and again. Each answer is cleaned
#    with .strip().lower(), so "Yes", "yes" and " yes " all count as the same answer.
# 3. Out: a message saying the user chose to continue or not to continue,
#    then a summary of the loop.
# 4. My stop condition, my attempt limit, my summary:
#    - Stop condition: the user types "yes" or "no" (capitals and extra spaces accepted).
#    - Attempt limit: 5 attempts. 
#    - Summary: number of attempts used, and whether the user chose to continue or not


# Your code below

i = 0
while i < 5:
    print("Attempt number:", i + 1)
    i = i + 1


while True :
    answer = input("Do you want to continue? (yes/no): ")
    if answer.strip().lower() == "yes":
        print("You chose to continue.")
        break
    elif answer.strip().lower() == "no":
        print("You chose not to continue.")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")