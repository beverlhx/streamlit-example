import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import chess
import chess.svg

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



def play_chess():
    st.title("Simple Chess Game")
    board = chess.Board()

    while not board.is_game_over():
        st.write("Current board:")
        st.image(chess.svg.board(board=board))

        move_input = st.text_input("Enter your move (e.g., e2e4):")
        if st.button("Make Move"):
            try:
                move = chess.Move.from_uci(move_input)
                if move in board.legal_moves:
                    board.push(move)
                else:
                    st.warning("Invalid move! Try again.")
            except ValueError:
                st.warning("Invalid move format! Use UCI notation (e.g., e2e4).")

    st.write("Game Over!")
    st.write("Result:", board.result())
