quiz = {
    "question1": {
        "question": "What is the Capital City of Afghanistan?",
        "city": "Kabul"
    },
    "question2": {
        "question": "What is the Capital City of Albania?",
        "city": "Tirana"
    },
    "question3": {
        "question": "What is the Capital City of Algeria?",
        "city": "Alger"
    },
    "question4": {
        "question": "What is the Capital City of American Samoa?",
        "city": "Fagatogo"
    },
    "question5": {
        "question": "What is the Capital City of Andorra?",
        "city": "Andorra la Vella"
    },
}
score = 0
for key, value in quiz.items():
    print(value['question'])
    answer = input('Answer: ')
    ans = value['city']

    if answer.lower() == value['city'].lower():
        print('You Are Correct.')
        score += 1
        print(f'Your Score is: {score}.')
    else:
        print(f'You are Wrong. The answer is {ans}.')
print(f'You got {score} out of 5. Your percentage is {score/5*100}%.')

