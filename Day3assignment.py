#Program to find the sum of n numbers using while loop
sum1=0
num1=int(input("Enter a number")) 
while(num1>0):
    sum1=sum1+num1
    print(num1, "-->", sum1)
    num1=num1-1

print("The total sum of numbers is ", sum1)


#Program to find if a given number is prime or not 
n=int(input("Enter a number ")) 
if(n%2==0 or n%3==0 or n%5==0 or n%7==0):
   print(" It is not a prime number")
else:
   print("It is a prime number")
