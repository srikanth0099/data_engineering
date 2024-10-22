def prime_check(x):
    if x>1:
        for i in range(2,x):
            if (x%i==0):
                print(f"{x} is not a prime number")
                break
        else:
            print(f"{x} is a prime number")
        
    else:
        print(f"{x} is not a prime number")

prime_check(7)