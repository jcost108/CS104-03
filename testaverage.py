#Initialize variables
numberOfScores = 0
score = 0
scoreCount = 0
total = 0
average = 0.0

#Ask user for number of test scores to be averaged
numberOfScores = int(input("Please enter the number of test scores you want to average: "))

#Ask user for each test score and add to total
while scoreCount < numberOfScores:
    score = int(input("\nPlease enter a score: "))
    total += score
    scoreCount += 1
    print("Score received.")

#Average the scores
average = total / numberOfScores

#Display the average
print("\nThe average for the given test scores is:",average)
