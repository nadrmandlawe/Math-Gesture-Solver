import google.generativeai as genai

def solve_math_problem(api_key, image):
    """
    Sends the image of a math problem to the Gemini AI model and retrieves the solution.

    Parameters:
    - api_key (str): Gemini API Key.
    - image (PIL.Image): Image containing the math problem.

    Returns:
    - str: AI-generated solution or an error message.
    """
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(["Solve this math problem", image])
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
