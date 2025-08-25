import streamlit as st
from app.main import MusicLLM
from app.utils import *
from io import BytesIO
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="MusicLLm", page_icon=":musical_note:", layout="centered")
st.title("MusicLLm :musical_note:")
st.markdown("Generate music from text prompts using LLM")

music_input = st.text_input("Enter a music theme or idea")
style_input = st.selectbox("Choose a music style", ["Classical", "Jazz", "Rock", "Pop", "Blues", "Electronic", "Romantic"])

if st.button("Generate Music") and music_input:
    generator = MusicLLM()

    with st.spinner("Generating melody..."):
        melody = generator.generate_melody(music_input)
        harmony = generator.generate_harmony(melody)
        rhythm = generator.generate_rhythm(melody)

        composition = generator.adapt_style(style_input, melody, harmony, rhythm)

        melody_notes = melody.split()
        melody_freqs = note_to_frequencies(melody_notes)

        harmony_chords = harmony.split()
        harmony_notes = []
        for chord in harmony_chords:
            harmony_notes.extend(chord.split('-'))

        harmony_freqs = note_to_frequencies(harmony_notes)

        all_freqs = melody_freqs + harmony_freqs

        wav_bytes = generate_wav_bytes_from_notes_freq(all_freqs)

    st.audio(BytesIO(wav_bytes), format="audio/wav")

    st.success("Music generation complete!")

    with st.expander("View Composition Details"):
        st.text(composition)