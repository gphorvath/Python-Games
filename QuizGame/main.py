from question_model import Question
from quiz_brain import QuizBrain
from open_trivia_wrapper import OpenTriviaWrapper
from art import logo
import os

def get_category():
    print("Choose a category:")
    print("1. Books\n2. Computers\n3. Science\n4. Film\n5. Music")
    selected_category = input("Select a category: ")
    if selected_category == "1":
        return OpenTriviaWrapper.CATEGORY_BOOKS
    elif selected_category == "2":
        return OpenTriviaWrapper.CATEGORY_COMPUTERS
    elif selected_category == "3":
        return OpenTriviaWrapper.CATEGORY_SCIENCE
    elif selected_category == "4":
        return OpenTriviaWrapper.CATEGORY_FILM
    elif selected_category == "5":
        return OpenTriviaWrapper.CATEGORY_MUSIC
    else:
        print("Invalid category selection.")
        return get_category()
    
def get_question_count():
    question_count = input("How many questions would you like to answer? (1-10): ")
    if question_count.isdigit() and 1 <= int(question_count) <= 10:
        return int(question_count)
    else:
        print("Invalid question count.")
        return get_question_count()
    
def get_difficulty():
    print("Choose a difficulty level:")
    print("1. Easy\n2. Medium\n3. Hard")
    selected_difficulty = input("Select a difficulty level: ")
    if selected_difficulty == "1":
        return OpenTriviaWrapper.DIFFICULTY_EASY
    elif selected_difficulty == "2":
        return OpenTriviaWrapper.DIFFICULTY_MEDIUM
    elif selected_difficulty == "3":
        return OpenTriviaWrapper.DIFFICULTY_HARD
    else:
        print("Invalid difficulty selection.")
        return get_difficulty()
    
def get_quiz_brain(questions):
    question_bank = []
    for question in questions:
        text = question["question"]
        answer = question["correct_answer"]
        new_question = Question(text, answer)
        question_bank.append(new_question)

    return QuizBrain(question_bank)
    
def game_loop():
    open_trivia_wrapper = OpenTriviaWrapper()
    os.system('clear')
    print(logo)
    selected_category = get_category()
    selected_count = get_question_count()
    selected_difficulty = get_difficulty()

    open_trivia_wrapper = OpenTriviaWrapper()
    questions = open_trivia_wrapper.get_questions(amount=selected_count, category=selected_category, difficulty=selected_difficulty, type=open_trivia_wrapper.QUESTION_TYPE_BOOLEAN)
    if not questions:
        print("Error fetching questions. Please try again.")
        return game_loop()

    quiz = get_quiz_brain(questions)


    while quiz.still_has_questions():
        os.system('clear')
        print(logo)
        print(f"Your current score: {quiz.score} / {quiz.question_number}")
        quiz.next_question()
        
    print("You've completed the quiz!")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")
    if(input("Would you like to play again? (yes/no): ").lower() == "yes"):
        game_loop()
        
game_loop()