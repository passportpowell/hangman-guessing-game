import streamlit as st
import random

# Word categories
categories = {
    "Animals": ["elephant", "giraffe", "kangaroo"],
    "Fruits": ["apple", "banana", "orange"],
    "Tech": ["computer", "python", "docker"]
}

st.title("🧠 Hangman Guessing Game (Streamlit)")

# Choose category
category = st.selectbox("Choose a category", list(categories.keys()))

word = random.choice(categories[category]).lower()
display = ["_"] * len(word)
attempts = st.session_state.get("attempts", 6)
guessed = st.session_state.get("guessed", [])

if "initialized" not in st.session_state:
    st.session_state.initialized = True
    st.session_state.word = word
    st.session_state.display = display
    st.session_state.attempts = attempts
    st.session_state.guessed = guessed

word = st.session_state.word
display = st.session_state.display
attempts = st.session_state.attempts
guessed = st.session_state.guessed

st.write("Word:", " ".join(display))
st.write(f"Attempts Remaining: {attempts}")
st.write("Guessed Letters:", guessed)

if attempts > 0 and "_" in display:
    letter = st.text_input("Guess a letter:", max_chars=1)

    if st.button("Submit"):
        if letter and letter.isalpha():
            letter = letter.lower()
            if letter not in guessed:
                guessed.append(letter)
                if letter not in word:
                    attempts -= 1
                else:
                    for i, c in enumerate(word):
                        if c == letter:
                            display[i] = letter

        st.session_state.guessed = guessed
        st.session_state.display = display
        st.session_state.attempts = attempts

if "_" not in display:
    st.success("🎉 You won!")
elif attempts <= 0:
    st.error(f"😢 Game over! The word was **{word}**. Try again!")
