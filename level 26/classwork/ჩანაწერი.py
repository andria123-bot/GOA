# inputs = input("Enter Your Name: ")

# capitalized_name = inputs.capitalize()
# print(capitalized_name)



# sentence = "My Name Is andria, and I am JR.Programmist."

# occurs = sentence.index("m")
# print (occurs)


# sentence = "My Name Is andria, and I am JR.Programmist."

# occurs = sentence.index("m")
# print (occurs)


emails = []

count = int(input("Please Enter How Many Emails Do You Wanna Enter: "))

for i in range(count):
    email = input("Pleace Enter Email: ")

    if email.endswith("@gmail.com"):
        emails.append(email)
        print("Email Was Correct!")
    else:
        print("Invalid Email")
print(emails)