import streamlit as st
import random
import time

# Streamlit app title
st.title("💰 Money Making Machine 💰")

# Initialize session state for user balance
if "balance" not in st.session_state:
    st.session_state.balance = 0  # Starting balance

# Function to generate random money
def generate_money():
    return random.randint(10, 500)  # Random money between $10 and $500

# Create a money generator section
st.subheader("🎰 Click to Make Money")
if st.button("Generate Money"):
    st.write("Generating money... 💸")
    time.sleep(2)  # Simulate waiting time
    earned_money = generate_money()
    st.session_state.balance += earned_money  # Update balance
    st.success(f"🎉 You made ${earned_money}! Your total balance is now ${st.session_state.balance}.")

# Show current balance
st.subheader(f"💵 Your Total Balance: ${st.session_state.balance}")

# Leaderboard (Top money makers)
st.subheader("🏆 Top Earners (Fake leaderboard)")
top_earners = {
    "Alice": 5000,
    "Bob": 3500,
    "Charlie": 4200,
    "You": st.session_state.balance  # Add user's current balance
}
sorted_earners = sorted(top_earners.items(), key=lambda x: x[1], reverse=True)

# Display leaderboard
for rank, (name, amount) in enumerate(sorted_earners, start=1):
    st.write(f"🥇 {rank}. {name} - ${amount}")

# Motivation section
st.subheader("💡 Money-Making Motivation")
quotes = [
    "Money grows on the tree of persistence! 🌱",
    "You have to see it before you achieve it! 💰",
    "Hustle until your haters ask if you're hiring! 🚀",
]
st.info(random.choice(quotes))  # Show a random quote
