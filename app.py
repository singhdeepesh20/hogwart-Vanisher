
import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="Hogwarts Vanisher 🏰", layout="wide")


page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://i.ibb.co/QvhndRG5/series-harry-potter-ron-weasley-hermione.jpg");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    background-repeat: no-repeat;
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
[data-testid="stToolbar"] {
    right: 2rem;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)


page = st.sidebar.radio("🧭 Navigate", ["🏰 Welcome", "📸 Magic Cloak Demo"])




if page == "🏰 Welcome":
    st.markdown(
        "<h1 style='text-align: center; color: white; text-shadow: 2px 2px 6px black;'>🪄 Hogwarts Vanisher 🏰</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<h3 style='text-align: center; color: white; text-shadow: 1px 1px 4px black;'>Step into the world of magic — become invisible like Harry Potter with the legendary cloak!</h3>",
        unsafe_allow_html=True
    )

    st.markdown("### ✨ Instructions")
    st.markdown("""
    1. Go to **Magic Cloak Demo** page from sidebar.  
    2. First, capture the **background** (without you in the frame).  
    3. Next, capture yourself with a **white cloth/cloak**.  
    4. Watch yourself vanish — just like in Hogwarts!  
    """)

   






elif page == "📸 Magic Cloak Demo":
    st.title("📸 Hogwarts Vanisher – Magic Cloak Demo")

    if "background" not in st.session_state:
        st.session_state.background = None


    st.subheader("Step 1: Capture Background (Empty)")
    bg_file = st.camera_input("Stand out of frame and capture background")

    if st.button("Save Background"):
        if bg_file is None:
            st.error("⚠️ No photo taken. Please capture the background first.")
        else:
            bg_img = Image.open(bg_file).convert("RGB")
            bg = cv2.cvtColor(np.array(bg_img), cv2.COLOR_RGB2BGR)
            st.session_state.background = bg
            st.success("✅ Background saved!")


    st.subheader("Step 2: Capture Cloak Photo")
    cloak_file = st.camera_input("Step into frame with the cloak")

    if cloak_file is not None and st.session_state.background is None:
        st.info("ℹ️ You need to save the background first before cloak photo.")


    if cloak_file is not None and st.session_state.background is not None:
        cloak_img = Image.open(cloak_file).convert("RGB")
        frame = cv2.cvtColor(np.array(cloak_img), cv2.COLOR_RGB2BGR)


        bg = st.session_state.background
        if (bg.shape[1], bg.shape[0]) != (frame.shape[1], frame.shape[0]):
            bg = cv2.resize(bg, (frame.shape[1], frame.shape[0]))


        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_white = np.array([0, 0, 200])
        upper_white = np.array([180, 40, 255])
        mask = cv2.inRange(hsv, lower_white, upper_white)

        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
        mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel, iterations=1)

        mask_inv = cv2.bitwise_not(mask)
        cloak_area = cv2.bitwise_and(bg, bg, mask=mask)
        rest = cv2.bitwise_and(frame, frame, mask=mask_inv)
        final = cv2.add(cloak_area, rest)

        st.subheader("✨ Vanished Result")
        st.image(cv2.cvtColor(final, cv2.COLOR_BGR2RGB), use_container_width=True)


    if st.button("Clear Background"):
        st.session_state.background = None
        st.experimental_rerun()

