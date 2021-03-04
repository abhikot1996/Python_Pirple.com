prime=0
for num in range(1,101):
    if num > 1:
        check=num
        for isprime in range(2,check):
            if check % isprime == 0:
                break
        else:
            print(f"{num} is Prime |",end=" ")
            prime=num
    if num % 3 == 0 and num % 5 == 0:
        print(f"FizzBuzz {num} is Multiple of 3 and 5 |",end=" ")
    elif num % 3 == 0:
        print(f"Fizz {num} is Multiple of 3 |",end=" ")
    elif num % 5 == 0:
        print(f"Buzz {num} is Multiple of 5 |",end=" ")

    elif num % 3 and num % 5 and num !=prime:
        print(num,end=" | ")
    if num % 10 == 0:
        print(end="\n")