# ---------------------
def new_game():
    guesses =[]
    correct_guesses = 0
    question_number = 1

    for key in questions:
        print("---------------------")
        print(key)
        for i in options[question_number-1]:
            print(i)
        guess = input("Enter (A,B,C,D): ")
        guess =guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_number += 1
    display_score(correct_guesses, guesses)
# ---------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0
# ---------------------
def display_score(correct_guesses, guesses):
    print("---------------------")
    print("RESULTS")
    print("---------------------")

    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score =int((correct_guesses/len(questions))*100)
    print("Your score is: " + str(score) + "%")
# ---------------------
def play_again():

    response = input("Play again? (yes/ no):")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# ---------------------
questions = {"Who's the richest person on the planet?" : "A",
             "What's 2+2?" : "C",
             "Where do mosquitos go in winter?": "D",
             "How old Tupac was when he was shot?" : "B"
}

options = [["A.Elun Musk", "B. Mark Zuckerberg", "C. jeff Bezoss", "D. Bill Gates"],
           ["A.2", "B. 5", "C.4", "D. 8"],
           ["A. North of the wall", "B. Greenwich", "C. Belgium", "D. Kualalampoor"],
           ["A. 33", "B. 28", "C. 45", "D. Haden't started aging yet"]]

new_game()


while play_again():
    new_game()
print("Byeee!")

