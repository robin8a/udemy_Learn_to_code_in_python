import requests as rq
import json
import pprint as pp
import random
import html

url = "https://opentdb.com/api.php?amount=1&category=11&difficulty=easy"
end_game = ""
score_correct = 0
score_incorrect = 0

while end_game.lower() != "quit":
    response = rq.get(url)
    if (response.status_code != 200):
        end_game =  input ("There was a problem retrieving the question. Press enter to try again or type 'quit' to quit the game: ")
    else:
        valid_answer = False
        answer_number = 1
        data = json.loads(response.text)
        question = data['results'][0]['question']
        answers = data['results'][0]['incorrect_answers']
        correct_answer = data['results'][0]['correct_answer']
        answers.append(correct_answer)
        random.shuffle(answers)
        print ("\n", html.unescape(question), "\n")
        # pp.pprint(data)
        for answer in answers:
            print (str(answer_number) + "- " + html.unescape(answer))
            answer_number += 1
        print("\n")

        while valid_answer == False:
            number_answer = input ("\nType the number of the correct answer: ")
            try:
                number_answer = int(number_answer)
                if (number_answer > len(answers) or number_answer <= 0):
                    print("Invalid answer")
                else:
                    valid_answer = True
            except:
                print("Invalid answer")

        user_answer = answers[number_answer - 1]

        if (  user_answer == correct_answer ):
            print( "\nCongratulations! You answered correctly! The correct answer was: ", html.unescape(correct_answer), "\n" )
            score_correct += 1
        else:
            print ( "Sorry! ", html.unescape(user_answer), " is incorrect. The correct answer is: ", html.unescape(correct_answer), "\n" )
            score_incorrect += 1

        print("###############")
        print("Your score is ")
        print("Correct answers: ", score_correct)
        print("Incorrect answers: ", score_incorrect, "\n")
        print("###############")
        end_game = input ("Press enter to get a new question or type 'quit' to quit the game: ")

print("\nThanks for playing...\n")
