

import streamlit as st
import random
import importlib
import copy
from datetime import datetime, timedelta

# Optional smooth 1s timer updates
try:
    from streamlit_autorefresh import st_autorefresh
    AUTOR = True
except Exception:
    AUTOR = False

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="Databricks Certification Practice Quizzes", layout="wide", page_icon="🧪")

# ---------- GLOBAL, SAFE CSS (small + reliable) ----------
# --- Polished sticky app-bar with center tabs (no emojis) ---
# --- App-bar with centered, pill-style tabs + live clock ---
# --- Full-width AMGEN-style app bar (clean, bigger, evenly spaced) ---
st.markdown("""
<style>
:root{
  --bg:#0b0f1a; --panel:#0f141c; --ink:#e9eef9; --muted:#9aa6bd;
  --stroke:#242a36; --accent:#ff6b6b; --accent2:#6aa6ff;
}

/* content width */
.block-container{ max-width:1200px; padding-top:1rem; }

/* Full-bleed bar wrapper (stretches beyond container) */
.appbar-wrap{
  position: sticky; top:0; z-index:60;
  margin-left: calc(-50vw + 50%); margin-right: calc(-50vw + 50%);
  width: 100vw;
  backdrop-filter: blur(8px);
  border-bottom:1px solid var(--stroke);
  background: linear-gradient(180deg, rgba(19,25,36,.92), rgba(16,22,32,.86));
  box-shadow: 0 8px 30px rgba(0,0,0,.35);
}

/* Inner row (centers to page width) */
.appbar-inner{
  max-width:1200px; margin:0 auto;
  padding: 18px 18px 8px 18px;   /* taller than before */
  display:flex; align-items:center; gap:16px;
}

/* Brand (left) */
.brand{
  font-size:28px; font-weight:900; letter-spacing:.2px; line-height:1;
  color:var(--ink);
}
.brand-sub{ color:var(--muted); font-size:13px; margin-top:4px; }

/* Middle nav: evenly spaced across available space */
.nav-center{
  flex:1;
  display:flex; justify-content:space-evenly; align-items:center;
}

/* Tabs: text buttons with underline for active */
.navtab .stButton>button{
  background: transparent !important; color: var(--ink) !important;
  border: 1px solid rgba(255,255,255,0) !important;
  padding: .55rem 1.1rem; border-radius: 10px; font-weight: 800;
}
.navtab .stButton>button:hover{
  background: rgba(255,255,255,.04) !important;
  border-color: rgba(255,255,255,.06) !important;
}
.navtab.active .stButton>button{
  background: transparent !important;
  box-shadow: inset 0 -3px 0 0 var(--accent);     /* underline */
}

/* Right side chips */
.right{
  display:flex; align-items:center; gap:8px;
}
.chip{
  display:inline-flex; align-items:center; gap:.45rem;
  color:var(--ink); font-weight:700; font-size:12.5px;
  background:#172034; border:1px solid #2b3343; border-radius:999px;
  padding:.34rem .7rem;
}

/* Keep your quiz UI styling */
.q-card{ border:1px solid #2a2f3b; border-radius:12px; padding:16px; background:#121722; }
.q-title{ font-weight:700; font-size:1.05rem; }
.navbtn .stButton>button{ width:100%; border-radius:10px; background:#1c2330 !important; color:#dbe7ff !important; border:1px solid #2a2f3b; padding:.4rem 0; }
.navbtn.current .stButton>button{ background:#262c40 !important; border-color:#3b4670; }
.navbtn.answered .stButton>button{ background:#15261a !important; border-color:#224a2d; color:#bff0c9 !important; }
</style>
""", unsafe_allow_html=True)




# -------------------- QUIZ REGISTRY --------------------
QUIZ_FILES = {
    "Quiz 2": "quizzes.quiz2",
    "Quiz 3": "quizzes.quiz3",
    "Quiz 4": "quizzes.quiz4",
}

QUIZ_CATALOG = {
    "Quiz 2": {
        "subtitle": "Section 2 · Data Management",
        "blurb": "Delta Lake, managed vs unmanaged, views, permissions, PII, and troubleshooting.",
        "default_minutes": 60
    },
    "Quiz 3": {
        "subtitle": "Databricks SQL – Full Practice",
        "blurb": "Dashboards, warehouses, Partner Connect, medallion layers, streaming caveats.",
        "default_minutes": 60
    },
    "Quiz 4": {
        "subtitle": "Delta Lake – Concepts & History",
        "blurb": "ACID, time travel, _delta_log, global temp views, VACUUM/OPTIMIZE and security.",
        "default_minutes": 60
    },
}

DEFAULT_DURATION_MIN = 60

# -------------------- HELPERS --------------------
def load_quiz(key):
    module = importlib.import_module(QUIZ_FILES[key])
    quiz = copy.deepcopy(module.quiz)
    for q in quiz["questions"]:
        if "answer_text" not in q and "answer" in q:
            q["answer_text"] = q["options"][q["answer"]]
    return quiz

def shuffle_quiz(quiz):
    for q in quiz["questions"]:
        correct = q["answer_text"]
        random.shuffle(q["options"])
        q["answer"] = q["options"].index(correct)
    return quiz

def init_state(quiz, duration_min=DEFAULT_DURATION_MIN):
    st.session_state.quiz_data = quiz
    st.session_state.start_time = datetime.now()
    st.session_state.end_time = st.session_state.start_time + timedelta(minutes=duration_min)
    st.session_state.current_q = 0
    st.session_state.submitted = False
    st.session_state.answers = {i: None for i in range(len(quiz["questions"]))}
    st.session_state.widget_keys = {i: f"q_{i}_{random.randint(1,10**9)}" for i in range(len(quiz["questions"]))}

def secs_left():
    if "end_time" not in st.session_state: return 0
    return max(0, int((st.session_state.end_time - datetime.now()).total_seconds()))

def fmt_mmss(s):
    m, s = divmod(s, 60)
    return f"{m:02d}:{s:02d}"

def go(i):
    total = len(st.session_state.quiz_data["questions"])
    st.session_state.current_q = min(max(i, 0), total-1)

# -------------------- NAVBAR --------------------
def render_navbar():
    # keep current page in state
    if "page" not in st.session_state:
        st.session_state.page = "Home"
    cur = st.session_state.page

    # live date/time
    if AUTOR: st_autorefresh(interval=1000, key="clock")
    now = datetime.now()
    date_str = now.strftime("%a, %d %b")
    time_str = now.strftime("%H:%M:%S")

    # full-bleed app bar
    with st.container():
        st.markdown('<div class="appbar-wrap"><div class="appbar-inner">', unsafe_allow_html=True)

        # LEFT — brand
        left, mid, right = st.columns([1.2, 2.6, 1.2], vertical_alignment="center")
        with left:
            st.markdown('<div class="brand">DBX Quizzes</div>', unsafe_allow_html=True)
            # If you want a subtitle line, uncomment:
            # st.markdown('<div class="brand-sub">Databricks Certification Practice</div>', unsafe_allow_html=True)

        # CENTER — evenly spaced tabs
        with mid:
            c1, c2, c3, c4 = st.columns([1,1,1,1], vertical_alignment="center")
            with c1:
                cls = "navtab active" if cur == "Home" else "navtab"
                st.markdown(f'<div class="{cls}">', unsafe_allow_html=True)
                if st.button("Home", key="nav_home"): st.session_state.page = "Home"; st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)
            with c2:
                cls = "navtab active" if cur == "Study" else "navtab"
                st.markdown(f'<div class="{cls}">', unsafe_allow_html=True)
                if st.button("Management" if False else "Study", key="nav_study"):  # rename if you want
                    st.session_state.page = "Study"; st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)
            with c3:
                cls = "navtab active" if cur == "Quiz" else "navtab"
                st.markdown(f'<div class="{cls}">', unsafe_allow_html=True)
                if st.button("QA Runner" if False else "Quiz", key="nav_quiz"):
                    st.session_state.page = "Quiz"; st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)
            with c4:
                cls = "navtab active" if cur == "Help" else "navtab"
                st.markdown(f'<div class="{cls}">', unsafe_allow_html=True)
                if st.button("Help", key="nav_help"): st.session_state.page = "Help"; st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)

        # RIGHT — date & time chips (you can add mini status here)
        with right:
            st.markdown('<div class="right">', unsafe_allow_html=True)
            st.markdown(f'<div class="chip">{date_str}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="chip">{time_str}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('</div></div>', unsafe_allow_html=True)


# -------------------- PAGES --------------------
def page_home():
    st.markdown("## ✨ Databricks Certification Practice Quizzes")
    st.write(
        "Sharpen your Databricks **Data Analyst Associate** skills. "
        "Pick a quiz, beat the timer, and get detailed explanations after you submit."
    )
    st.markdown("""
- Questions show **one per screen** with **Prev/Next** + a quick **jump grid**  
- **Options shuffle** every attempt  
- **No preselected answers**  
- **Live timer** (configurable)  
- **Results view** shows your pick, the correct answer, and a clear explanation
    """)

def page_study():
    st.title("📘 Study")
    st.info("This section is reserved for notes, links, and study guides. (Coming soon)")

def page_help():
    st.title("❓ Help")
    st.write("**How it works**")
    st.markdown("""
- Go to **Quiz** and pick a test.
- One question per screen; use **Prev/Next** or **Quick Jump**.
- Timer counts down; there are **no preselected options**.
- After submitting, you’ll see your answer vs the **correct** one and a full **explanation**.
    """)

def page_quiz_selector():
    # Styled header with bottom spacing
    st.markdown("""
    <style>
      /* Outer container card */
      .outer-quiz-card{
        border:1px solid #2a2f3b; border-radius:16px; padding:18px 18px 8px 18px;
        background:#11161f; box-shadow:0 6px 22px rgba(0,0,0,.25); margin-bottom:18px;
      }
      /* Inner quiz tiles */
      .quizgrid{ margin-top:.4rem; }
      .quizcard{
        border:1px solid #2a2f3b; border-radius:14px; padding:14px; background:#151a23;
        box-shadow: 0 4px 18px rgba(0,0,0,.22);
        height:100%; display:flex; flex-direction:column; gap:.35rem;
      }
      .quizcard h3{ margin:.1rem 0 .3rem 0; font-size:1.1rem; }
      .quizmeta{ color:#a6b0c3; font-size:.9rem; }
      .pill{ display:inline-block; padding:.12rem .5rem; border:1px solid #2a2f3b; border-radius:999px; font-size:.8rem; margin-right:.35rem; color:#cdd6f4; }
    </style>
    <div class="outer-quiz-card">
      <h2 style="margin:0 0 .2rem 0;">📝 Available Quizzes</h2>
      <p style="color:#a6b0c3;margin:.15rem 0 .6rem 0;">Pick a quiz below. You can adjust the duration per quiz before starting.</p>
    </div>
    """, unsafe_allow_html=True)

    names = list(QUIZ_FILES.keys())
    cols = st.columns(3, gap="large")

    for i, name in enumerate(names):
        with cols[i % 3]:
            with st.container(border=True):
                # Load quiz to get question count
                mod = importlib.import_module(QUIZ_FILES[name])
                quiz_obj = getattr(mod, "quiz")
                total_qs = len(quiz_obj["questions"])

                meta = QUIZ_CATALOG.get(name, {})
                subtitle = meta.get("subtitle", "")
                blurb = meta.get("blurb", "")
                default_minutes = int(meta.get("default_minutes", DEFAULT_DURATION_MIN))

                st.subheader(name)
                if subtitle: st.caption(subtitle)
                if blurb: st.write(blurb)

                st.write(f"**{total_qs} questions** · **{default_minutes} min** · Options shuffle")

                dur = st.number_input(
                    "Duration (minutes):",
                    min_value=5, max_value=180,
                    value=default_minutes, step=5,
                    key=f"dur_{name}"
                )
                start = st.button("🚀 Start", key=f"start_{name}", use_container_width=True)
                if start:
                    quiz = copy.deepcopy(quiz_obj)
                    quiz = shuffle_quiz(quiz)
                    init_state(quiz, int(dur))
                    st.rerun()

def page_quiz():
    qz = st.session_state.quiz_data
    total = len(qz["questions"])
    idx = st.session_state.current_q
    q = qz["questions"][idx]

    if AUTOR: st_autorefresh(interval=1000, key="tick")
    remaining = secs_left()
    if remaining <= 0 and not st.session_state.submitted:
        st.session_state.submitted = True
        st.rerun()

    left, right = st.columns([3,1])
    with left:
        st.markdown(f"### Question {idx+1} of {total}")
        st.progress((idx+1)/total)
    with right:
        st.markdown(f'<span class="chip">⏳ {fmt_mmss(remaining)}</span>', unsafe_allow_html=True)

    st.markdown('<div class="q-card">', unsafe_allow_html=True)
    st.markdown(f'<div class="q-title">{q["q"]}</div>', unsafe_allow_html=True)

    wkey = st.session_state.widget_keys[idx]
    cur_idx = st.session_state.answers.get(idx)
    if cur_idx is None:
        selected_label = st.radio(" ", q["options"], index=None, key=wkey, label_visibility="collapsed")
    else:
        selected_label = st.radio(" ", q["options"], index=cur_idx, key=wkey, label_visibility="collapsed")

    if selected_label is None:
        st.session_state.answers[idx] = None
    else:
        st.session_state.answers[idx] = q["options"].index(selected_label)

    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")
    c1, c2, c3 = st.columns([1,1,2])
    with c1: st.button("⬅️ Previous", disabled=(idx==0), on_click=lambda: go(idx-1))
    with c2: st.button("Next ➡️", disabled=(idx==total-1), on_click=lambda: go(idx+1))
    with c3: st.button("✅ Submit", type="primary", on_click=lambda: setattr(st.session_state, "submitted", True))

    st.write("")
    st.markdown("#### Quick Jump")
    rows = st.columns(10)
    for i in range(total):
        answered = st.session_state.answers.get(i) is not None
        klass = "navbtn answered" if answered else "navbtn"
        if i == idx: klass += " current"
        with rows[i % 10]:
            st.markdown(f'<div class="{klass}">', unsafe_allow_html=True)
            st.button(f'{"✅" if answered else "⬜️"} {i+1}', key=f"nav_{i}", use_container_width=True, on_click=lambda j=i: go(j))
            st.markdown('</div>', unsafe_allow_html=True)

def page_results():
    qz = st.session_state.quiz_data
    answers = st.session_state.answers
    total = len(qz["questions"])
    score = sum(1 for i, q in enumerate(qz["questions"]) if answers.get(i) == q["answer"])

    used = min(
        int((datetime.now()-st.session_state.start_time).total_seconds()),
        int((st.session_state.end_time-st.session_state.start_time).total_seconds())
    )

    with st.container():
        st.markdown("## 📊 Results")
        st.write(f"**Score:** {score}/{total}  •  **Percent:** {score/total*100:.2f}%")
        st.write(f"✅ Correct: {score}  |  ❌ Incorrect: {total-score}  |  ⏱ Time Taken: {fmt_mmss(used)}")

    st.write("")
    st.markdown("### Detailed Review")
    for i, q in enumerate(qz["questions"]):
        sel_idx = answers.get(i)
        correct_idx = q["answer"]
        user_txt = q["options"][sel_idx] if sel_idx is not None else "Not answered"
        correct_txt = q["options"][correct_idx]

        if sel_idx is None:
            st.warning(f"Q{i+1}: Not Answered")
        elif sel_idx == correct_idx:
            st.success(f"Q{i+1}: Correct")
        else:
            st.error(f"Q{i+1}: Incorrect")

        st.markdown(f"**{q['q']}**")
        for j, opt in enumerate(q["options"]):
            tags = []
            if j == correct_idx: tags.append("✅ **Correct**")
            if sel_idx is not None and j == sel_idx: tags.append("_Your choice_")
            st.markdown(f"- {opt}{' — ' + ' • '.join(tags) if tags else ''}")

        st.info(f"**Correct answer:** {correct_txt}")
        if sel_idx is not None and sel_idx != correct_idx:
            st.write(f"**Your answer:** {user_txt}")
        if q.get("explanation"):
            st.markdown(f"**Explanation:** {q['explanation']}")
        st.markdown("---")

    if st.button("🏠 Back to Home"):
        for k in ["quiz_data","answers","submitted","start_time","end_time","current_q","widget_keys"]:
            st.session_state.pop(k, None)
        st.session_state.page = "Home"
        st.rerun()

# -------------------- ROUTER --------------------
def main():
    render_navbar()  # New AMGEN-style navbar

    page = st.session_state.get("page", "Home")

    if page == "Home":
        page_home()
        return

    if page == "Study":
        page_study()
        return

    if page == "Help":
        page_help()
        return

    # Quiz section
    if "quiz_data" not in st.session_state:
        page_quiz_selector()
        return

    if not st.session_state.submitted:
        page_quiz()
    else:
        page_results()



if __name__ == "__main__":
    main()
