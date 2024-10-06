import random

def load_mcqs(filename):
    with open(filename, 'r') as file:
        content = file.read().strip().split('\n\n')
    
    questions = []
    for item in content:
        lines = item.split('\n')
        question = lines[0].strip()
        options = [line.strip() for line in lines[1:-1]]
        # Update correct_answer extraction
        correct_answer = lines[-1].strip().split()[-1].upper()  # Store as 'A', 'B', 'C', or 'D'
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
        
        # Validate input
        if user_answer.isdigit() and 1 <= int(user_answer) <= len(options):
            # Convert to correct answer letter based on user input
            user_answer_letter = chr(int(user_answer) + 64)  # 1 -> 'A', 2 -> 'B', etc.
            if user_answer_letter == correct_answer:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is: {correct_answer}")
        else:
            print("Invalid input. Please enter a number corresponding to the options.")

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

