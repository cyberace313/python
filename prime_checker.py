def prime_checker(num):
    if num < 0:
        print("Please input a positive number")
    elif num == 0 or num == 1:
        print("Neither prime nor composite")
    elif num == 2 or num == 3 or num == 5 or num == 7:
        print("It is a Prime number")
    else:
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
            print("It is not a Prime Number")
        else:
            print("It is a Prime Number")


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

for prime in primes:
    prime_checker(prime)