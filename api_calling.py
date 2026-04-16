from google import genai
from dotenv import load_dotenv
import os
from gtts import gTTS
import io


# load the environment variable
load_dotenv()

my_api_key = os.environ.get('GEMINI_API_KEY')

# initializing a client
client = genai.Client(api_key=my_api_key)

# note generation 
def note_generator(images):

    promt = """Summarize the picture in note format at max 100 words,
      make sure to add necessary markdown to differentiate different section"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images, promt]
    )

    return response.text


def audio_transcription(text):
    speech = gTTS(text=text, lang='en', slow=False)

    # allocate some memory
    audio_buffer = io.BytesIO()

    speech.write_to_fp(audio_buffer)

    return audio_buffer


def quiz_generator(images, difficulty):
    promt = f"Generate 3 quizzes based on the {difficulty}. Make sure to add markdown to add markdown to differentiate the options. Add correct answer too after generating the quizzes."
    
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images, promt]
    )

    return response.text