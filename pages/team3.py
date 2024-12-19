import streamlit as st
import json
import os

# Load questions from team1.json file
json_file_path = os.path.join('pages', 'team3.json')

if os.path.exists(json_file_path):
    with open(json_file_path, 'r') as f:
        questions = json.load(f)
else:
    st.error(f"File {json_file_path} not found.")
    questions = []
    
# Initialize session state variables
if 'question_index' not in st.session_state:
    st.session_state['question_index'] = 0
if 'answered_questions' not in st.session_state:
    st.session_state['answered_questions'] = []

# Display previous answers
st.write("### Previous Answers:")
for idx, ans in enumerate(st.session_state['answered_questions']):
    st.write(f"Q{idx + 1}: {ans['question']} - Your Answer: {ans['answer']}")

# Check if all questions have been answered
if st.session_state['question_index'] < len(questions):
    # Display the current question
    question = questions[st.session_state['question_index']]
    st.write(f"### Question {st.session_state['question_index'] + 1}: {question['question']}")

    # Input for the answer
    user_answer = st.text_input("Your answer", key="answer_input")

    # Check if the answer is correct
    if user_answer and user_answer.lower() == question['answer'].lower():
        # If the answer is correct, move to the next question
        st.session_state['answered_questions'].append({"question": question["question"], "answer": user_answer})
        st.session_state['question_index'] += 1
        st.success("Correct! Moving to the next question.")
        st.rerun()
        
else:
    data = ""
    st.write("### Your Next Clue:")
    for i in questions:
        data += "." +i['answer']
    st.write(data)
    
