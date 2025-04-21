import random
import string

user_input = int(input('Enter the length of the password:'))
char = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(char) for i in range(user_input))
print(password)
