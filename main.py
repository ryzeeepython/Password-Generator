import random

symbols = "abcdefghijklmnoprst1234sgktyo123456789<>?+_=-"

def main():
    amount = int(input("How many passwords?: "))
    number = int(input("Amount of symbols: "))
    for k in range(amount):
        password = ''
        for i in range(number):
            password += random.choice(symbols)
        print(password)    
    
main()
