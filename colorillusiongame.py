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
    st.session_state.game_over = False

# Display the game interface
st.title("Color Matching Game")

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

    # Game logic
    def process_answer(is_yes):
        """Check the answer, update the score, and progress to the next round."""
        correct_match = card1_name == card2_color
        if (is_yes and correct_match) or (not is_yes and not correct_match):
            st.session_state.score += 1  # Increment score for correct answer

        st.session_state.round += 1  # Move to the next round
        if st.session_state.round < st.session_state.max_rounds:
            st.session_state.cards = generate_cards()  # Generate new cards
        else:
            st.session_state.game_over = True

    # Buttons for user input
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Yes", key=f"yes_button_{st.session_state.round}"):
            process_answer(True)

    with col2:
        if st.button("No", key=f"no_button_{st.session_state.round}"):
            process_answer(False)

# Display results at the end of the game
if st.session_state.game_over:
    st.markdown(f"## Game Over! 🎉 Your final score is **{st.session_state.score}/{st.session_state.max_rounds}**.")
    # Clear UI for the final round
    st.stop()