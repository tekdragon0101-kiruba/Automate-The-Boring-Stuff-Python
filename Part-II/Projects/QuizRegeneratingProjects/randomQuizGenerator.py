#! python3 
# randomQuizGenerator.py - Creates quizzes with question and shuffle the choices
# randomly along with answer keys.

import random
import os

# The quiz data - keys are States and values are the Capitals

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New \
Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West \
Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


# Generate quiz files
for quizNum in range(35):
    # create quiz and answer key files:
    absolutePath = os.path.abspath('.\Part-II\Projects\QuizRegeneratingProjects\OutputFiles')

    quizFileObject = open(os.path.join(absolutePath, 'capitalsQuiz%s.txt' % (quizNum + 1)), 'w')
    answerKeyFileObject = open(os.path.join(absolutePath,'capitalsQuizAnswers%s.txt' % (quizNum + 1)), 'w')

    # write the header to the quiz file
    quizFileObject.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFileObject.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFileObject.write('\n\n')

    # shuffle the order of the states:
    states = list(capitals.keys())
    random.shuffle(states)

    # create answer options
    # loop through the 50 states for 50 questions
    for questionNum in range(50):

        # Get correct and wrong answers
        wrongAnswers = list(capitals.values())
        correctAnswer = capitals[states[questionNum]]
        
        # remove correct answer from wrong answers
        del wrongAnswers[wrongAnswers.index(correctAnswer)]

        # get 3 random options 
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]

        # shuffle the options 
        random.shuffle(answerOptions)

        # write questions and answer options into the quiz file
        quizFileObject.write('%s. what is the capital of %s?\n' % (questionNum + 1, states[questionNum]))

        # adding options for question
        for i in range(4):
            quizFileObject.write('\t%s. %s\n' % ('ABCD'[i], answerOptions[i]))
        
        # new line for upcoming new questions
        quizFileObject.write('\n')

        # Write answers to answer file
        answerKeyFileObject.write('%s. %s - %s\n' % (str(questionNum+1).rjust(2), 'ABCD'[answerOptions.index(correctAnswer)], correctAnswer)) 

    quizFileObject.close()
    answerKeyFileObject.close()