import streamlit as st
import random

# List of colors to choose from
COLORS = ["red", "blue", "green", "yellow", "purple", "orange"]

# Function to generate a new round of cards
def generate_cards():
    card1_name = random.choice(COLORS)
    card1_color = random.choice(COLORS)
    card2_name = random.choice(COLORS)
    card2_color = random.choice(COLORS)
    return (card1_name, card1_color, card2_name, card2_color)

# Initialize game state
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.round = 0
    st.session_state.max_rounds = 10
    st.session_state.cards = generate_cards()

# Display the game interface
st.title("Color Matching Game")
st.write("Does the color name on Card 1 match the text color on Card 2?")
st.write(f"Round: {st.session_state.round + 1}/{st.session_state.max_rounds}")

# Display the cards
card1_name, card1_color, card2_name, card2_color = st.session_state.cards

st.markdown(
    f'<p style="font-size:24px; font-weight:bold; color:{card1_color};">'
    f"Card 1: {card1_name}</p>",
    unsafe_allow_html=True,
)

st.markdown(
    f'<p style="font-size:24px; font-weight:bold; color:{card2_color};">'
    f"Card 2: {card2_name}</p>",
    unsafe_allow_html=True,
)

# Game logic
def next_round(is_yes):
    if (card1_name == card2_color and is_yes) or (card1_name != card2_color and not is_yes):
        st.session_state.score += 1

    st.session_state.round += 1
    if st.session_state.round < st.session_state.max_rounds:
        st.session_state.cards = generate_cards()
    else:
        st.session_state.game_over = True

# Buttons for user input
col1, col2 = st.columns(2)

with col1:
    if st.button("Yes"):
        next_round(True)

with col2:
    if st.button("No"):
        next_round(False)

# Display results or progress
if "game_over" in st.session_state and st.session_state.game_over:
    st.markdown(f"## Game Over! Your final score is {st.session_state.score}/{st.session_state.max_rounds}")
    if st.button("Play Again"):
        st.session_state.score = 0
        st.session_state.round = 0
        st.session_state.cards = generate_cards()
        st.session_state.game_over = False
else:
    st.markdown(f"Score: {st.session_state.score}")