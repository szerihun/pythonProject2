# Develop a program that take input from the user for a student’s ID,
# name, and scores earned in 5 subjects. Each subject has a maximum
# of 100 points. The program should then calculate the total marks
# earned by the student. Finally, your program should print the
# student’s ID, name, each of the five scores, the total score,
# and the average of the five subjects.

studentID = input("Enter your ID: ")
name = input("Enter your name: ")
score1 = int(input("Enter exam score 1: "))
score2 = int(input("Enter exam score 2: "))
score3 = int(input("Enter exam score 3: "))
score4 = int(input("Enter exam score 4: "))
score5 = int(input("Enter exam score 5: "))

totalScore = score1 + score2 + score3+ score4 + score5
averageScore = (totalScore/5)

print("The student's name is " + name + ".")
print("The student's ID is " + studentID + ".")
print(f"The exam 1 score is {score1}.")
print("The exam 2 score is ", score2)
print(f"The exam 3 score is {score3}.")
print(f"The exam 4 score is {score4}.")
print(f"The exam 5 score is {score5}.")
print("The total score is ", totalScore)
print(f"The average exam score is {averageScore}")