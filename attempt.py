print("Welcome to my quiz!")
question = input("Are you ready to attempt? ")
if question.lower() == "yes":
    print("Okay,let's do this! :)" )
    score = 0
else:
    quit()
question_1 = input("What is your first name? ")
if question_1.lower() == "chadrack":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question_2 = input("What is your last name? ")
if question_2.lower() == "ndalamba":
    print("Correct!") 
    score += 1
else:
    print("Incorrect!")

question_3 = input("How old are you? ")
if question_3.lower() == "26":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!" )
print("You got " + str(score/3*100) + "%")
