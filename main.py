# Beatles Quiz Game

# Create New Game
def new_game():
#Declare Variables
    guesses = []
    correct_guesses = 0
    question_num = 1
  
#Loop through questions
    for key in questions:
        print("-------------------------")
        print(key)
#Show individual question
        for i in options[question_num-1]:
            print(i)
#Get input from user
        guess = input("Enter (A, B, C, or D): ")
#Convert answer to uppercase if lowercase
        guess = guess.upper()
#Add guess to list of guesses
        guesses.append(guess)
#Add correct guesses to total
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
#Display final score
    display_score(correct_guesses, guesses)

def check_answer(answer, guess):
#Check if correct answer matches user input and respond accordingly
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

#Display final score function
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")
#Display all right answers
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
#Display all user guesses
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()
#Calculate and display final score
    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

# Play game again
def play_again():
# Ask user if they would like to play again
    response = input("Do you want to play again? (yes or no): ")
# Convert response to uppercase if lowercase
    response = response.upper()

    if response == "YES" or response == "Y":
        return True
    else:
        return False

# Questions for quiz game
questions = {
  "What is Ringo's real name?: ": "A",
  "Where are the Beatles from?: ": "B",
  "What was the Beatle's first album?: ": "C",
  "What is the name of the Beatle's first drummer?: ": "A"
}


# Possible Answers to questions
options = [["A. Richard Starkey", "B. Bill Smith", "C. Robert Zimmerman", "D. Pete Best"],
           ["A. London", "B. Liverpool", "C. New York", "D. Los Angeles"],
           ["A. Abbey Road", "B. Revolver", "C. Please Please Me", "D. A Hard Day's Night"],
           ["A. Pete Best", "B. Phil Collins", "C. Brian Esptein", "D. George Martin"]]

new_game()

#If user says they want to play again, run program from the beginning
while play_again():
    new_game()

print("Hello, Goodbye!")


