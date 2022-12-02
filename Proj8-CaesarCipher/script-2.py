# Prime number checker

def prime_checker(number):
    flag = True
    for i in range(2, number):
        if number % i == 0:
            flag = False
    print(f"{number} is a prime number!") if flag else print(f"{number} is not a prime number...")


n = int(input("Check this number: "))
prime_checker(number=n)
