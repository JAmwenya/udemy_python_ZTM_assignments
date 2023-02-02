#!/usr/bin/python3
#accepts username and password and returns the length of your hidden password
er_name = input("what is your username? ")
password = input("enter your password ")
print(f"{user_name}, your password {('*' * len(password))} is {len(password)} letters long")
