import streamlit as st
import random
import matplotlib.pyplot as plt

st.set_page_config(page_title="Quantum Guessing Game", layout="centered")
st.title("Quantum Guessing Game")

if "state" not in st.session_state:
    st.session_state.state = random.choice(['|0⟩', '|1⟩', 'superposition'])
if "score" not in st.session_state:
    st.session_state.score = 0
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "history" not in st.session_state:
    st.session_state.history = []

guess = st.radio("Guess the qubit state will collapse to:", ['0', '1'])

def measure_qubit(state):
    if state == '|0⟩':
        return '0'
    elif state == '|1⟩':
        return '1'
    elif state == 'superposition':
        return random.choice(['0', '1'])

if st.button("Measure Qubit"):
    measured_state = measure_qubit(st.session_state.state)
    correct = guess == measured_state

    st.write(f"Qubit state: **{st.session_state.state}**, measured as **{measured_state}**.")

    if correct:
        st.success("✅ Correct guess!")
        st.session_state.score += 1
    else:
        st.error("❌ Incorrect guess.")

    st.session_state.attempts += 1
    st.session_state.history.append(correct)

    st.write(f"**Score:** {st.session_state.score} / {st.session_state.attempts}")

    st.session_state.state = random.choice(['|0⟩', '|1⟩', 'superposition'])

st.subheader("Auto Simulation")

def auto_simulate(n):
    correct = 0
    for _ in range(n):
        state = random.choice(['|0⟩', '|1⟩', 'superposition'])
        measured = measure_qubit(state)
        if guess == measured:
            correct += 1
    return correct

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Run 10 Times"):
        correct = auto_simulate(10)
        st.info(f"✅ {correct}/10 correct → {correct * 10}% chance")
with col2:
    if st.button("Run 50 Times"):
        correct = auto_simulate(50)
        st.info(f"✅ {correct}/50 correct → {correct * 2}% chance")
with col3:
    if st.button("Run 100 Times"):
        correct = auto_simulate(100)
        st.info(f"✅ {correct}/100 correct → {correct}% chance")

if st.session_state.history:
    st.subheader("Your Guessing Performance")
    correct = st.session_state.history.count(True)
    incorrect = st.session_state.history.count(False)

    fig, ax = plt.subplots()
    ax.bar(["Correct", "Incorrect"], [correct, incorrect], color=["green", "red"])
    ax.set_ylabel("Count")
    ax.set_title("Guessing Accuracy")
    st.pyplot(fig)
