import cv2
import numpy as np
import streamlit as st
from PIL import Image
import os
from utils.hand_tracking import HandDetector
from utils.ai_solver import solve_math_problem
from dotenv import load_dotenv

# ----------------------- Load API Key -----------------------
load_dotenv()  # Load environment variables from .env
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error("API Key not found! Set GEMINI_API_KEY in your .env file.")
    st.stop()

# ----------------------- Streamlit Page Config -----------------------
st.set_page_config(layout="wide")
# st.image("MathGestures.png", width=700)

# Add Gesture Guidelines Section in a Single Line
st.markdown("""
### ✋ Gesture Guidelines:
🖐 **[1,0,0,0,0]** - Reset | ☝️ **[0,1,0,0,0]** - Draw | ✌️ **[0,1,1,0,0]** - Stop Drawing | ✋ **[0,1,1,1,1]** - Send to AI
""")


col1, col2 = st.columns([3, 2])
with col1:
    run = st.checkbox("Run", value=True)
    FRAME_WINDOW = st.image([])

with col2:
    st.title("Math AI Solver")
    output_text_area = st.empty()

# ----------------------- Initialize Components -----------------------
# Test camera before main loop
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(maxHands=1)
canvas = None
prev_pos = None
output_text = ""

# ----------------------- Helper Functions -----------------------
def get_hand_info(img, detector):
    """Gets hand landmarks and finger positions."""
    hands, img = detector.findHands(img, draw=False, flipType=True)
    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        lmList = hand["lmList"]
        return fingers, lmList
    return None, None

def draw_on_canvas(img, canvas, prev_pos, fingers, lmList):
    """Draws lines or clears canvas based on hand gestures."""
    current_pos = None
    if fingers == [0, 1, 0, 0, 0]:  # Index finger up
        current_pos = lmList[8][:2]
        if prev_pos is None:
            prev_pos = current_pos
        cv2.line(canvas, tuple(current_pos), tuple(prev_pos), (255, 0, 255), 10)
    elif fingers == [1, 0, 0, 0, 0]:  # Thumb up (Clear canvas)
        canvas = np.zeros_like(img)
    return current_pos, canvas

# ----------------------- Main Loop -----------------------
while run:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    if canvas is None:
        canvas = np.zeros_like(img)

    # Process Hand Information
    fingers, lmList = get_hand_info(img, detector)
    if fingers and lmList:
        prev_pos, canvas = draw_on_canvas(img, canvas, prev_pos, fingers, lmList)

        # AI Trigger: Four fingers up
        if fingers == [0, 1, 1, 1, 1]:
            pil_image = Image.fromarray(canvas)
            output_text = solve_math_problem(API_KEY, pil_image)
            output_text_area.text(output_text)

    # Combine Image and Canvas
    image_combined = cv2.addWeighted(img, 0.7, canvas, 0.3, 0)
    FRAME_WINDOW.image(image_combined, channels="BGR")

# Cleanup
cap.release()
cv2.destroyAllWindows()
