import streamlit as st
from api_calling import note_generator
from google import genai
from dotenv import load_dotenv
import os
from PIL import Image

# load the environment variable
load_dotenv()

my_api_key = os.environ.get('GEMINI_API_KEY')

# initializing a client
client = genai.Client(api_key=my_api_key)


images = st.file_uploader(
    'Upload the photos of your notes',
    type=['jpg', 'png', 'jpeg'],
    accept_multiple_files=True
)

print(f"*******{type(images)}*******")


if images:
    # pil_images = Image.open(images)
    pil_images = [Image.open(x) for x in images]

    promt = """Summarize the picture in note format at max 100 words,
      make sure to add necessary markdown to differentiate different section"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[pil_images, promt]
    )

    st.text(response.text)