for nary in range (10):
    print ( nary+1)

for dara in range(1,11):
    print(dara*2)

for Nita in range(20,0,-1):
    print(Nita)


n=int(input("write a positive number: "))
value=0
for i in range(1,n+1):
    value = value+i
print(value)

b=int(input("write a positive number: "))

for c in range(1,11):
    print(f"{b}*{c}={b*c}")


n=int(input("write a positive number: "))
count=0
for i in range(1,101):
    if i%n==0:
        count+= 1
print(count)

n=int(input("How many number do you want to input?:" ))
numbers=[]
for i in range (1,n+1):
    number_input= int(input("Enter a number:"))
    numbers.append(number_input)
print(max(numbers))

n=int(input("write a number: "))
pattern=""
for i in range(1,n+1):
    pattern+=str(i)
    print(pattern)

n=input("write your favorite number: ")
sum=0
for i in n:
    sum=sum+int(i)
print(sum)

n=int(input("enter a number:"))
count=0
for i in range(1,n):
    if n%i==0:
        count= count+i
if(count==n):
    print(n," is a perfect number")
else:
    print(n," is not a perfect number")




