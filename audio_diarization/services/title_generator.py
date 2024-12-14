import google.generativeai as genai
from django.conf import settings


genai.configure(api_key=settings.API_KEY)

def generate_blog_title(content: str) -> str:
    """
    Generates a creative, short, SEO-friendly blog title using the Gemini Pro model.

    Args:
        content (str): Blog content for which the title needs to be generated.

    Returns:
        str: Generated blog title.
    """
    if not content.strip():
        raise ValueError("Content cannot be empty.")
    
    # Prepare the prompt
    input_prompt = f"Generate a creative, short, SEO-friendly blog title for the following content:\n\n{content}\n\nTitle:"
    
    try:
        # Generating the title using Gemini Pro
        model = genai.GenerativeModel("gemini-pro") 
        response = model.generate_content(input_prompt)
        return response.text.strip()
    except Exception as e:
        raise RuntimeError(f"Error generating blog title: {str(e)}")
