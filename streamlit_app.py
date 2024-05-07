import altair as alt
import numpy as np
import pandas as pd
import streamlit as st


"""
# Welcome to the world of awesome software engineers!
"""

num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

indices = np.linspace(0, 1, num_points)
theta = 2 * np.pi * num_turns * indices
radius = indices

x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(num_points),
})

st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))


def check_winner(board):
    # Check rows, columns, and diagonals for a win
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != ' ':
            return board[row][0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def display_board(board):
    for row in board:
        st.write(" | ".join(row))
        st.write("-" * 9)

def play_tic_tac_toe():
    st.title("Tic-Tac-Toe Game")
    board = np.array([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])
    player = 'X'

    while True:
        st.write("Current board:")
        display_board(board)

        move_input = st.text_input(f"Player {player}, enter your move (e.g., 1 2 for row 1, column 2):")
        if st.button("Make Move"):
            try:
                row, col = map(int, move_input.split())
                if board[row-1][col-1] == ' ':
                    board[row-1][col-1] = player
                    winner = check_winner(board)
                    if winner:
                        st.success(f"Player {winner} wins!")
                        break
                    elif ' ' not in board:
                        st.warning("It's a draw!")
                        break
                    else:
                        player = 'O' if player == 'X' else 'X'
                else:
                    st.warning("Invalid move! Position already taken.")
            except ValueError:
                st.warning("Invalid move format! Use row and column numbers (e.g., 1 2).")

play_tic_tac_toe()
