import streamlit as st
import requests
from datetime import date

# Base URL for backend API
BASE_URL = "http://localhost:8000"

# To check if the user already exists
def check_user_exists(email):
    response = requests.get(f"{BASE_URL}/user/exists", params={"email": email})  # ✅ Correct
    return response.status_code == 200 and response.json().get("exists", False)

# ------------------- UI Entry Point ------------------- #
def main():
    st.title("Welcome to 🌻 Laxmi Bank App")

    if "page" not in st.session_state:
        st.session_state.page = "home"

    if st.session_state.page == "home":
        st.subheader("Please choose an option")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Register"):
                st.session_state.page = "register"
        with col2:
            if st.button("Login"):
                st.session_state.page = "login"

    if st.session_state.page == "register":
        register_form()

    elif st.session_state.page == "login":
        login_form()

# ------------------- Register Form ------------------- #
def register_form():
    st.header("User Registration Form")

    with st.form("registration_form"):
        name = st.text_input("Full Name")
        date_of_birth = st.date_input("Date of Birth",min_value=date(1900, 1, 1),max_value=date.today(),value=date(2000, 1, 1))
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        phone_number = st.text_input("Phone Number")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        city = st.text_input("City")
        state = st.text_input("State")
        country = st.text_input("Country")
        submit = st.form_submit_button("Submit Registration")

    if submit:
        if password != confirm_password:
            st.error("Passwords do not match. Please try again.")
            return

        # Check if user already exists
        if check_user_exists(email):
            st.error("User already exists. Please login.")
            if st.button("Go to Login"):
                st.session_state.page = "login"
            return

        # Send registration data to backend
        payload = {
            "name": name,
            "date_of_birth": str(date_of_birth),
            "gender": gender,
            "phone_number": phone_number,
            "email": email,
            "password": password,
            "city": city,
            "state": state,
            "country": country
        }

        try:
            res = requests.post(f"{BASE_URL}/user/register", json=payload)
            if res.status_code == 200 or res.status_code == 201:
                st.success("Registration Successful! Redirecting to login page...")
                st.session_state.page = "login"
                st.rerun()
            else:
                st.error(res.json().get("detail", "Registration failed."))
        except Exception as e:
            st.error(f"An error occurred: {e}")

# ------------------- Login Placeholder ------------------- #

def login_form():
    st.header("User Login")

    # Login form layout
    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

    if submit:
        # Prepare request payload
        payload = {
            "email": email,
            "password": password
        }

        try:
            # Send POST request to login endpoint
            res = requests.post(f"{BASE_URL}/auth/login", json=payload)

            # Success: Show welcome message and save user in session
            if res.status_code == 200:
                user_data = res.json()

                # Debugging: view full response structure
                st.write("Login response:", user_data)

                # Safely extract user's name or email
                user_name = user_data.get("name") or user_data.get("email") or "User"

                st.success(f"Welcome, {user_name}!")

                # Store user data in session
                st.session_state.user = user_data

                # Navigate to dashboard
                st.session_state.page = "dashboard"
                st.rerun()

            # Handle login error
            else:
                st.error(res.json().get("detail", "Invalid credentials."))
        
        except Exception as e:
            st.error(f"An error occurred during login: {e}")

# ------------------- Run App ------------------- #
if __name__ == "__main__":
    main()
