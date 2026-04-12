import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="TrainSmart", page_icon="💪", layout="centered",
                   initial_sidebar_state="collapsed")

# Light background styling
st.markdown("""
<style>
    .stApp { background-color: #f8fafb; }
    .stButton > button { background-color: #16a34a; color: white; border: none;
        border-radius: 8px; padding: 0.6rem 2rem; font-size: 16px; font-weight: 500; }
    .stButton > button:hover { background-color: #15803d; color: white; }
    h1 { color: #14532d; }
    h3 { color: #166534; }
</style>
""", unsafe_allow_html=True)

st.title("💪 TrainSmart")
st.subheader("Your AI-powered personal trainer")
st.markdown("---")

# ── User Info Form ──────────────────────────────────────────
st.markdown("### Tell us about yourself")

col1, col2 = st.columns(2)
with col1:
    age = st.number_input("Age", min_value=10, max_value=80, value=20)
    weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=70)
    height = st.number_input("Height (cm)", min_value=100, max_value=250, value=170)

with col2:
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    goal = st.selectbox("Fitness Goal", [
        "Lose weight",
        "Build muscle",
        "Improve stamina",
        "Stay fit and healthy",
        "Gain weight"
    ])
    activity = st.selectbox("Activity Level", [
        "Sedentary (little or no exercise)",
        "Lightly active (1-3 days/week)",
        "Moderately active (3-5 days/week)",
        "Very active (6-7 days/week)"
    ])

st.markdown("### Diet Preferences")
col3, col4 = st.columns(2)
with col3:
    diet_type = st.selectbox("Diet Type", [
        "Vegetarian",
        "Non-Vegetarian",
        "Eggetarian (Veg + Eggs)",
        "Vegan"
    ])
with col4:
    indian_meals = st.selectbox("Meal Style", [
        "Indian meals preferred 🇮🇳",
        "Mix of Indian and Western",
        "No preference"
    ])

st.markdown("---")

# ── BMI Calculator ───────────────────────────────────────────
height_m = height / 100
bmi = round(weight / (height_m ** 2), 1)

if bmi < 18.5:
    bmi_category = "Underweight"
    bmi_color = "warning"
elif bmi < 25:
    bmi_category = "Normal weight"
    bmi_color = "success"
elif bmi < 30:
    bmi_category = "Overweight"
    bmi_color = "warning"
else:
    bmi_category = "Obese"
    bmi_color = "error"

st.markdown("### Your BMI")
col1, col2 = st.columns(2)
with col1:
    st.metric("BMI Score", bmi)
with col2:
    if bmi_color == "success":
        st.success(f"✅ {bmi_category}")
    elif bmi_color == "warning":
        st.warning(f"⚠️ {bmi_category}")
    else:
        st.error(f"❌ {bmi_category}")

st.markdown("---")

# ── Generate Plans ───────────────────────────────────────────
if st.button("🚀 Generate My Personal Plan"):

    user_info = f"""
    Age: {age}
    Gender: {gender}
    Weight: {weight} kg
    Height: {height} cm
    BMI: {bmi} ({bmi_category})
    Fitness Goal: {goal}
    Activity Level: {activity}
    Diet Type: {diet_type}
    Meal Style: {indian_meals}
    """

    # Diet Plan
    st.markdown("### 🥗 Your Weekly Diet Plan")
    with st.spinner("Generating your diet plan..."):
        diet_response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{
                "role": "user",
                "content": f"""
                Create a detailed 7-day diet plan for this person:
                {user_info}

                IMPORTANT dietary rules:
                - Diet type is {diet_type} — strictly follow this. Do NOT suggest any foods that go against this.
                - If vegetarian or vegan, absolutely NO meat, fish or seafood like salmon, chicken, eggs etc.
                - Meal style preference: {indian_meals} — if Indian meals preferred, use Indian foods like dal, roti,
                  rice, sabzi, paneer, curd, poha, idli, upma, rajma, chana etc. Use Indian meal names.
                - Keep ingredients affordable and easily available in India.

                Format it clearly with:
                - Each day (Monday to Sunday)
                - Breakfast, Lunch, Dinner and Snacks for each day
                - Include approximate calories for each meal
                - Make it practical and specific to their fitness goal
                - Add a short motivational tip at the end
                Keep it friendly and encouraging.
                """
            }]
        )
        diet_plan = diet_response.choices[0].message.content
        st.markdown(diet_plan)

    st.markdown("---")

    # Workout Plan
    st.markdown("### 🏋️ Your Weekly Workout Plan")
    with st.spinner("Generating your workout plan..."):
        workout_response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{
                "role": "user",
                "content": f"""
                Create a detailed 7-day workout plan for this person:
                {user_info}

                Format it clearly with:
                - Each day (Monday to Sunday)
                - Exercise name, sets, reps/duration for each exercise
                - Include rest days appropriately
                - Warm up and cool down suggestions
                - Make it beginner-friendly if activity level is low
                - Add a motivational tip at the end
                Keep it practical and specific to their goal.
                """
            }]
        )
        workout_plan = workout_response.choices[0].message.content
        st.markdown(workout_plan)

    st.markdown("---")

    # Download button
    full_plan = f"# TrainSmart — Your Personal Plan\n\n## Your Info\n{user_info}\n\n## Diet Plan\n{diet_plan}\n\n## Workout Plan\n{workout_plan}"
    st.download_button(
        label="📥 Download My Full Plan",
        data=full_plan,
        file_name="trainsmart_plan.txt",
        mime="text/plain"
    )

st.markdown("---")
st.caption("Built by Paras Parashar · TrainSmart v1.0 · Powered by LLaMA 3.3")