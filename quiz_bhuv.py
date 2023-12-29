import random

def display_question(question, options):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    return int(input("Enter your answer (1-4): "))

def check_answer(user_answer, correct_answer, score):
    if user_answer == correct_answer:
        print("Correct!")
        return score + 1
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.")
        return score

def run_quiz(questions):
    total_questions = len(questions)
    user_score = 0

    for index, (question, options, correct_answer) in enumerate(questions, start=1):
        print(f"\nQuestion {index}/{total_questions}:")
        user_answer = display_question(question, options)
        user_score = check_answer(user_answer, correct_answer, user_score)

    print("\nQuiz completed!")
    print(f"Your final score is: {user_score}/{total_questions}")

# Define your quiz questions, options, and correct answers
quiz_questions = [
    ("What is the capital of France?", ["Berlin", "Paris", "Madrid", "Rome"], 2),
    ("Which planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter", "Saturn"], 1),
    ("What is the largest mammal?", ["Elephant", "Whale Shark", "Blue Whale", "Giraffe"], 3),
]

# Shuffle the questions to provide a random order
random.shuffle(quiz_questions)

# Run the quiz
run_quiz(quiz_questions)
