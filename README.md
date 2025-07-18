Update: 
- Added Auto Simulate
- Added a chart
- Added a counter
- Added a reset button



A simple python code to simulate superpositions when measured

Try it out: [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://quantumguessinggame-djfhzkhuo8ewgb4rexc8wx.streamlit.app/)

How to play:

The game will randomly prepare a qubit in three possible states: |0>, |1>, or superposition.

You will be asked to guess the state of the qubit after measurement. Your guess can be either |0> or |1>.

After the qubit is measured. The outcome depends on the inital state:

If its |0>, it'll always be 0.

If its |1>, it'll always be 1.

If its superposition, it has a 50% chance of being measured as |1> or |0>.


Code explanation:

measure_qubit(state): This function simulates the measurement of a qubit. It uses random probabilities to simulate the measurement outcome.

quantum_game(): This is the main game function. It runs the game loop, asks for user input, and displays the result based on the measurement outcome.

This project is licensed under the MIT License.
