# Lab 05 - Exercise A - Question 1
for i in range(3):
    print("SSUET")
 
#Exercise A - Question 2
count = 3
while count < 8:
    count = count + 3
    print(count)
#Exercise A - Question 3    
for v in range (4, 8):
 print (v)
 
#Exercise B - Question 1
i = 1
while i < 10:
    if i % 2 == 0:
        print(i)
    i += 1 

#Exercise B - Question 2
i = 1
while i>0:
    print(i)
    i = i + 1
    
#Exercise B - Question 3
for v in range(3, 9, 2):
    print(v)

#Exercise C - Question 1
total = 0

print("The First Natural Numbers Are")

for i in range(1,11):
    print(i, end=" ")
    total = total + i

print("\n The sum is:", total)

#Exercise C - Question 2
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

 

