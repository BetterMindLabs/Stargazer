import streamlit as st
from PIL import Image
import google.generativeai as genai

# ============ Gemini Setup ============
genai.configure(api_key=st.secrets["API_KEY"])
model = genai.GenerativeModel("gemini-2.5-flash")

# ============ Streamlit UI ============
st.title("🔭 SkyBuddy AI — Citizen Scientist Stargazer App")
st.write("Upload your night sky image, and let AI identify stars, planets, and events!")

uploaded_image = st.file_uploader("Upload a sky photo (JPG, PNG)", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Sky Image", use_column_width=True)

    prompt = """
You are an expert astronomer AI. Analyze this night sky image and identify visible celestial objects (e.g., planets, bright stars, constellations).
Suggest upcoming celestial events the user might be able to see, and provide educational tips for amateur astronomers.
If the image is unclear, explain what to look for when taking a better sky photo.
"""

    analyze_button = st.button("🔍 Analyze Sky Image")

    if analyze_button:
        with st.spinner("Analyzing your sky photo with Gemini..."):
            response = model.generate_content([prompt, image])
            ai_result = response.text

        st.subheader("🌟 AI Analysis & Suggestions")
        st.markdown(ai_result)

# Optional: Fun event tips even without image
st.sidebar.header("⭐ Upcoming Events")
st.sidebar.markdown("""
- 🌑 **New Moon** — Great for deep-sky viewing!
- ☄️ **Perseid Meteor Shower** — Peaks August 12–13.
- 🌕 **Full Moon** — July 21.
- 🔭 **International Observe the Moon Night** — September 15.
""")
