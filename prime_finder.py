#prime finder 
def find_prime(number):
    is_prime = True 
    for num in range (2,num):
        if number % num ==0:
            is_prime =False 
            break
    if is_prime:
            print("This is a prime number")
    else:
         print(" This is not a prime number") 

number = int (input('please enter a number:'))
find_prime(number)
       
