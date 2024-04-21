n = int(input())


def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's prime")
    else:
        print("It's not prime")


prime_checker(number=n)

