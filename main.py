import streamlit as st

# Define questions, options, correct answers, and explanations
scenarios = [
    {
        "question": "You worked hard on a project, but your team leader points out several mistakes in front of your team. How do you respond?",
        "options": [
            "I stay quiet, avoid eye contact, and feel embarrassed.",
            "I thank them for the feedback but feel hurt and might bring it up later.",
            "I listen actively, acknowledge their points, and ask for ways to improve."
        ],
        "correct": 2,  # Index of the correct answer (0-based)
        "explanation": "The best way to handle feedback is to listen actively, acknowledge the points made, and seek ways to improve.",
        "scenario": "Handling Feedback"
    },
    {
        "question": "In a meeting, a colleague suggests an idea you strongly disagree with. What would you do?",
        "options": [
            "I stay silent or nod even though I disagree.",
            "I speak up but struggle to find the right words or get defensive.",
            "I calmly share my perspective, explain my reasons, and suggest alternatives."
        ],
        "correct": 2,
        "explanation": "Calmly explaining your perspective and suggesting alternatives is the most constructive approach to disagreements.",
        "scenario": "Expressing Disagreement"
    },
    {
        "question": "A friend makes a joke at your expense that hurts your feelings. What do you do?",
        "options": [
            "I laugh it off but feel hurt and never bring it up.",
            "I bring it up later but struggle to explain why it hurt me.",
            "I tell them how I feel in the moment and explain why it was hurtful."
        ],
        "correct": 2,
        "explanation": "Communicating hurt feelings in the moment and explaining why it was hurtful can help prevent similar situations in the future.",
        "scenario": "Communicating Hurt Feelings"
    },
    {
        "question": "You’re in an argument with a close family member, and the situation is getting heated. How do you respond?",
        "options": [
            "I shut down, stop talking, or walk away to avoid confrontation.",
            "I argue back but later regret the things I said.",
            "I pause, try to de-escalate the situation, and suggest talking calmly."
        ],
        "correct": 2,
        "explanation": "De-escalating the situation and suggesting calm communication can help resolve conflicts constructively.",
        "scenario": "Managing Conflict"
    },
    {
        "question": "You’re struggling with a task at work but don’t understand what went wrong. What do you do?",
        "options": [
            "I avoid asking for help because I’m afraid I’ll be judged or seem weak.",
            "I ask for help but feel embarrassed or don’t fully explain the issue.",
            "I confidently ask for help and explain the situation so I can learn and improve."
        ],
        "correct": 2,
        "explanation": "Confidently asking for help and fully explaining the situation can lead to learning and improvement.",
        "scenario": "Asking for Help"
    },
    {
        "question": "A colleague takes credit for your work in a meeting. What do you do?",
        "options": [
            "Stay quiet and let it go.",
            "Bring it up afterward in private.",
            "Politely correct them during the meeting."
        ],
        "correct": 2,  # Index of the correct answer (0-based)
        "explanation": "Politely correcting them during the meeting demonstrates assertiveness and ensures your contributions are recognized.",
        "scenario": "Handling Credit for Your Work"
    },
    {
        "question": "Someone gives you feedback, and you feel criticized. What’s your immediate reaction?",
        "options": [
            "Defend yourself and explain why they’re wrong.",
            "Stay quiet and feel bad.",
            "Thank them for the feedback and reflect on it."
        ],
        "correct": 2,  # Index of the correct answer (0-based)
        "explanation": "Thanking them for the feedback and reflecting on it shows maturity and emotional intelligence.",
        "scenario": "Handling Criticism"
    },
    {
        "question": "What’s the best way to handle an emotional situation?",
        "options": [
            "React immediately based on how you feel.",
            "Take a deep breath and respond thoughtfully.",
            "Avoid the situation altogether."
        ],
        "correct": 1,  # Index of the correct answer (0-based)
        "explanation": "Taking a deep breath and responding thoughtfully can help you manage your emotions and handle the situation calmly.",
        "scenario": "Managing Emotions"
    },
    {
        "question": "You’ve been misunderstood during a conversation. What do you do?",
        "options": [
            "Let it go and move on.",
            "Clarify your point politely and calmly.",
            "Argue to prove your point."
        ],
        "correct": 1,  # Index of the correct answer (0-based)
        "explanation": "Politely and calmly clarifying your point is the best way to ensure you are understood without escalating the situation.",
        "scenario": "Handling Misunderstanding"
    },
    {
        "question": "You need to give critical feedback to a friend. How do you approach it?",
        "options": [
            "Be direct and tell them what they did wrong.",
            "Use the feedback sandwich: start with something positive, share the critique, and end with encouragement.",
            "Avoid the conversation, as it might hurt their feelings."
        ],
        "correct": 1,  # Index of the correct answer (0-based)
        "explanation": "The feedback sandwich helps to deliver constructive criticism while maintaining the relationship.",
        "scenario": "Giving Critical Feedback"
    },
    {
        "question": "Your manager tells you that your recent work isn’t good enough. How do you respond?",
        "options": [
            "Defend yourself and list reasons for your performance.",
            "Ask for specific feedback on how to improve.",
            "Stay quiet and feel upset."
        ],
        "correct": 1,  # Index of the correct answer (0-based)
        "explanation": "Asking for specific feedback on how to improve is a constructive way to handle criticism and show your willingness to grow.",
        "scenario": "Receiving Critical Feedback"
    }
]

# Initialize session state variables
if 'question_index' not in st.session_state:
    st.session_state['question_index'] = 0
if 'score' not in st.session_state:
    st.session_state['score'] = 0
if 'answered' not in st.session_state:
    st.session_state['answered'] = False
if 'selected_answer' not in st.session_state:
    st.session_state['selected_answer'] = None
if 'feedback' not in st.session_state:
    st.session_state['feedback'] = None
if 'quiz_complete' not in st.session_state:
    st.session_state['quiz_complete'] = False

# Get the current question and options
if not st.session_state['quiz_complete']:
    current_question = scenarios[st.session_state['question_index']]

    # Display the score dynamically
    st.write(f"Score: {st.session_state['score']}/{len(scenarios)}")

    st.title("Scenario-Based Communication Quiz")

    # Display the current question
    st.write(f"### {current_question['question']}")

    # Show the options as radio buttons
    selected_answer = st.radio(
        "Select your answer:",
        current_question['options'],
        index=st.session_state['selected_answer'] if st.session_state['selected_answer'] is not None else 0
    )

    # Submit the answer and display feedback
    if st.button("Submit Answer"):
        # Check if the answer is correct
        selected_index = current_question['options'].index(selected_answer)
        st.session_state['selected_answer'] = selected_index

        if selected_index == current_question['correct']:
            st.session_state['feedback'] = ("Correct", "success", current_question['explanation'])
            st.session_state['score'] += 1
        else:
            st.session_state['feedback'] = ("Wrong", "error", current_question['explanation'])

        st.session_state['answered'] = True

    # Display the feedback immediately
    if st.session_state['answered']:
        if st.session_state['feedback'][1] == "success":
            st.success(st.session_state['feedback'][0] + "! " + st.session_state['feedback'][2])
        else:
            st.error(st.session_state['feedback'][0] + ". " + st.session_state['feedback'][2])

    # "Next" button to proceed to the next question
    if st.session_state['answered']:
        if st.button("Continue to Next Question"):
            st.session_state['question_index'] += 1
            st.session_state['answered'] = False
            st.session_state['selected_answer'] = None
            st.session_state['feedback'] = None

            # If no more questions, mark the quiz as complete
            if st.session_state['question_index'] >= len(scenarios):
                st.session_state['quiz_complete'] = True
                st.session_state['question_index'] = 0  # Reset for potential retry

else:
    st.write(f"### Quiz Completed! Your score is {st.session_state['score']}/{len(scenarios)}.")
    if st.button("Restart Quiz"):
        st.session_state['quiz_complete'] = False
        st.session_state['score'] = 0
        st.session_state['question_index'] = 0
        st.session_state['answered'] = False
        st.session_state['selected_answer'] = None
        st.session_state['feedback'] = None
