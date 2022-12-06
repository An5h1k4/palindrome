'''Your task is to write a program to find the nth prime palindrome number, n is the input user will give.
A prime number, such as 127, has no factors other than itself and one. A palindrome, such as 121, is the same number when its digits are reversed.
 A prime palindrome, such as 131, is both prime and a palindrome. '''

n= int(input("Enter Your Desired Number:"))
v=''
if n<1:
    v='This is not prime number'
else:    
    for x in range(2,n):   #Check for prime number
        if n%x==0 or n<1:
            v='This is not prime number'
            
            break
        else:                     #Check for palindrome number
            rev=str(n)[::-1]
            if str(n)==rev:
                v='This a prime and a palindrome number'
            
            else:
                v='This is prime number but, not palindrome number'

print(v)