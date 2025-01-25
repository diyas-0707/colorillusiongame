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
    return card1_name, card1_color, card2_name, card2_color

# Initialize game state
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.round = 0
    st.session_state.max_rounds = 10
    st.session_state.cards = generate_cards()
    st.session_state.game_over = False

# Function to process answers
def process_answer(is_yes):
    """Check the answer, update the score, and progress to the next round."""
    card1_name, card1_color, card2_name, card2_color = st.session_state.cards
    correct_match = card1_name == card2_color

    # Update the score based on the correctness of the answer
    if (is_yes and correct_match) or (not is_yes and not correct_match):
        st.session_state.score += 1

    # Progress to the next round or end the game
    st.session_state.round += 1
    if st.session_state.round < st.session_state.max_rounds:
        st.session_state.cards = generate_cards()
    else:
        st.session_state.game_over = True

# Display the game interface
st.title("Color Matching Game")
st.write("Does the name of the color on Card 1 match the color of Card 2?")

if not st.session_state.game_over:
    # Display current round and score
    st.write(f"Round: {st.session_state.round + 1}/{st.session_state.max_rounds}")
    st.write(f"Score: {st.session_state.score}")

    # Retrieve current cards
    card1_name, card1_color, card2_name, card2_color = st.session_state.cards

    # Display the cards
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

    # Buttons for user input
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Yes", key=f"yes_button_{st.session_state.round}"):
            process_answer(True)
            st.rerun()  # Force rerender to go to the next round immediately

    with col2:
        if st.button("No", key=f"no_button_{st.session_state.round}"):
            process_answer(False)
            st.rerun()  # Force rerender to go to the next round immediately

else:
    # Display results at the end of the game
    st.markdown(f"## Game Over! 🎉 Your final score is **{st.session_state.score}/{st.session_state.max_rounds}**.")
