# **AI Math Gesture Solver ✋➕🤖**

## **Overview**
The **AI Math Gesture Solver** is an interactive application that allows users to **draw mathematical problems using hand gestures** captured via a webcam. The drawn math problem is sent to **Google's Gemini AI** to be solved, and the solution is displayed in real-time.

This project combines the power of:
- **OpenCV** for real-time video capture and image processing.  
- **MediaPipe** for hand gesture detection.  
- **Streamlit** for an interactive and user-friendly interface.  
- **Google Gemini AI** for solving mathematical problems.  

---

## **Features 🚀**

- **Gesture-Based Drawing**: Use hand gestures to draw on a virtual canvas.
- **AI-Powered Solutions**: Send the drawn math problem to Gemini AI for a solution.
- **Interactive UI**: Real-time feedback and visualizations via Streamlit.
- **Clear Gesture Controls**:
  - 🖐 **[1,0,0,0,0]** - **Reset** the canvas.  
  - ☝️ **[0,1,0,0,0]** - Start **drawing**.  
  - ✌️ **[0,1,1,0,0]** - **Stop drawing**.  
  - ✋ **[0,1,1,1,1]** - **Send to AI** to solve the math problem.

---

## **Technologies Used 🛠️**

- **Python 3.8+**
- **OpenCV** - Real-time image and video processing.
- **MediaPipe** - Hand gesture detection.
- **Streamlit** - Web-based user interface.
- **Google Generative AI** (Gemini API) - Math problem solving.
- **Pillow** - Image handling and conversion.

---

## **Project Structure 📂**

```plaintext
AI-Math-Gesture-Solver/
│
├── math_gesture_solver.py      # Main Streamlit application
├── utils/
│   ├── ai_solver.py            # Handles AI communication
│   ├── hand_tracking.py        # Hand gesture detection logic
│
├── MathGestures.png            # Project banner/logo
├── requirements.txt            # Project dependencies
├── .env                        # Environment variables (API key)
└── README.md                   # Project documentation
```

---

## **Setup Instructions 🔧**

### **1. Set Up Environment Variables**
Create a **`.env`** file in the root directory and add your Google API key:

```plaintext
GEMINI_API_KEY=your_google_api_key_here
```

### **2. Install Dependencies**
Install all required libraries using:

```bash
pip install -r requirements.txt
```

### **3. Run the Streamlit Application**
Launch the Streamlit app with the following command:

```bash
streamlit run math_gesture_solver.py
```

---

## **How to Use 🧑‍💻**

1. **Run the Application**: Follow the setup instructions to launch the Streamlit app.
2. **Gesture Guide**: Use the following gestures to interact with the app:
   - 🖐 **[1,0,0,0,0]**: Reset the canvas.  
   - ☝️ **[0,1,0,0,0]**: Start drawing on the canvas.  
   - ✌️ **[0,1,1,0,0]**: Stop drawing.  
   - ✋ **[0,1,1,1,1]**: Send the drawn problem to Gemini AI for solving.  
3. **Real-Time Feedback**: Watch the canvas update as you draw and view the AI's solution on the right panel.

---

## **Example Workflow ✨**

1. Start the application.
2. Use **☝️ [0,1,0,0,0]** to draw a math equation, such as **"2+2"**.
3. Stop drawing using **✌️ [0,1,1,0,0]**.
4. Send the equation to AI using **✋ [0,1,1,1,1]**.
5. The solution will appear instantly on the screen (e.g., **"4"**).

---

## **Dependencies 📦**

The project uses the following libraries:

```
opencv-python
cvzone
numpy
google-generativeai
Pillow
streamlit
python-dotenv
```

Install them with:

```bash
pip install -r requirements.txt
```

---

## **Future Improvements 🛠️**

- Add support for gesture-based **right-click** and **scrolling**.
- Allow for multi-hand drawing.
- Integrate more advanced AI models for solving complex equations.

---
# Math-Gesture-Solver
