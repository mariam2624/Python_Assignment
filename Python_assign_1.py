"""

1. Write a Python program to print the following string in a specific format (see the output).
Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are
2. Write a Python program to get the Python version you are using
3. Write a Python program to display the current date and time.
4. Write a Python program which accepts the radius of a circle from the user and compute the area.
5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
6. Write a python program which takes two inputs from user and print them addition
"""


print("Twinkle, twinkle, little star,\n\t How I wonder what you are!\n\t\t Up above the world so high,\n\t\t Like a diamond in the sky.\nTwinkle, twinkle, little star,\n \t How I wonder what you are ")
      
import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)


import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))



radius = int(input("Enter radius: "))
A = 2 * 3.14 * radius
print(f"The area is {A}")



f_name = input("Enter first name: ")
l_name = input("Enter last name: ")
print(f"{l_name}  {f_name}")


ip_1 = int(input("Enter first input: "))
ip_2 = int(input("Enter second input: "))
op = ip_1 + ip_2
print(op)
