import streamlit as st

st.set_page_config(page_title="Growth Mindset Project", project_icon="✨")
st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("'*•.¸♡ Welcome to your Growth Journey! ♡¸.•*'")
st.write("Your journey toward progress and self-improvement has begun! Each new day brings fresh opportunities and a chance to learn. Small improvements lead to big changes—just keep moving forward with determination, passion, and a positive mindset. 🚀✨")

#Quote Section
st.header("Todays Growth Mindset Quote")
st.write("Be not afraid of growing slowly ═........═ be afraid only of standing still. 'Famouse Chinese Poverb'")
st.write("Translation:- Aahista barhne se mat ghabrao »--•--« sirf ruk jaane se daro. 'Mashhoor Chinese Kahawat'")

st.header("⌚ Whats Your Challenge Today ?")
user_input = st.text_input("Describe a challenge you are facing today!")


# Condition
if user_input:
    st.success(f"🌟 You are facing: {user_input}.\n💡 Remember, every challenge is an opportunity to grow. 💪 Stay strong, keep learning, and never give up! 🚀")
else:
    st.warning("Tell us about your Challenge to get started!")

# Reflaxing
st.header("Reflect on Your Journey")  
reflection = st.text_area("Write your outcome/reflection of your project here.")  

if reflection:  
    st.success(f"🌟 Great insight! Your reflection: {reflection}\n💭 Self-reflection is the key to continuous growth. Keep learning and evolving! 🚀")  
else:  
    st.info("🔍 Reflecting on your past experiences helps you grow! ✨ Take a moment to analyze your challenges and celebrate your progress. 💡")  


# Acheivment
st.header("Celebrate your Wins!")
achievement = st.text(f"Please share something you have accomplished.")

if achievement:
    st.success(f"🏆 Wow! You achieved: {achievement}\n🌟 Every step forward is a victory. Keep pushing and celebrating your progress! 🚀")
else:
    st.info("🎯 Big or small, every achievement counts! 🌱 Take a moment to recognize your progress and share your success. 💪")


# Footer
st.write("- - -")  
st.write("🌱 Keep believing in yourself. Growth is a journey, not a destination! 🚀")  
st.write("✨ Stay consistent, stay motivated, and keep pushing forward! 💡")  
st.write("📌 Created by **Muhammad Kashif Hanif** © 2025")  
