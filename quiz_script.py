import os
import random

def load_mcqs(filename):
    with open(filename, 'r') as file:
        content = file.read().strip().split('\n\n')

    if not content:  # Check if the content is empty
        print(f"The file {filename} is empty. Please add questions.")
        return []  # Return an empty list or handle as needed

    questions = []
    for item in content:
        lines = item.split('\n')
        question = lines[0].strip()
        options = [line.strip() for line in lines[1:-1]]
        correct_answer = lines[-1].strip().split()[-1].upper()  # Extract last word and uppercase
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
        
        if user_answer.isdigit() and 1 <= int(user_answer) <= len(options):
            user_answer_letter = chr(int(user_answer) + 64)  # Convert to 'A', 'B', etc.
            if user_answer_letter == correct_answer:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is: {correct_answer}")
        else:
            print("Invalid input. Please enter a number corresponding to the options.")

    print(f"\nYour final score: {score}/{len(questions)}")

def list_subjects():
    base_path = './subjects'  # Folder containing subject folders
    subjects = {}
    
    for idx, folder in enumerate(os.listdir(base_path)):
        folder_path = os.path.join(base_path, folder)
        if os.path.isdir(folder_path):
            subjects[str(idx + 1)] = folder_path
    
    return subjects

def select_quiz_file(subject_folder):
    files = [f for f in os.listdir(subject_folder) if f.endswith('.md')]
    if not files:
        print("No quiz files available in this subject.")
        return None
    
    print("Select a quiz file:")
    for idx, file in enumerate(files):
        print(f"{idx + 1}. {file[:-3]}")  # Display without .md
    
    choice = input("Enter the number of your choice: ")
    if choice.isdigit() and 1 <= int(choice) <= len(files):
        return os.path.join(subject_folder, files[int(choice) - 1])
    else:
        print("Invalid choice. Please select a valid file.")
        return None

def main():
    subjects = list_subjects()
    
    if not subjects:
        print("No subjects found.")
        return
    
    print("Select a subject:")
    for key, subject_path in subjects.items():
        subject_name = os.path.basename(subject_path)
        print(f"{key}. {subject_name}")

    choice = input("Enter the number of your choice: ")
    
    if choice in subjects:
        quiz_file = select_quiz_file(subjects[choice])
        if quiz_file:
            questions = load_mcqs(quiz_file)
            quiz_user(questions)
    else:
        print("Invalid choice. Please select a valid subject.")

if __name__ == "__main__":
    main()
