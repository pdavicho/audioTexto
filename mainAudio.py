import streamlit as st
import speech_recognition as sr

def transcribe_audio(audio_file_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as source:
        st.subheader("Procesando audio...")
        audio = recognizer.record(source)

        try:
            st.subheader("Realizando la transcripción...")
            text = recognizer.recognize_google(audio, language="es-ES")
            st.subheader("Texto transcrito:")
            st.caption(text)
        except sr.UnknownValueError:
            st.text("No se pudo entender el audio.")
        except sr.RequestError as e:
            st.text(f"Error en la solicitud a Google Speech Recognition: {e}")

def main():
    st.title("Transcriptor de Audio con Streamlit")
    
    uploaded_file = st.file_uploader("Cargar archivo de audio", type=["wav", "mp3"])

    transcribir = st.button("Transcribir")

    if transcribir:
        if uploaded_file is not None:
            st.audio(uploaded_file, format="audio/wav")
            transcribe_audio(uploaded_file)
    else:
        st.warning('Subir archivo de audio')

if __name__ == "__main__":
    main()
