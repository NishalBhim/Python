print ("\nWelcome to our Capital Cities Quiz")

play = input("\nThis quiz has 10 questions, would you like to play?")

if play != "yes":
    quit()

print("\nOkay let's play")
score = 0

name = input("Please enter a username: ")

answer = input("\n1) What is the Capital City of Australia? ")
if answer.lower() == "canberra":
    print("Correct! 1pt has been added to your score!")
    score += 1
else:
    print("Sorry that answer is wrong, the correct answer is Canberra (no pts were added to your score)")

answer = input("\n2) What is the Capital City of Japan? ")
if answer.lower() == "tokyo":
    print("Correct! 1pt has been added to your score!")
    score += 1
else:
    print("Sorry that answer is wrong, the correct answer is Tokyo (no pts were added to your score)")

answer = input("\n3) What is the Capital City of Brazil? ")
if answer.lower() == "brasilia":
    print("Correct! 1pt has been added to your score!")
    score += 1
else:
    print("Sorry that answer is wrong, the correct answer is Brasilia (no pts were added to your score)")

answer = input("\n4) What is the Capital City of Portugal? ")
if answer.lower() == "lisbon":
    print("Correct! 1pt has been added to your score!")
    score += 1
else:
    print("Sorry that answer is wrong, the correct answer is Lisbon (no pts were added to your score)")

answer = input("\n5) What is the Capital City of Egypt? ")
if answer.lower() == "cairo":
    print("Correct! 1pt has been added to your score!")
    score += 1
else:
    print("Sorry that answer is wrong, the correct answer is Cairo (no pts were added to your score)")

answer = input("\n6) What is the Capital City of Mexico? ")
if answer.lower() == "mexico city":
    print("Correct! 1pt has been added to your score!")
    score += 1
else:
    print("Sorry that answer is wrong, the correct answer is Mexico City (no pts were added to your score)")

answer = input("\n7) What is the Capital City of Norway? ")
if answer.lower() == "oslo":
    print("Correct! 1pt has been added to your score!")
    score += 1
else:
    print("Sorry that answer is wrong, the correct answer is Oslo (no pts were added to your score)")

answer = input("\n8) What is the Capital City of Greece? ")
if answer.lower() == "athens":
    print("Correct! 1pt has been added to your score!")
    score += 1
else:
    print("Sorry that answer is wrong, the correct answer is Athens (no pts were added to your score)")

answer = input("\n9) What is the Capital City of Turkey? ")
if answer.lower() == "ankara":
    print("Correct! 1pt has been added to your score!")
    score += 1
else:
    print("Sorry that answer is wrong, the correct answer is Ankara (no pts were added to your score)")

answer = input("\n10) What is the Capital City of Canada? ")
if answer.lower() == "ottawa":
    print("Correct! 1pt has been added to your score!")
    score += 1
else:
    print("Sorry that answer is wrong, the correct answer is Ottawa (no pts were added to your score)")

print ("\nCongratulations " + name + " you got " + str(score) +"/10 pts")
print ("That's " + str((score/10) * 100) + "%")
