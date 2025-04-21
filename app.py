#streamlit
import streamlit as st

st.set_page_config(page_title="growth mindset project", project_icon="✭")
st.title("Growth Mindset Challenge: Web App with streamlit")

st.header("🗝️ WellcOm tOo YoUr GrOwth jOurney 🗝️!")
st.write("Embark on this growth journey with passion and purpose, letting each moment fuel your dreams")

#quote section
st.header("【Today's Growth Mindset Quote】")
st.write("Success is not final, failure is not fatal: it is the courage to continue that counts._Winston Churchill")


st.header(" What's Your Challenge Today?")
user_input=st.text_input("Describe a challenge you're facing:")

 #condition
if user_input:
          st.success(f"You're facing: {user_input}. Keep pushing forward towords your goal!")

else:
          st.warning("Tell us about your challenge to get started!")

 #reflexing
st.header(" Reflect on Your Learning")
reflection = st.text_area("Write your reflections here:")

if reflection:
         st.success(f"🌟Great Insight! Your reflection: {reflection}")

else:
     st.info("Reflecting on past experience help you grow! Share your difficulties")

#acheivements
st.header(" ! Celebrate Your Wins!")
acheivment = st.text_input("Share something you've recently accomplished:")

if acheivment:
        st.success (f"💫 Amazing! You achieved: {acheivment}")

else:
       st.info("Big or small, every acheivement counts! Share one now 😊")



#footer
st.write("- - -")
st.write("keep believing in yourself. Growth is a journey, not a destination!🌞")
st.write("💖🔴 Created By Sejal Khan💖")











