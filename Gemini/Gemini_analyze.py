import json
import re
import google.generativeai as genai

# Load API key from json file
api_key_path = r'C:\Users\Tyler\Documents\.CodingMinds\EthanBookCapture\Gemini\api_key.json'
with open(api_key_path) as f:
    api_key = json.load(f)["api_key"]

genai.configure(api_key=api_key)


def load_text_from_file(text_file_path):
    """Loads text from a given file."""
    with open(text_file_path, 'rb') as file:
        text = file.read().decode('utf-8', errors='ignore')
    return text


def clean_text(text):
    """Clean and preprocess the text."""
    # Remove non-standard characters and excessive whitespace
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)  # Remove non-ASCII characters
    text = re.sub(r'\s+', ' ', text)  # Replace multiple whitespace with a single space
    text = text.strip()
    return text


def analyze_text_with_gemini(text, analysis_type):
    """Analyze the text using Google Gemini."""
    model = create_gemini_model("gemini-1.5-flash")
    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [{"text": text}],
            },
        ]
    )

    prompt = ""

    if analysis_type == "summarize":
        prompt = f"Please summarize the following text: \n\n{text}"
    elif analysis_type == "translate":
        prompt = f"Please translate the following text to French: \n\n{text}"
    elif analysis_type == "explain":
        prompt = f"Please explain the following text: \n\n{text}"
    elif analysis_type == "contextualize":
        prompt = f"Please provide context for the following text: \n\n{text}"

    response = chat_session.send_message(prompt)
    return response.text.strip()


def create_gemini_model(model_name):
    # Create the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name=model_name,
        generation_config=generation_config,
    )
    return model


if __name__ == "__main__":
    # Use the correct path for the file on your local system
    text_file_path = r'C:\Users\Tyler\Documents\.CodingMinds\EthanBookCapture\Gemini\extracted_text_from_images.txt'
    text = load_text_from_file(text_file_path)

    # Print the loaded text for debugging
    print(f"Original Loaded Text:\n{text}\n")

    # Clean the text before analysis
    cleaned_text = clean_text(text)

    # Print the cleaned text for debugging
    print(f"Cleaned Text:\n{cleaned_text}\n")

    # Choose the type of analysis
    analysis_type = "summarize"  # Change to "translate", "explain", or "contextualize" as needed

    analyzed_text = analyze_text_with_gemini(cleaned_text, analysis_type)
    print(f"Analyzed Text ({analysis_type}):\n{analyzed_text}\n")

    # Optionally, save the analyzed text to a file
    output_file_path = r'C:\Users\Tyler\Documents\.CodingMinds\EthanBookCapture\Gemini\analyzed_text_output.txt'
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(f"{analysis_type.capitalize()} Output:\n{analyzed_text}\n")

    print(f"Analysis result saved to {output_file_path}")
