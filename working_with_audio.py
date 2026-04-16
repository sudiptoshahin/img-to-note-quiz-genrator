from gtts import gTTS
import streamlit as st
import io

text = "Hello, Welcome to this course"

speech = gTTS(text=text, lang='en', slow=False)
# speech.save('welcome.mp3')

# allocate some memory
audio_buffer = io.BytesIO()

speech.write_to_fp(audio_buffer)

st.audio(audio_buffer)