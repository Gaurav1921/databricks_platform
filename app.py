import streamlit as st
import random
import importlib
import copy
from datetime import datetime, timedelta

# Optional smooth 1s timer refresh (recommended)
try:
    from streamlit_autorefresh import st_autorefresh
    AUTOR = True
except Exception:
    AUTOR = False

st.set_page_config(page_title="Databricks Certification Practice Quizzes", layout="wide")

# Map quiz names to modules in /quizzes
QUIZ_FILES = {
    "Quiz 2": "quizzes.quiz2",
    "Quiz 3": "quizzes.quiz3",
    "Quiz 4": "quizzes.quiz4",
}

DEFAULT_DURATION_MIN = 45


# -------------------- Data helpers --------------------
def load_quiz(quiz_key):
    module = importlib.import_module(QUIZ_FILES[quiz_key])
    quiz = copy.deepcopy(module.quiz)
    # Normalize (support older files with numeric answer)
    for q in quiz["questions"]:
        if "answer_text" not in q and "answer" in q:
            q["answer_text"] = q["options"][q["answer"]]
    return quiz


def shuffle_quiz(quiz):
    """Shuffle options per question and compute the correct index."""
    for q in quiz["questions"]:
        correct = q["answer_text"]
        random.shuffle(q["options"])
        q["answer"] = q["options"].index(correct)
    return quiz


def init_state(quiz, duration_min):
    st.session_state.quiz_data = quiz
    st.session_state.start_time = datetime.now()
    st.session_state.end_time = st.session_state.start_time + timedelta(minutes=duration_min)
    st.session_state.current_q = 0
    st.session_state.submitted = False
    # Store selected INDEX or None
    st.session_state.answers = {i: None for i in range(len(quiz["questions"]))}
    # Stable widget keys so radios don’t reset (fixes “double-click”)
    st.session_state.widget_keys = {
        i: f"q_{i}_{random.randint(1, 10**9)}" for i in range(len(quiz["questions"]))
    }


def secs_left():
    if "end_time" not in st.session_state:
        return 0
    return max(0, int((st.session_state.end_time - datetime.now()).total_seconds()))


def mmss(secs):
    m, s = divmod(secs, 60)
    return f"{m:02d}:{s:02d}"


# -------------------- Pages --------------------
def home_text():
    st.title("📚 Databricks Certification Practice Quizzes")
    st.write(
        "Welcome! This app lets you practice for the Databricks **Data Analyst Associate** exam.\n\n"
        "- Choose a quiz from the **Quiz** page.\n"
        "- You’ll get a **45-minute** timer by default (configurable).\n"
        "- Questions show **one per screen** with a **Prev/Next** flow and a **jump grid**.\n"
        "- Options are **shuffled** each attempt.\n"
        "- After you submit, you’ll see **every question**, your choice, the **correct answer**, and a **detailed explanation**."
    )
    st.info("Head over to the **Quiz** page in the sidebar to start.")


def quiz_selector():
    """Top section of the Quiz page before a quiz has started."""
    st.title("📝 Start a Quiz")
    colA, colB = st.columns([2, 1])
    with colA:
        choice = st.selectbox("Choose a quiz:", list(QUIZ_FILES.keys()), key="quiz_choice")
    with colB:
        duration = st.number_input("Duration (minutes):", min_value=5, max_value=180,
                                   value=DEFAULT_DURATION_MIN, step=5, key="quiz_duration")

    start_col = st.columns([1, 3])[0]
    with start_col:
        if st.button("🚀 Start Quiz", type="primary"):
            quiz = shuffle_quiz(load_quiz(st.session_state.quiz_choice))
            init_state(quiz, st.session_state.quiz_duration)
            st.rerun()


def nav_grid(total, current_idx):
    st.write("#### Questions")
    cols = st.columns(10)
    for i in range(total):
        answered = st.session_state.answers.get(i) is not None
        label = f"{'✅' if answered else '⬜️'} {i+1}"
        btn_type = "primary" if i == current_idx else "secondary"
        if cols[i % 10].button(label, key=f"nav_{i}", type=btn_type, use_container_width=True):
            st.session_state.current_q = i
            st.rerun()


def page_quiz():
    qz = st.session_state.quiz_data
    total = len(qz["questions"])
    idx = st.session_state.current_q
    q = qz["questions"][idx]

    # Timer (auto refresh every second if the helper is installed)
    if AUTOR:
        st_autorefresh(interval=1000, key="tick")
    remaining = secs_left()
    if remaining <= 0 and not st.session_state.submitted:
        st.session_state.submitted = True
        st.rerun()

    header_left, header_right = st.columns([3, 1])
    with header_left:
        st.subheader(f"Question {idx+1} of {total}")
        st.progress((idx + 1) / total)
    with header_right:
        st.metric("⏳ Time Left", mmss(remaining))

    st.divider()
    st.markdown(f"**{q['q']}**")

    # Radio with NO pre-selected option
    wkey = st.session_state.widget_keys[idx]
    current_idx = st.session_state.answers.get(idx)

    if current_idx is None:
        selected_label = st.radio("Select an option:", q["options"], index=None, key=wkey)
    else:
        selected_label = st.radio("Select an option:", q["options"], index=current_idx, key=wkey)

    # Persist selection as index (or None)
    if selected_label is None:
        st.session_state.answers[idx] = None
    else:
        st.session_state.answers[idx] = q["options"].index(selected_label)

    st.divider()

    c1, c2, c3 = st.columns([1, 1, 2])
    with c1:
        st.button("⬅️ Previous", disabled=(idx == 0), on_click=lambda: set_q(idx - 1))
    with c2:
        st.button("Next ➡️", disabled=(idx == total - 1), on_click=lambda: set_q(idx + 1))
    with c3:
        st.button("✅ Submit", type="primary", on_click=lambda: setattr(st.session_state, "submitted", True))

    st.divider()
    nav_grid(total, idx)


def set_q(new_idx):
    total = len(st.session_state.quiz_data["questions"])
    st.session_state.current_q = min(max(new_idx, 0), total - 1)


def page_results():
    qz = st.session_state.quiz_data
    answers = st.session_state.answers
    total = len(qz["questions"])

    # Score
    score = sum(1 for i, q in enumerate(qz["questions"]) if answers.get(i) == q["answer"])
    used_secs = min(
        int((datetime.now() - st.session_state.start_time).total_seconds()),
        int((st.session_state.end_time - st.session_state.start_time).total_seconds()),
    )

    st.title("📊 Results")
    st.write(f"**Score:** {score}/{total}  •  **Percent:** {score/total*100:.2f}%")
    st.write(f"✅ Correct: {score}  |  ❌ Incorrect: {total - score}  |  ⏱ Time Taken: {mmss(used_secs)}")

    st.divider()
    st.subheader("Detailed Review (all questions)")

    # Show every question, user choice, all options (mark correct + your choice), and explanation
    for i, q in enumerate(qz["questions"]):
        sel_idx = answers.get(i)
        correct_idx = q["answer"]
        user_txt = q["options"][sel_idx] if sel_idx is not None else "Not answered"
        correct_txt = q["options"][correct_idx]

        # Status header
        if sel_idx is None:
            st.warning(f"Q{i+1}: Not Answered")
        elif sel_idx == correct_idx:
            st.success(f"Q{i+1}: Correct")
        else:
            st.error(f"Q{i+1}: Incorrect")

        st.markdown(f"**{q['q']}**")

        for j, opt in enumerate(q["options"]):
            tags = []
            if j == correct_idx:
                tags.append("✅ **Correct**")
            if sel_idx is not None and j == sel_idx:
                tags.append("_Your choice_")
            tail = f" — {' • '.join(tags)}" if tags else ""
            st.markdown(f"- {opt}{tail}")

        st.info(f"**Correct answer:** {correct_txt}")
        if sel_idx is not None and sel_idx != correct_idx:
            st.write(f"**Your answer:** {user_txt}")

        if q.get("explanation"):
            st.markdown(f"**Explanation:** {q['explanation']}")

        st.markdown("---")

    # Reset
    if st.button("🏠 Back to Home"):
        for k in ["quiz_data", "answers", "submitted", "start_time", "end_time", "current_q", "widget_keys"]:
            st.session_state.pop(k, None)
        st.rerun()


# -------------------- Router --------------------
def main():
    page = st.sidebar.radio("Navigate", ["Home", "Quiz"])

    if page == "Home":
        home_text()
        return

    # QUIZ PAGE
    # If no quiz in progress/submitted -> show selector (as in your screenshot)
    if "quiz_data" not in st.session_state:
        quiz_selector()
        return

    # If quiz in progress or finished -> show appropriate view
    if not st.session_state.submitted:
        page_quiz()
    else:
        page_results()


if __name__ == "__main__":
    main()
