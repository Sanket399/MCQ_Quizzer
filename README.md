# MCQ Quiz Repository

Welcome to the MCQ Quiz Repository! This repository is designed to store multiple-choice questions (MCQs) across various subjects and to facilitate quizzes for educational purposes.

## Table of Contents

- [About](#about)
- [Subjects](#subjects)
- [Getting Started](#getting-started)
- [Repository Structure](#repository-structure)
- [Adding MCQs](#adding-mcqs)
- [Notes on Formatting](#notes-on-formatting)
- [Running the Quiz](#running-the-quiz)
- [Quiz Script](#quiz-script)
- [Customizing the Quiz](#customizing-the-quiz)
- [Contributing](#contributing)
- [License](#license)

## About

This repository is dedicated to collecting and organizing MCQs for various subjects. It aims to help users in their preparation and understanding of different topics.

## Subjects

Currently, the repository contains MCQs for the following subjects:

1. FCN
2. Networking
3. Security
4. _(Add more subjects as needed)_

## Getting Started

To get started with the repository, clone it using the following command:

```bash
git clone https://github.com/yourusername/mcq-quiz-repo.git
```

## Repository Structure

MCQ_Quiz_Repo/
│
├── FCN_mcqs.md # Markdown file containing MCQs for FCN
├── Networking_mcqs.md # Markdown file containing MCQs for Networking
├── Security_mcqs.md # Markdown file containing MCQs for Security
│
└── quiz_script.py # Python script to run the quiz

## Adding MCQs

1. Create a new markdown file for each subject (e.g., FCN_mcqs.md).
2. Format your questions as follows: 1. Question text? \*
   a) Option A
   b) Option B
   c) Option C
   d) Option D
   Correct answer
   b) Option B

## Notes on Formatting

- Ensure that each question is followed by its options and the correct answer in the specified format.
- You can have any number of options (e.g., 4, 5, or more) for each question by adjusting the formatting accordingly.

## Running the Quiz

1. Open Command Prompt (or terminal).
2. Navigate to the repository directory:

   ```bash
   cd path/to/your/MCQ_Quiz_Repo
   ```

3. Run the quiz script:

   ```bash
   python quiz_script.py
   ```

4. Follow the prompts to select a subject and answer the questions.

## Quiz Script

The quiz_script.py script randomly selects questions from the markdown files and quizzes you. It provides feedback on whether your answers are correct and reveals the correct answer if you select an incorrect option.

## Customising the Quiz

You can easily customize the quiz script:

- Add new subjects: Create new markdown files with the same formatting.
- Change question count: The script randomly selects a set number of questions from each subject.
