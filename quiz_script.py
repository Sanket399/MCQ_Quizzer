import random
import os

def load_mcqs(filename):
    with open(filename, 'r') as file:
        content = file.read().strip().split('\n\n')
    
    questions = []
    for item in content:
        lines = item.split('\n')
        question = lines[0].strip()
        options = [line.strip() for line in lines[1:-1]]
        correct_answer = lines[-1].strip().split()[-1]  # Assuming "Correct answer" is on the last line
        questions.append((question, options, correct_answer))
    
    return questions

def quiz_user(questions):
    random.shuffle(questions)
    score = 0
    
    for question, options, correct_answer in questions:
        print(f"\n{question}")
        for idx, option in enumerate(options):
            print(f"{idx + 1}. {option}")
        
        user_answer = input(f"Your answer (1-{len(options)}): ")
        
        if options[int(user_answer) - 1].strip().lower() == correct_answer.strip().lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")

    print(f"\nYour final score: {score}/{len(questions)}")

def main():
    subjects = {
        '1': 'FCN_mcqs.md',
        '2': 'Networking_mcqs.md',  # Assuming you have this file
        '3': 'Security_mcqs.md',     # Assuming you have this file
    }
    
    print("Select a subject:")
    for key, subject in subjects.items():
        print(f"{key}. {subject[:-3]}")  # Displaying without .md
    
    choice = input("Enter the number of your choice: ")
    
    if choice in subjects:
        questions = load_mcqs(subjects[choice])
        quiz_user(questions)
    else:
        print("Invalid choice. Please select a valid subject.")

if __name__ == "__main__":
    main()
