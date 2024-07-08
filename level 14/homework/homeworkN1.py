# # while loop 5 მაგალითი

# მაგალითი 1
num = 0

sum = 0

while num <= 10:
    sum = sum + num
    num = num + 2

print(sum)

# მაგალითი 2

num = 100

num1 = 0

while num1 < 10:
    print ("andria")
    num1 = num1 +1

# მაგალითი 3

num = 0

while num != 195:
    num = int(input("Enter Your Number : "))

    if num  == 195:
        print ("Nice You Won")
    
    else: 
        print ("Welp You Loose")


# მაგალითი 4



while True :
    name = input("Enter Your name : ")
    if name  == "andria":
        print ("Succes")
        break
    else: 
        print ("Loose")


# მაგალითი 5


num = 0

while num != 10:
    num = int(input("Enter Your Number : "))

    if num  == 10:
        print ("Good Guess")
    
    else: 
        print ("Bad Guess")