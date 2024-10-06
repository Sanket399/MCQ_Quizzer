import random
import os

# Function to load questions from a file
def load_questions(file_name):
    questions = []
    with open(file_name, 'r') as file:
        content = file.read().strip().split('\n\n')  # Split by double newlines
        for item in content:
            lines = item.strip().split('\n')
            question = lines[0]
            options = lines[1:5]
            answer = lines[5].split(': ')[1]  # Get the correct answer
            questions.append((question, options, answer))
    return questions

# Function to run the quiz
def quiz(questions):
    score = 0
    random.shuffle(questions)  # Shuffle questions for randomness
    
    for question, options, correct_answer in questions:
        print(question)
        for idx, option in enumerate(options, start=1):
            print(f"{idx}. {option}")

        # Get user's answer
        answer = input("Your answer (1-4): ")
        if options[int(answer) - 1] == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}\n")
            
    print(f"Your final score is: {score}/{len(questions)}")

# Main function to run the program
def main():
    subject_files = {
        "FCN": "FCN_mcqs.md",
        "Networking": "networking_mcqs.md",
        "Security": "security_mcqs.md",
        # Add more subjects here as needed
    }

    print("Select a subject:")
    for idx, subject in enumerate(subject_files.keys(), start=1):
        print(f"{idx}. {subject}")

    subject_choice = int(input("Enter the number of your choice: ")) - 1
    selected_subject = list(subject_files.keys())[subject_choice]
    mcq_file = subject_files[selected_subject]

    # Load and quiz
    questions = load_questions(mcq_file)
    quiz(questions)

# Start the program
if __name__ == "__main__":
    main()
