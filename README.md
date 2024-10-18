# Mock Interview Application - Flask 🎙️💼

Welcome to the **Mock Interview Application**, a Flask-based web application designed to help candidates prepare for various job roles through simulated interviews. This project allows users to enter a job profile, optionally upload their resume, and experience a mock interview tailored to the selected role.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Usage Instructions](#usage-instructions)
- [Project Structure](#project-structure)
- [Future Improvements](#future-improvements)
- [License](#license)
- [Contributions](#contributions)

## Project Overview

This project leverages the Flask framework, Google's Gemini AI model, and LangChain to conduct personalized mock interviews. Users can:

- Select a job role for the interview.
- Upload their resume (in PDF format) to provide context.
- Engage in an interactive, AI-driven interview experience.
- Receive tailored feedback after completing the interview.

## Features

✨ **Job-specific interviews**: Interviews are customized based on the selected job profile.
📄 **Resume parsing**: The uploaded resume is analyzed to personalize questions.
💬 **Interactive session**: Users answer questions one by one, with the next question generated dynamically.
🔄 **Session management**: Progress is tracked using Flask sessions.
🤖 **AI feedback**: After answering several questions, users receive feedback on their performance.

## Technologies Used

- [Flask](https://flask.palletsprojects.com/): Web framework for building the backend and handling routes.
- [Google Generative AI (Gemini)](https://cloud.google.com/ai-platform/training/docs/algorithms/gemini): To generate interview questions and analyze user responses.
- [LangChain](https://python.langchain.com/): For text processing and extracting information from PDFs.
- [Werkzeug](https://werkzeug.palletsprojects.com/): Utilities for working with file uploads securely.

**Requirements** (from `requirements.txt`): 
flask
google-generativeai
langchain
werkzeug

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/mock-interview-app.git
   cd mock-interview-app

2. Set up a virtual environment (optional but recommended):

```shellscript
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```


Install dependencies:

```shellscript
pip install -r requirements.txt
```


Add your Google API key:

- Replace `'YourAPIkey'` in the code with your valid Google API key.



Create a directory for uploads:

```shellscript
mkdir data
```


Run the Flask application:

```shellscript
python app.py
```


Open the application in a browser:

- Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Usage Instructions

1. **Home Page**:

1. Navigate to the homepage where you'll see the options for starting a new interview.



2. **Interview Setup**:

1. Enter the job profile for which you want to simulate an interview.
2. Upload your resume (optional) in PDF format.



3. **Mock Interview**:

1. The interview begins, and you'll be presented with one question at a time.
2. Answer the questions to proceed through the interview.



4. **Feedback and Results**:

1. After answering several questions, the AI will provide feedback on your performance.

## Project Structure

```plaintext
/mock-interview-app
│
├── templates/           # HTML templates (home.html, interview.html, etc.)
├── static/              # Static files (CSS, JS, etc.)
├── data/                # Directory for uploaded resumes
├── requirements.txt     # Dependencies
├── app.py               # Main Flask application
└── README.md            # Project documentation (this file)
```

## Future Improvements

- User Authentication: Allow users to create accounts and track interview history.
- Role-specific templates: Add predefined interview templates for popular roles.
- Question Bank: Incorporate a question bank for certain job profiles.
- Improved Feedback: Use NLP models to analyze responses more thoroughly.
- Deployment: Host the application on a cloud platform like Heroku or AWS.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contributions

Feel free to fork the repository and submit pull requests for improvements. Contributions are welcome! 🎉
