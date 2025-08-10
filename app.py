import streamlit as st
import random
import importlib
import copy
from datetime import datetime, timedelta

QUIZ_FILES = {
    "Quiz 2": "quizzes.quiz2",
    "Quiz 3": "quizzes.quiz3",
    "Quiz 4": "quizzes.quiz4"
    # Add "Quiz 4": "quizzes.quiz4" etc.
}

def load_quiz(quiz_key):
    module = importlib.import_module(QUIZ_FILES[quiz_key])
    return copy.deepcopy(module.quiz)

def shuffle_quiz(quiz_data):
    for q in quiz_data["questions"]:
        correct_text = q["answer_text"]
        random.shuffle(q["options"])
        q["answer"] = q["options"].index(correct_text)
    return quiz_data

def main():
    st.set_page_config(page_title="Databricks Practice Quizzes", layout="centered")
    st.title("📚 Databricks Certification Practice Quizzes")

    page = st.sidebar.radio("Navigate", ["Home", "Take Quiz"])

    if page == "Home":
        st.write("Welcome to the Databricks Certification Practice Quiz App!")
        st.write("Choose a quiz from the sidebar and test your knowledge.")
        st.write("You will have **45 minutes** to complete each quiz.")

    elif page == "Take Quiz":
        quiz_choice = st.selectbox("Select a Quiz", list(QUIZ_FILES.keys()))
        if st.button("Start Quiz"):
            quiz_data = load_quiz(quiz_choice)
            quiz_data = shuffle_quiz(quiz_data)

            st.session_state.quiz_data = quiz_data
            st.session_state.start_time = datetime.now()
            st.session_state.end_time = datetime.now() + timedelta(minutes=45)
            st.session_state.answers = {i: None for i in range(len(quiz_data["questions"]))}
            st.session_state.submitted = False
            st.experimental_rerun()

    # Quiz taking UI
    if "quiz_data" in st.session_state and not st.session_state.submitted:
        time_left = st.session_state.end_time - datetime.now()
        if time_left.total_seconds() <= 0:
            st.session_state.submitted = True
            st.experimental_rerun()

        st.write(f"⏳ Time left: {time_left.seconds//60}:{time_left.seconds%60:02d}")

        for idx, q in enumerate(st.session_state.quiz_data["questions"]):
            current_index = st.session_state.answers.get(idx, 0)
            if current_index is None:
                current_index = 0

            selected_index = st.radio(
                f"**Q{idx+1}: {q['q']}**",
                q["options"],
                index=current_index,
                key=f"q_{idx}"
            )

            # Store the index, not the string
            st.session_state.answers[idx] = q["options"].index(selected_index)
            st.write("---")

        if st.button("Submit"):
            st.session_state.submitted = True
            st.experimental_rerun()

    # Results page
    if "quiz_data" in st.session_state and st.session_state.submitted:
        score = 0
        st.write("### Results")
        for idx, q in enumerate(st.session_state.quiz_data["questions"]):
            selected_index = st.session_state.answers.get(idx, None)
            if selected_index is None:
                st.error(f"Q{idx+1}: No answer selected ❌ — Correct answer: {q['options'][q['answer']]}\n\n{q['explanation']}")
                continue

            user_ans_text = q["options"][selected_index]
            correct_ans_text = q["options"][q["answer"]]

            if user_ans_text == correct_ans_text:
                score += 1
                st.success(f"Q{idx+1}: Correct ✅ — {q['explanation']}")
            else:
                st.error(f"Q{idx+1}: Wrong ❌ — Correct answer: {correct_ans_text}\n\n{q['explanation']}")

        st.write(f"**Your Score:** {score} / {len(st.session_state.quiz_data['questions'])}")

        if st.button("Take Again"):
            for k in ["quiz_data", "answers", "submitted", "start_time", "end_time"]:
                st.session_state.pop(k, None)
            st.experimental_rerun()

if __name__ == "__main__":
    main()
