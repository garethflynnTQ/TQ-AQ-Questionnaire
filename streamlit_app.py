import streamlit as st
import numpy as np  # For calculating the average AQ

# --- TQ Branding Colors (from guidelines) ---
tq_rich_blue = "#244092"
tq_vibrant_orange = "#f03c24"
tq_grey = "#ededf0"
tq_light_grey = "#f5f5f7"
tq_white = "#ffffff"

# --- Fonts (To implement fully, you'd need to ensure these are available or use web imports) ---
# For simplicity, let's use web-safe alternatives for now
primary_font = "Arial Black"  # Closest to Source Sans Pro
secondary_font = "Arial Bold"  # Closest to Ubuntu Bold
tertiary_font = "Calibri"  # Closest to Open Sans

# --- Page Configuration ---
st.set_page_config(page_title="TQ Adaptability Quotient (AQ) Questionnaire", page_icon=":question:")

# --- CSS Styling ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")  # Create a style.css file in the same directory

# --- AQ Definition ---
st.markdown(f"<h1 style='color: {tq_rich_blue}; font-family: {primary_font};'>TQ Adaptability Quotient (AQ) Questionnaire</h1>", unsafe_allow_html=True)

st.markdown(f"""
<div style='background-color: {tq_light_grey}; padding: 15px; border-radius: 10px; font-family: {tertiary_font};'>
    <b>Adaptability Quotient (AQ)</b> refers to an individual's capacity to adjust to new conditions, learn new skills, and thrive in changing environments. 
    It encompasses traits like flexibility, resilience, curiosity, and a willingness to embrace uncertainty.
</div>
""", unsafe_allow_html=True)

# --- Questions ---
questions = [
    {
        "question": "1. When your usual way of doing things is suddenly disrupted, you typically:",
        "options": {
            "a": {"text": "Feel a bit frustrated initially but then focus on finding a new approach.", "score": 3},
            "b": {"text": "Feel somewhat uneasy and prefer to stick to familiar methods if possible.", "score": 2},
            "c": {"text": "See it as an opportunity to explore different possibilities and learn something new.", "score": 4},
            "d": {"text": "Find it takes a while to adjust and can feel quite disruptive to your flow.", "score": 1},
        },
    },
    {
        "question": "2. When faced with a completely new task or challenge, you are most likely to:",
        "options": {
            "a": {"text": "Feel a bit hesitant but willing to give it a try and learn as you go.", "score": 3},
            "b": {"text": "Prefer to have clear guidelines and examples before starting.", "score": 2},
            "c": {"text": "Approach it with enthusiasm and a desire to understand it thoroughly.", "score": 4},
            "d": {"text": "Feel somewhat uncertain and might take a while to figure out where to start.", "score": 1},
        },
    },
    {
        "question": "3. When you encounter a significant change at work or in your personal life, your first reaction is usually to:",
        "options": {
            "a": {"text": "Acknowledge the change and try to understand its implications.", "score": 3},
            "b": {"text": "Feel a sense of uncertainty and worry about how it will affect you.", "score": 2},
            "c": {"text": "Actively seek information and look for ways to navigate the new situation effectively.", "score": 4},
            "d": {"text": "Initially resist the change and hope things will stabilize soon.", "score": 1},
        },
    },
    {
        "question": "4. If you invest time and effort in learning a new skill and then realize it's no longer relevant, you would:",
        "options": {
            "a": {"text": "Be a little disappointed but recognize the value of learning itself.", "score": 3},
            "b": {"text": "Feel frustrated but eventually move on to other things.", "score": 2},
            "c": {"text": "Quickly identify other potentially useful skills and start exploring them.", "score": 4},
            "d": {"text": "Continue to try and find ways to apply the learned skill, even if less effective.", "score": 1},
        },
    },
    {
        "question": "5. When someone presents a completely different perspective on a topic you feel strongly about, you typically:",
        "options": {
            "a": {"text": "Listen respectfully and consider their viewpoint, even if you don't agree.", "score": 3},
            "b": {"text": "Hear them out but maintain your original stance.", "score": 2},
            "c": {"text": "Find it interesting to understand different ways of thinking.", "score": 4},
            "d": {"text": "Become somewhat defensive and want to explain why your view is correct.", "score": 1},
        },
    },
    {
        "question": "6. When faced with a complex problem you've never encountered before, you tend to:",
        "options": {
            "a": {"text": "Break it down into smaller steps and try different strategies.", "score": 4},
            "b": {"text": "Feel challenged and might need some time to figure out where to begin.", "score": 2},
            "c": {"text": "See it as an interesting puzzle to solve and enjoy the process.", "score": 3},
            "d": {"text": "Feel a bit lost and might seek guidance or help early on.", "score": 1},
        },
    },
    {
        "question": "7. In situations where the rules or guidelines are unclear or constantly changing, you typically:",
        "options": {
            "a": {"text": "Adapt your approach as needed and try to find what works best.", "score": 4},
            "b": {"text": "Prefer more clarity but can manage in the absence of it.", "score": 3},
            "c": {"text": "See it as an opportunity to be flexible and innovative.", "score": 3},
            "d": {"text": "Prefer more structure and predictability and might find it difficult to operate without them.", "score": 1},
        },
    },
    {
        "question": "8. If you receive constructive criticism that challenges your usual way of working, you are most likely to:",
        "options": {
            "a": {"text": "Reflect on the feedback and consider making adjustments.", "score": 3},
            "b": {"text": "Acknowledge it but might not immediately change your approach.", "score": 2},
            "c": {"text": "See it as valuable input for growth and improvement.", "score": 4},
            "d": {"text": "Feel a bit discouraged and question your abilities.", "score": 1},
        },
    },
    {
        "question": "9. When you notice a new trend or technology emerging in your field, you typically:",
        "options": {
            "a": {"text": "Ignore it and stick to what you know.", "score": 1},
            "b": {"text": "Take a cautious approach, observing how others use them before trying them yourself.", "score": 2},
            "c": {"text": "Show interest and actively explore how these new tools can enhance your work.", "score": 4},
            "d": {"text": "Find it requires significant effort to keep up with these changes.", "score": 3},
        },
    },
    {
        "question": "10. When you anticipate a significant upcoming change that will affect you, you typically:",
        "options": {
            "a": {"text": "Wait to see how things unfold and then react.", "score": 1},
            "b": {"text": "Think about potential challenges and start to plan how you might adapt.", "score": 3},
            "c": {"text": "Actively seek information about the change and look for ways to prepare and potentially benefit.", "score": 4},
            "d": {"text": "Feel a bit anxious and hope the change won't be too disruptive.", "score": 2},
        },
    },
    {
        "question": "11. If you realize that a long-held belief or approach you have is no longer effective in a new situation, you are most likely to:",
        "options": {
            "a": {"text": "Hold onto it initially, hoping it will eventually become relevant again.", "score": 1},
            "b": {"text": "Gradually start to question its validity and consider alternative ways of thinking.", "score": 2},
            "c": {"text": "Recognize the need to change and actively seek out new information and perspectives.", "score": 4},
            "d": {"text": "Feel confused and unsure about what to believe or do.", "score": 3},
        },
    },
    {
        "question": "12. When new technologies, tools, or AI are introduced that significantly change your usual ways of working, you typically:",
        "options": {
            "a": {"text": "Feel resistant and prefer to stick with the familiar methods as long as possible.", "score": 1},
            "b": {"text": "Take a cautious approach, observing how others use them before trying them yourself.", "score": 2},
            "c": {"text": "Show interest and actively explore how these new tools can enhance your work.", "score": 4},
            "d": {"text": "Find it challenging to adapt to new systems and processes.", "score": 3},
        },
    },
]

# --- State Management ---
if "answers" not in st.session_state:
    st.session_state.answers = {}

# --- Display Questions ---
for i, q in enumerate(questions):
    st.markdown(f"<h3 style='color: {tq_rich_blue}; font-family: {primary_font};'>{q['question']}</h3>", unsafe_allow_html=True)
    selected_option = st.radio(
        "",  # Empty label for the radio group
        list(q["options"].keys()), # Pass the option keys to st.radio
        key=f"q{i}", # Unique key for each question
        index=None, # Initialize with no default selection
        format_func=lambda option_key: f"{option_key}. {q['options'][option_key]['text']}" # Format the display
    )
    if selected_option is not None:  # Check if an option has been selected
        st.session_state[f"q{i}"] = q["options"][selected_option]["score"]

# --- Calculate Score ---
def calculate_score():
    total_score = 0
    for key in st.session_state.keys():
        if key.startswith("q"):  # Only consider keys that start with "q"
            total_score += st.session_state[key]
    return total_score

# --- Provide Feedback ---
def provide_feedback(total_score):
    percentage_aq = (total_score / 48) * 100
    st.subheader(f"Your Total AQ Score: {total_score} / 48")
    st.subheader(f"Your AQ: {percentage_aq:.2f}%")

    if 25 <= percentage_aq <= 48:
        st.markdown(f"<div style='background-color: {tq_light_grey}; padding: 10px; border-radius: 5px; font-family: {tertiary_font};'><b>AQ-Low:</b> Your adaptability is relatively lower. You may tend to prefer routine and find it challenging when faced with unexpected changes. Focus on developing your flexibility and openness to new experiences.</div>", unsafe_allow_html=True)
    elif 50 <= percentage_aq <= 73:
        st.markdown(f"<div style='background-color: {tq_light_grey}; padding: 10px; border-radius: 5px; font-family: {tertiary_font};'><b>AQ-Moderate:</b> Your adaptability is moderate. You show some willingness to adjust to change, but there's room to grow. Continue to practice stepping outside your comfort zone and embracing new opportunities.</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='background-color: {tq_light_grey}; padding: 10px; border-radius: 5px; font-family: {tertiary_font};'><b>AQ-High:</b> Your adaptability is high! You demonstrate a strong ability to thrive in changing circumstances. Maintain your open-mindedness and continue to seek out challenges that will further enhance your adaptability.</div>", unsafe_allow_html=True)

# --- Submit Button ---
if st.button("Submit"):
    if len(st.session_state.answers) < len(questions):
        st.warning("Please answer all questions before submitting.")
    else:
        total_score = calculate_score()
        provide_feedback(total_score)
