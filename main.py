
questions = [
    {
        "challenge" : "What instrument does Animal play?",
        "choices"  : 
        {
            'A' : 'Tambourine',
            'B' : 'Electric Guitar',
            'C' : 'Drums',
            'D' : 'Triangle',
        },
        "answer" : "C"
    },
    {
        "challenge" : "Which muppet is green?",
        "choices" : {
            "A" : "Scooter",
            "B" : "Kermit the Frog",
            "C" : "Gonzo",
            "D" : "Fozzy Bear",
        },
        "answer" : "B"
    },
    {
        "challenge" : "Who is the girlfriend of Kermit the Frog?",
        "choices" : {
            "A" : "Miss Piggy",
            "B" : "The Swedish Chef",
            "C" : "Dr Teeth",
            "D" : "Rizzo the Rat",
        },
        "answer" : "A"
    }
]

print('Welcome to the quiz')
print()

score = 0
effort = ''
play = input('Do you want to play? (y/n): ')

if play not in ['y','yes']:
    quit()

print()
print('lets play then...')
print()

for question in questions:
    print(question['challenge'])
    for letter, choice in question['choices'].items():
        print(f"{letter}. {choice}")
    print()
    user_answer = input('Your answer: ')
    while user_answer.upper() not in question['choices']:
        user_answer = input(f'You gave an invalid answer please choose from the following options: {", ".join([option for option in question["choices"]])} : ')
    if user_answer.upper() == question['answer']:
        print('Correct!')
        score += 1
    else:
        print()
        print(f'Sorry, the correct answer is: {question["answer"]}. {question["choices"][question["answer"]]}.')
    print()

percentage = 100 / len(questions) * score
if percentage < 30:
    effort = 'poor'
elif percentage >= 30 and percentage < 70:
    effort = 'moderate'
elif percentage >= 70:
    effort = 'good'

print(f'The quiz has ended you got {score} out of {len(questions)} answers correct.')
print()
print(f'You scored {format(round(percentage,1))}% which is {effort}.')