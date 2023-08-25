#project name: Password Generator

import string
import random

if __name__ == "__main__":
    
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation 
    
    while True:
        try:
            pass_length = int(input("Enter The password length:\n"))
            pass_count = int(input("Enter the number of required passwords:\n"))
            break  # Break the loop if the input is a valid integer
        except ValueError:
            print("Invalid input. Please enter a valid integer for password length and count.")

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    
    for i in range(0, pass_count):
        print("".join(random.sample(s, pass_length)))

#alternative
#random.shuffle(s)
#print("".join(s[0:pass_length]))

  
    
    
     