import streamlit as st

# Functions for the calculator
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Title of the app
st.title("Simple Calculator")

# User input for operation selection
operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide"])

# User input for numbers
num1 = st.number_input("Enter first number:")
num2 = st.number_input("Enter second number:")

# Calculate result based on the selected operation
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)

    st.write(f"Result: {result}")
