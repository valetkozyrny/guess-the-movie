import streamlit as st
import random
from utilits.loader import load_movies
from game.movie import Movie

movies_df = load_movies("data/IMDb_movies/Top_1000_IMDb_movies_New_version.csv")

if "current_movie" not in st.session_state:
    random_movie_data = random.choice(movies_df)
    st.session_state.current_movie = Movie(random_movie_data)

if "score" not in st.session_state:
    st.session_state.score = 0

if "show_next_button" not in st.session_state:
    st.session_state.show_next_button = False

if "guess_input_value" not in st.session_state:
    st.session_state.guess_input_value = ""

movie = st.session_state.current_movie

st.title("🎬 Guess the Movie!")
st.write("Description of the film:")
st.write(movie.show_desc())


def update_guess_value():
    st.session_state.guess_input_value = st.session_state.guess_input


user_guess = st.text_input(
    "Your guess:",
    key="guess_input",
    value=st.session_state.guess_input_value,
    on_change=update_guess_value
)

if st.button("Check"):
    if movie.check_guess(st.session_state.guess_input_value):
        st.success("✅ That's correct! Нажмите 'Next' для продолжения.")
        st.session_state.score += 1
        st.session_state.show_next_button = True

    else:
        st.error("❌ Wrong! Try again.")
        st.session_state.score = 0
        st.session_state.show_next_button = False


if st.session_state.show_next_button:
    if st.button("Next movie ➡️"):
        random_movie_data = random.choice(movies_df)
        st.session_state.current_movie = Movie(random_movie_data)
        st.session_state.guess_input_value = ""
        st.session_state.show_next_button = False
        st.rerun()


if st.button("Skipping a move. Your correct answer counter will be reset."):
    random_movie_data = random.choice(movies_df)
    st.session_state.current_movie = Movie(random_movie_data)
    st.session_state.score = 0
    st.session_state.show_next_button = False

    st.session_state.guess_input_value = ""

    st.rerun()

st.write(f"✅ Counter of correct answers: {st.session_state.score}")

st.image("C:/Users/zzzha/Downloads/IMDB_Logo_2016.svg.png", caption="From IMDb's rating it was create)", width=300)