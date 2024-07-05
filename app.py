import os
import google.generativeai as genai
from flask import Flask, render_template, request, redirect, url_for, session
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter  
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename

api_key = 'AIzaSyBKAMX4Lr7A74R2Cw56ZpW6-iEDCB1OeRM'
# Configure Gemini with your API key
genai.configure(api_key=api_key)

# Model selection - Choose a model suitable for text generation (replace if needed)
model = genai.GenerativeModel('gemini-1.5-flash')

app = Flask(__name__)
app.secret_key = '5c2f4c9a38ca6a6b60cc4426524aa45e'

max_questions = 5  # Placeholder for maximum number of questions

@app.route('/')
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/interview", methods=['GET', 'POST'])
def interview():
  if request.method == 'GET':
    return render_template('interview.html')
  
  elif request.method == 'POST':
    # Process user input
    job_profile = request.form['job_profile']
    resume_file = request.files['resume']

    # Ensure the file is allowed (e.g., PDF)
    if resume_file and allowed_file(resume_file.filename):
        # Secure filename
        filename = secure_filename(resume_file.filename)
        # Initialize FileStorage with the uploaded file
        file_storage = FileStorage(resume_file) 
        # Save the file to the designated directory
        file_path = os.path.join('data', filename)  # Adjust 'data' to your desired directory
        file_storage.save(file_path)

        resume_text = extract_text_from_pdf(file_path)

        prompt = f"""
        **Job Profile:** {job_profile}

        **Resume:**
        {resume_text}

        **Task:** You need to act as an Interviewer for the following person ask conduct a 10-15 minute interview. Make sure to use formal language and proper conduct while taking the interview. Your response to this text should be to begin the interview."
        """
    else:
        prompt = f"""
        **Job Profile:** {job_profile}

        **Resume:**
        No resume text available.

        **Task:** You need to act as an Interviewer for the following person ask conduct a 10-15 minute interview. Make sure to use formal language and proper conduct while taking the interview. Your response to this text should be to begin the interview."
        """
     
    question_count = 1
    context_string = prompt
    interview_question = interview_with_gemini(prompt)
    print(context_string, "inside of interview POST route")
    session['question_count'] = question_count  # Initialize question count
    session['context_string'] = context_string  # Initialize context string
    session['interview_question'] = interview_question  # Initialize interview question
    return redirect(url_for('interviewer'))
  
@app.route("/interviewer", methods=['GET', 'POST'])
def interviewer():
  if request.method == 'GET':
    question_count = session.get('question_count', 1)
    context_string = session.get('context_string')
    print(context_string, 'inside of interviewer GET route')
    interview_question = session.get('interview_question')
    session.pop('question_count', None)
    return render_template('interviewer.html', interview_question=interview_question, question_count=question_count)
  
  elif request.method == 'POST':
    user_response = request.form['user_response']

    interview_question = request.form['interview_question']
    print(interview_question, 'INTERVOO QUESTION inside interviewer POST route')

    context_string = session.get('context_string')
    print(context_string, 'inside interviewer POST route, before adding user response')
    session.pop('context_string', None)

    question_count = int(request.form['question_count'])

    context_string += f"\nQ{question_count}:{interview_question}\n User Response: {user_response}"
    print(context_string, 'inside interviewer POST route, after adding user response')

    if question_count >= max_questions:
        return redirect(url_for('results'))  # Redirect to results page

    prompt = f"""
    **Context:**
    {context_string}

    **Task:** Generate the next interview question based on the context provided. Be sure to cover every aspect of the job profile. After having asked 3 questions. evaluate the candidate based on their responses and provide feedback on their performance.
    """
    # Generate next question based on context (replace with actual logic)
    next_question = interview_with_gemini(prompt)
    question_count += 1
    session['context_string'] = context_string

    return render_template('interviewer.html', interview_question=next_question, question_count=question_count)

def allowed_file(filename):
    return filename.lower().endswith('.pdf')

# Function to extract text from PDF (replace with error handling)
def extract_text_from_pdf(file_path):
    # Load the PDF file using PyPDFLoader
    loader = PyPDFLoader(file_path)
    pages = loader.load()

  # Split the text into chunks using RecursiveCharacterTextSplitter
    text_splitter = RecursiveCharacterTextSplitter(
      chunk_size=1000,
      chunk_overlap=200,
      length_function=len,
    )
    docs = text_splitter.split_documents(pages)

  # Extract text from each document and combine into a single string
    resume_text = ""
    for doc in docs:
        resume_text += doc.page_content

    return resume_text

def generate_analysis(context_string):
    # Generate analysis based on the context string (replace with actual logic)
    return context_string  

def interview_with_gemini(prompt):
  """
  This function uses the Gemini API to generate interview questions based on a job profile and resume.

  Prompt:
      job_profile: The job title or position the candidate is applying for (str).
      resume_text: The extracted text content of the candidate's resume (str).
      api_key: Your Google Cloud Project API key for accessing Gemini (str).

  Returns:
      A list of interview questions generated by Gemini (list[str]).
  """

  # with the following statement: "Welcome to our company. I'm pleased to meet you today as we consider your application for the {job_profile} position. The role requires strong technical skills, creativity, and problem-solving abilities. Let's begin with some introductions. Could you please tell me a bit about yourself? What programming languages are you most proficient in, and what projects have you worked on that demonstrate your skills as a software engineer?. Thank you!
  # Generate interview questions using Gemini
  response = model.generate_content(prompt)
  question = response.text.strip().split('\n')
  #question = process_interview_output(question)

  return question

def process_interview_output(text):
  """
  This function removes quotes, asterisks, and combines lines for a more paragraph-like format.

  Args:
      text: The list of strings containing the interview output (list[str]).

  Returns:
      A string with the processed interview text.
  """

  # Remove quotes and asterisks from each line
  processed_lines = [line.strip('*" ') for line in text]

  # Skip empty lines and combine the rest into paragraphs
  paragraphs = []
  current_paragraph = ""
  for line in processed_lines:
    if line:
      current_paragraph += line + " "  # Add space between sentences
    else:
      if current_paragraph:
        paragraphs.append(current_paragraph.rstrip())  # Remove trailing space
      current_paragraph = ""

  # Combine paragraphs with line breaks
  return "\n".join(paragraphs)

if __name__ == '__main__':
    app.run(debug=True)