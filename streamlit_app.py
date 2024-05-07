import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import random

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



st.title("Guess the Number Game")
number_to_guess = random.randint(1, 100)
attempts = 0
feedback = ""
st.write(number_to_guess)

while True:
    user_guess = st.number_input("Enter your guess (between 1 and 100)", min_value=1, max_value=100)
    if st.button("Submit Guess"):
        attempts += 1
        if user_guess < number_to_guess:
            feedback = "Too low! Try a higher number."
        elif user_guess > number_to_guess:
            feedback = "Too high! Try a lower number."
        else:
            feedback = f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts."
            st.success(feedback)
            break

    st.write(feedback)

