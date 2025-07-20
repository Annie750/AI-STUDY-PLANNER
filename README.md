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
<img width="677" height="455" alt="image" src="https://github.com/user-attachments/assets/06391332-b1ee-470e-84fb-7dc44c1be377" />
<img width="557" height="692" alt="image" src="https://github.com/user-attachments/assets/26b3cdc9-0134-43ee-b58d-32e622fae1e7" />
<img width="535" height="726" alt="image" src="https://github.com/user-attachments/assets/eda89f46-1131-490a-a0f5-e53b6a0b793b" />
<img width="532" height="312" alt="image" src="https://github.com/user-attachments/assets/b94fd0e0-37f1-4465-8b23-e96db0063251" />
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

🔐 License & Usage
This project is NOT open-source for reuse.
The code is shared for portfolio and educational showcase only.

✨ Credits
Made with ❤️ by Ananya
3rd Year B.Tech CSE (AI & ML)
Currently interning at NIC | AI Project Developer | Curious Creator

