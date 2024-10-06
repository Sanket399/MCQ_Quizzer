import tkinter as tk
import random

# Function to load MCQs from a file
def load_mcqs(filename):
    with open(filename, 'r') as file:
        content = file.read().strip().split('\n\n')
    
    questions = []
    for item in content:
        lines = item.strip().split('\n')
        question = lines[0].strip()
        options = [line.strip() for line in lines[1:-1]]
        
        # Extract correct answer from the last line
        correct_answer = lines[-1].strip().split()[-1]  # Extract the option letter (a, b, c, d)
        
        # Find the corresponding option text based on the letter
        correct_answer_text = options[ord(correct_answer) - ord('a')].strip()  # Convert 'a', 'b', 'c', or 'd' to index
        questions.append((question, options, correct_answer_text))
    
    return questions

# Class to handle the quiz UI using tkinter
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Platform")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        self.subjects = {
            '1': 'FCN_mcqs.md',
            '2': 'Networking_mcqs.md',
            '3': 'Security_mcqs.md',
        }
        
        self.current_question_index = 0
        self.score = 0
        self.questions = []

        # Call the method to create the subject selection screen
        self.create_subject_selection()

    # Create the subject selection screen
    def create_subject_selection(self):
        self.clear_window()
        
        tk.Label(self.root, text="Select a Subject", font=("Arial", 16)).pack(pady=20)
        
        for key, subject in self.subjects.items():
            subject_name = subject[:-3]  # Remove .md from display
            tk.Button(self.root, text=subject_name, font=("Arial", 12), width=20, command=lambda key=key: self.start_quiz(key)).pack(pady=5)

    # Clear the current window content
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # Load the selected subject's questions and start the quiz
    def start_quiz(self, subject_key):
        self.questions = load_mcqs(self.subjects[subject_key])
        random.shuffle(self.questions)
        self.current_question_index = 0
        self.score = 0
        self.show_question()

    # Display the current question
    def show_question(self):
        self.clear_window()
        if self.current_question_index < len(self.questions):
            question, options, correct_answer = self.questions[self.current_question_index]
            self.correct_answer = correct_answer
            
            tk.Label(self.root, text=question, wraplength=380, font=("Arial", 14)).pack(pady=20)
            
            self.selected_option = tk.StringVar(value="0")
            self.radio_buttons = []  # Store radio buttons for later access
            
            for option in options:
                radio_button = tk.Radiobutton(self.root, text=option, variable=self.selected_option, value=option, font=("Arial", 12))
                radio_button.pack(anchor='w', padx=20)
                self.radio_buttons.append(radio_button)  # Keep track of radio buttons
            
            # Add the next button to check the answer
            self.submit_button = tk.Button(self.root, text="Submit Answer", command=self.check_answer)
            self.submit_button.pack(pady=10)

        else:
            self.show_score()  # Show score if no more questions

    # Check if the selected answer is correct and update the UI accordingly
    def check_answer(self):
        selected_option = self.selected_option.get()
        
        if selected_option == self.correct_answer:
            for widget in self.radio_buttons:
                if widget['text'] == selected_option:
                    widget.config(fg='green')  # Correct answer
            self.score += 1
            self.current_question_index += 1
            self.root.after(1000, self.show_question)  # Wait 1 second before showing the next question
        else:
            for widget in self.radio_buttons:
                if widget['text'] == selected_option:
                    widget.config(fg='red')  # Incorrect answer
                    widget.config(state='disabled')  # Disable the incorrect option
                if widget['text'] == self.correct_answer:
                    widget.config(fg='green')  # Show correct answer
            self.submit_button.config(state='disabled')  # Disable the submit button until correct answer is selected
            
            # Enable the submit button only if the correct answer is selected
            for widget in self.radio_buttons:
                if widget['text'] == self.correct_answer:
                    widget.config(command=lambda: self.enable_submit(widget))  # Command to enable the submit button

    # Function to enable the submit button when the correct answer is selected
    def enable_submit(self, correct_widget):
        self.submit_button.config(state='normal')
        self.check_answer()  # Re-check the answer as the correct answer is now selected

    # Display the final score
    def show_score(self):
        self.clear_window()
        score_message = f"Your final score: {self.score}/{len(self.questions)}"
        tk.Label(self.root, text=score_message, font=("Arial", 16)).pack(pady=40)
        
        tk.Button(self.root, text="Restart Quiz", font=("Arial", 12), command=self.create_subject_selection).pack(pady=10)

# Run the tkinter application
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
