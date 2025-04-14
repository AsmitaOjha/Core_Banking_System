import streamlit as st
import requests
from datetime import date

#base url for backend api
BASE_URL = "http://localhost:8000"

#to check if the user already exists
def check_user_exists(email):
    response = requests.get(f"{BASE_URL}/users/{email}")
    return response.status_code == 200 and response.json().get("exists", False)

#-------------------------------UI Entry Point---------------------------#
def main():
    st.title("Welcome to Laxmi🌻Bank App")

    if "page " not in st.session_state:
        st.session_state.page = "home"

    if st.session_state.page == "home":
        st.subhead("Please choose an option")
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

#--------------------------Register Form----------------------------

def register_form():
    st.header("User Registration Form")

    name = st.text_input("Full Name")
    date_of_birth = st.date_input("Date of Birth", max_value= date.today())
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    phone_number = st.text_input("Phone Number")
    email = st.text_input("Email")
    password = st.text_input("Passowrd", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    city = st.text_input("City")
    state = st.text_input("State")
    country = st.text_input("Country")

    if st.button("Submit Registration"):
        if password != confirm_password:
            st.error("Passwords do not match. Please try again.")
            return
        
        #check if user already exists
        if check_user_exists(email):
            st.error("User already exists. Please login,")
            if st.button("login"):
                st.session_state.page = "login"
            return
        
    #send registration data to backend
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
        res = requests.post(f"{BASE_URL}/users", json=payload)
        if res.status_code == 200:
            st.success("Regisration Successful! Please login.")
            if st.button("Go to Login"):
                st.session_state.page = "Login"
        else:
            st.error(res.json().get("detail", "Registration failed."))
    except Exception as e:
        st.error(f"An error occurred: {e}")

#-------------------------------Placeholder for login---------------------------

def login_form():
    st.header("Login(To Be Implemented)")
    #We'll handle this after registration works

#-----------------------------------Run App-------------------------

if __name__ == "__main__":
    main()
