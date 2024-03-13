#The code will request for the service user to input a sentence

result = ""

user_input = input("please enter a sentence")

#This code will convert alternative letters of the input sentence into capitals

for i in range (len(user_input)):

    if i % 2 == 0:
        result += user_input[i].upper()

    else:
        result += user_input[i].lower()

print(f"{result}")

#The code below will convert alternative words of the inputed sentence into capitals 


seperator = " "
    
edited_user_input = user_input.split()

for i in range (len(edited_user_input)):
    if i % 2 == 0:
        edited_user_input[i] = edited_user_input[i].upper()

    else:
        edited_user_input[i] = edited_user_input[i].lower()
        
        


word_result = seperator.join(edited_user_input)


print(f"{word_result}")

def happy_birthday(g):
    
    print(f"Happy Birthday to {g}")
    print("Happy Birthday to you")
    print("Happy Birthday to you")

happy_birthday("Dude")
happy_birthday("Tom")
happy_birthday("Simon")