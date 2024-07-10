import google.generativeai as genai

# Configure the Generative AI with your API key
genai.configure(api_key="AIzaSyCF8LRXPCW6HnNqSMdut-PQqek4nruTpvE")

def upload_to_gemini(path, mime_type=None):
    """Uploads a file to Gemini."""
    file = genai.upload_file(path, mime_type=mime_type)
    return file

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 100000,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

def detect_objects_in_image(filepath):
    """Detects objects in an image using Generative AI."""
    gemini_file = upload_to_gemini(filepath, mime_type="image/jpeg")

    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [gemini_file],
            },
        ]
    )

    response = chat_session.send_message(
        "Analyze the image and detect objects. Provide the output in JSON format."
    )

    return response.text  # Assuming response.text is already in JSON format


