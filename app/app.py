import streamlit as st
from datetime import datetime
import math

st.set_page_config(page_title="All-in-One Calculator", layout="centered")

st.title("🧮 All-in-One Calculator")

mode = st.selectbox("Select Mode", ["Basic", "Scientific", "Age Calculator"])

# Basic Calculator
if mode == "Basic":
    num1 = st.number_input("Enter first number:")
    operation = st.selectbox("Operation", ["+", "-", "*", "/"])
    num2 = st.number_input("Enter second number:")

    if st.button("Calculate"):
        if operation == "+":
            st.success(f"Result: {num1 + num2}")
        elif operation == "-":
            st.success(f"Result: {num1 - num2}")
        elif operation == "*":
            st.success(f"Result: {num1 * num2}")
        elif operation == "/":
            if num2 != 0:
                st.success(f"Result: {num1 / num2}")
            else:
                st.error("Cannot divide by zero!")

# Scientific Calculator
elif mode == "Scientific":
    func = st.selectbox("Select Function", ["sin", "cos", "tan", "log", "sqrt", "exp"])
    value = st.number_input("Enter value:")

    if st.button("Compute"):
        try:
            result = {
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
                "log": math.log,
                "sqrt": math.sqrt,
                "exp": math.exp
            }[func](value)
            st.success(f"{func}({value}) = {result}")
        except ValueError:
            st.error("Invalid input for selected function.")

# Age Calculator
elif mode == "Age Calculator":
    birth_date = st.date_input("Enter your birth date")
    now = datetime.now()
    bdate = datetime.combine(birth_date, datetime.min.time())
    diff = now - bdate

    years = diff.days // 365
    months = (diff.days % 365) // 30
    days = diff.days
    hours = diff.total_seconds() // 3600
    minutes = diff.total_seconds() // 60
    seconds = diff.total_seconds()

    st.subheader("📊 Your Age in Different Units:")
    st.write(f"Years: {years}")
    st.write(f"Months: {months}")
    st.write(f"Days: {days}")
    st.write(f"Hours: {int(hours)}")
    st.write(f"Minutes: {int(minutes)}")
    st.write(f"Seconds: {int(seconds)}")

# HTML Custom Calculator (Advanced UI)
with st.expander("🔬 Open Advanced UI Calculator"):
    with open("templates/calculator.html", "r") as f:
        html_code = f.read()
    with open("static/style.css", "r") as f:
        css_code = f"<style>{f.read()}</style>"
    with open("static/script.js", "r") as f:
        js_code = f"<script>{f.read()}</script>"

    st.components.v1.html(css_code + html_code + js_code, height=550)
