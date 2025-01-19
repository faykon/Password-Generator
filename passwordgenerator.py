#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#creating a password list
password_list=[]
for i in range(0,nr_letters):#for in between 0 to how many letters the user wants
    random_letter=random.choice(letters)#setting to random_letter variable random letters from letters list
    password_list.append(random_letter)#adding them to the list 
for i in range(0,nr_symbols):
    random_symbols=random.choice(symbols)
    password_list.append(random_symbols)
for i in range(0,nr_numbers):
    random_numbers=random.choice(numbers)
    password_list.append(random_numbers)  
print(password_list)
#randomizing the order of elements in the password-list
random.shuffle(password_list)
#making passwordlist to a string
password=''.join(password_list)
print(password)