"""
Program to take input as Friend's name  and if the
name is 'Sheela' , then print 'She is my best friend.'
If the name is Rina, then print, I know her and if
any other name is found, print I don't know her/him '
"""


username = input("Enter friend's name: ")

if username == "Sheela":
    print("She is my best friend!")
    
elif username =="Rina":
    print("I know her!")
    
else:
    print("I don't know her/him.")

