"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the original list of 10 numbers from exercise 4.0
# 2. Process: The program creates four different orders of the list
# 3. Out: the program displays the four reordered lists and the original list at the end. 
# 4. My four orders, and which ones modify the original: I chose the ascending, descending, reversed and original order. 
# sorted() and reversed() create new lists.
# None of these operations modify the original list.


# Your code below

numbers = [4,5,6,7,8,9,10,11,2,1]

print("Ascending:",sorted(numbers))
print("Descending:", sorted(numbers, reverse=True))
print("Reserved:", list(reversed(numbers)))
print ("Original order:", numbers)

print("Original list at the end:",numbers)
