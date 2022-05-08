def prime_checker(number):
    is_prime = True
    if number == 2:
        print('Prime number')
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print('prime number')
    else:
        print("not a prime number")
    # if number <= 1:
    #     print("Prime numbers are greater than 1")
    # if number == 2 or number == 3 or number == 5 or number == 7:
    #     print(f"Prime number {number}")
    # if number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 ==0:
    #     pass
    # else: 
    #     print(f"prime number {number}")

n = int(input("Check this number: "))
# for i in range (2,100):
prime_checker(n)



