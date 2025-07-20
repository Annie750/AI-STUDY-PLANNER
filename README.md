# AI-STUDY-PLANNER
Smart study planner using machine learning to predict study hours and generate personalized schedules based on subject importance, difficulty, and past scores.

# 📅 AI Exam Planner — *Plan Smart. Study Smarter.*

An AI-powered study planner that helps students **optimize their exam preparation** by intelligently distributing study hours across subjects based on:
- 📘 Subject Importance (Credits)
- 📈 Past Scores
- 🎯 Difficulty Level
- 📉 Performance Trend

Built with 💡 Streamlit + 🧠 Machine Learning (Linear Regression)

---

## 🚀 Features
- 🎓 Personalized study plan for each subject
- 🧠 Predicts ideal study hours using AI
- 🎨 Clean, interactive Streamlit UI
- ✅ Supports multiple subjects and performance profiles
- 📊 Visualizes your AI-generated plan beautifully

---

## 🖼️ Preview
![Screenshot](https://i.imgur.com/your-placeholder.png)  
*Mockup: AI-generated study plan for a 5-subject exam week.*

---

## 🔧 Tech Stack
| Tool          | Purpose                          |
|---------------|----------------------------------|
| Python        | Core logic & ML model            |
| Streamlit     | Web interface                    |
| Scikit-learn  | Linear regression model          |
| Pandas/Numpy  | Data handling                    |
| Joblib        | Model serialization              |

---

## 🧪 How It Works (AI Logic)
The model uses:
- Low past scores → more study hours
- High difficulty subjects → more study hours
- Declining trends → extra study buffer
- Total available time → normalized allocation

Example formula used during training *(simplified)*:
study_time = f(past_score, difficulty, trend, total_time)

*Note: Model training code and `.pkl` file are withheld for IP protection.*

