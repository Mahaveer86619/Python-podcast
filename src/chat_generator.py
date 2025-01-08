import google.generativeai as genai
from src.config import GEMINI_API_KEY
from typing import TypedDict

class ChatMessage(TypedDict):
    speaker: str 
    text: str 

genai.configure(api_key=GEMINI_API_KEY)

def generate_podcast_script(pdf_path):
    """
    Generate a conversation script between host and guest using Gemini AI.
    Args:
        context (str): The extracted text from the PDF to be used as context.
        num_turns (int): The number of exchanges between host and guest in the conversation.
        stream (bool): Whether to stream the conversation or not.
    Returns:
        str: Generated conversation script as JSON or None if an error occurs.
    """

    # Upload the PDF file
    try:
        uploaded_pdf = genai.upload_file(pdf_path)
        # file_name = uploaded_pdf.name
        # print(file_name + " uploaded to Gemini")
    except Exception as e:
        print(f"Error uploading PDF to Gemini: {e}")
        return None
    
    prompt = f''' 
Instructions:

Generate a conversation between a Host and an Expert. The conversation should be relevant to the provided Context.

The Host should:
- Greet the Expert and start topics by asking questions.
- Introduce and incorporate perspectives from a third party into the Expert's responses.
- Provide commentary or transitions between topics.
The conversation should alternate between the Host and the Expert.
Use the following to make the conversation more engaging:
- Add three dots “ … ” to create a longer pause. 
- Add the filler words “um” and “uh” if required. 
- Try to have shorter sentences to improve pronunciation.
    '''

    model = genai.GenerativeModel("gemini-1.5-flash")

    try:

        response = model.generate_content(
            [prompt, uploaded_pdf], 
            generation_config=genai.GenerationConfig(
                max_output_tokens=1000,
                temperature=0.1,
                response_mime_type="application/json", 
                response_schema=list[ChatMessage]
            )
        )
            
        # Return the conversation as a JSON response
        return clean_and_parse_json(response.text.strip())

    except Exception as e:
        print(f"Error generating conversation: {e}")
        return None

def clean_and_parse_json(json_str: str) -> list[ChatMessage]:
  """
  Cleans and parses a JSON string containing a list of ChatMessages.

  Args:
    json_str: The JSON string to clean and parse.

  Returns:
    A list of ChatMessage objects.
  """

  # Parse the cleaned JSON string
  try:
    chat_messages = eval(json_str) 
  except Exception as e:
    print(f"Error parsing JSON: {e}")
    return [] 

  return chat_messages