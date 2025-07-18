import random
import streamlit as st

def measure_qubit(state):
    """Simulate the measurement of a qubit."""
    if state == '|0⟩':
        return '|0⟩' if random.random() < 1.0 else '|1⟩'
    elif state == '|1⟩':
        return '|1⟩' if random.random() < 1.0 else '|0⟩'
    elif state == 'superposition':
        return '|0⟩' if random.random() < 0.5 else '|1⟩'

st.title("Quantum Guessing Game")
st.write("""
Welcome to the Quantum Guessing Game!  
I have a qubit in a certain state. Try to guess its state after measurement.  
The possible states are `|0⟩` and `|1⟩`.  
Sometimes, the qubit might be in a superposition, so it could be either `|0⟩` or `|1⟩` with equal probability.  
""")

if "state" not in st.session_state:
    st.session_state.state = random.choice(['|0⟩', '|1⟩', 'superposition'])

guess = st.radio("Guess the state after measurement:", options=['|0⟩', '|1⟩'])

if st.button("Measure Qubit"):
    measured_state = measure_qubit(st.session_state.state)
    st.write(f"The qubit was in state **{st.session_state.state}**, and it was measured in state **{measured_state}**.")
    
    if guess == measured_state:
        st.success("Congratulations! You guessed correctly. 🎉")
    else:
        st.error("Sorry, your guess was incorrect. 😢")
    
    st.session_state.state = random.choice(['|0⟩', '|1⟩', 'superposition'])
    st.info("The game has been reset. Try again!")

