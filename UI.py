import streamlit as st
import pandas as pd
import joblib
import numpy as np

model = joblib.load("study_time_predictor.pkl")

st.set_page_config(page_title="AI Exam Planner", layout="centered")

st.markdown("""
    <div style="text-align: center;">
        <img src="https://i0.wp.com/yourdream.liveyourdream.org/wp-content/uploads/2017/06/venus-williams-believe-in-yourself.png?resize=580%2C580&ssl=1" 
             width="250"/>
        <p style="font-size: 18px; font-style: italic;">Plan Smart. Study Smarter.</p>
    </div>
""", unsafe_allow_html=True)

st.title("📅 AI Exam Planner")

st.markdown("""
    <style>
    .stApp {
        background-color: #e6ffee;
    }
    </style>
""", unsafe_allow_html=True)

st.subheader("✨ Plan your study schedule smartly before exams!")
st.markdown("Helps you divide your study time based on **subject importance and available hours.**")
st.markdown("---")

a = st.slider("📚 Select number of subjects", 1, 15, 1)
subjects = []

st.markdown("## 📝 Enter Subject Details")

all_filled = True

for i in range(a):
    st.markdown(f"#### Subject {i + 1}")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input(f"📘 Name of subject {i + 1}", key=f"name_{i}")
    with col2:
        credit = st.number_input(f"🏷️ Credit/Importance", min_value=1, value=1, key=f"credit_{i}")
    if name.strip() != "":
        subjects.append({"name": name, "credit": credit})
    else:
        all_filled = False
        st.warning(f"⚠️ Subject {i + 1} name cannot be empty!")

st.markdown("---")

total_study_time = st.number_input("⏰ Enter total available study time (in hours)", min_value=1)

if all_filled and len(subjects) == a:
    study_inputs = []
    show_warning = False

    st.markdown("### 📥 Enter Inputs per Subject")

    for i, subj in enumerate(subjects):
        st.markdown(f"#### 🧠 {subj['name']}")
        col1, col2, col3 = st.columns(3)
        with col1:
            past_score = st.slider(f"Past Score for {subj['name']}", 0, 100, 75, key=f"score_{i}")
        with col2:
            difficulty = st.slider(f"Difficulty (1=Easy, 5=Hard)", 1, 5, 3, key=f"diff_{i}")
        with col3:
            trend = st.selectbox("Performance Trend", ["Improving", "Same", "Declining"], key=f"trend_{i}")
            trend_value = {"Improving": 1, "Same": 0, "Declining": -1}[trend]

        study_inputs.append({
            "Subject": subj['name'],
            "Past Score": past_score,
            "Difficulty": difficulty,
            "Trend": trend,
            "Trend Value": trend_value,
        })

    if st.button("📊 Generate AI Study Plan", key="final_generate_plan"):
        st.success("✅ All inputs entered successfully!")

        study_plan = []
        total_raw_prediction = 0

        for entry in study_inputs:
            input_features = np.array([
                [entry['Past Score'], entry['Difficulty'], entry['Trend Value'], total_study_time]
            ])
            predicted_time = model.predict(input_features)[0]
            predicted_time = max(1, round(predicted_time, 2))
            total_raw_prediction += predicted_time

            study_plan.append({
                "Subject": entry['Subject'],
                "Past Score": entry['Past Score'],
                "Difficulty": entry['Difficulty'],
                "Trend": entry['Trend'],
                "Raw Predicted Time": predicted_time
            })

        for row in study_plan:
            normalized_time = (row["Raw Predicted Time"] / total_raw_prediction) * total_study_time
            row["Predicted Study Time (hrs)"] = round(normalized_time, 2)
            del row["Raw Predicted Time"]  # clean up

        df = pd.DataFrame(study_plan)

        styled_html = df.style.set_table_styles(
            [
                {'selector': 'thead th',
                 'props': [('background-color', '#f2f2f2'), ('font-weight', 'bold'), ('text-align', 'center')]},
                {'selector': 'tbody td', 'props': [('text-align', 'center')]},
            ]
        ).set_properties(**{
            'background-color': '#ffffff',
            'color': '#333333',
            'border': '1px solid #ccc',
            'padding': '8px',
            'font-size': '16px',
            'text-align': 'center'
        }).hide(axis='index').to_html()

        centered_html = f"""
        <div style="display: flex; justify-content: center;">
            <div>
                {styled_html}
        """

        st.markdown("### 🤖 AI-Generated Study Plan")
        st.markdown(centered_html, unsafe_allow_html=True)
