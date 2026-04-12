# 💪 TrainSmart — AI Personal Trainer

> An AI-powered fitness web app that generates personalised weekly diet plans and workout routines based on your body stats, fitness goals and Indian food preferences.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-412991?style=for-the-badge&logoColor=white)
![LLaMA](https://img.shields.io/badge/LLaMA_3.3-0467DF?style=for-the-badge&logoColor=white)

---

## 🌟 Features

- 🥗 **AI Diet Plan Generator** — Personalised 7-day meal plan with calories for each meal
- 🏋️ **AI Workout Plan Generator** — 7-day workout routine with sets, reps and rest days
- 🇮🇳 **Indian Meal Support** — Suggests Indian foods like dal, roti, paneer, poha, idli, rajma etc.
- 🥦 **Diet Type Filter** — Vegetarian, Non-Vegetarian, Eggetarian, Vegan — strictly followed
- 📊 **BMI Calculator** — Instant BMI score with health category
- 📥 **Download Your Plan** — Save your full diet + workout plan as a text file
- ⚡ **Powered by LLaMA 3.3** — Fast, accurate AI responses via Groq API

---

## 🖥️ Screenshots

> Fill in your stats → Choose your diet preference → Get your full personalised plan instantly

---

## 🚀 How to Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/pparashar073/TrainSmart.git
cd TrainSmart
```

### 2. Install dependencies
```bash
pip install streamlit groq python-dotenv
```

### 3. Get a free Groq API key
- Go to [console.groq.com](https://console.groq.com)
- Sign up and create an API key

### 4. Create a `.env` file
```
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Run the app
```bash
streamlit run app.py
```

---

## 🛠️ Tech Stack

| Tech | Purpose |
|---|---|
| Python | Core language |
| Streamlit | Web UI framework |
| Groq API | AI inference engine |
| LLaMA 3.3 70B | Language model for plan generation |
| python-dotenv | Environment variable management |

---

## 📋 How It Works

1. User enters their age, weight, height, gender, fitness goal and activity level
2. User selects diet type (Veg/Non-Veg/Eggetarian/Vegan) and meal style preference
3. App calculates BMI instantly
4. On clicking Generate, two separate AI calls are made to LLaMA 3.3 via Groq
5. A personalised 7-day diet plan and workout plan are generated and displayed
6. User can download the full plan as a text file

---

## 🔮 Upcoming Features (Phase 2)

- 📸 **AI Exercise Form Checker** — Upload a photo of your exercise and get form feedback
- 📈 **Workout Logger** — Track your daily workouts and streaks
- 🔔 **Smart Reminders** — Notifications for meals and workouts

---

## 👨‍💻 Built By

**Paras Parashar** — B.Tech CS/AI Student  
[GitHub](https://github.com/pparashar073) · [LinkedIn](https://linkedin.com/in/paras-parashar-a0b947346)

---

> *TrainSmart v2.0 — Because your fitness plan should be as unique as you are* 💪
