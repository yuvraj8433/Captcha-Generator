def main():
    # List of questions and their correct answers
    questions = [
        {
            "question": "What is the correct file extension for Python files?",
            "answer": ".py"
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "answer": "Harper Lee"
        },
        {
            "question": "What is the smallest planet in our solar system?",
            "answer": "Mercury"
        }
    ]
    
    # Initialize score
    score = 0

    # Iterate through questions
    for q in questions:
        # Get user answer
        user_answer = input(q["question"] + " ")
        
        # Check if answer is correct
        if user_answer.strip().lower() == q["answer"].strip().lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer is {q['answer']}.")

        # Display current score
        print(f"Your current score is: {score}/{len(questions)}\n")

    # End of quiz
    print(f"Quiz Over! Your final score is: {score}/{len(questions)}")

    # Display a message based on performance
    if score == len(questions):
        print("Excellent! You got all the answers right!")
    elif score > len(questions) / 2:
        print("Good job! You got more than half of the answers correct!")
    else:
        print("Better luck next time! Keep practicing.")

if __name__ == "__main__":
    main()
