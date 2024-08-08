import streamlit as st
import hashlib
from backend import extract_text_from_pdf, extract_text_from_docx, extract_text_from_txt

# In-memory store for users (for testing purposes)
users = {}

def add_user(username, password):
    """Add a new user to the in-memory store."""
    if username in users:
        return False
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    users[username] = hashed_password
    return True

def authenticate(username, password):
    """Authenticate user by username and password."""
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return users.get(username) == hashed_password

# Streamlit UI
st.title("Document Upload and Text Extraction")

menu = ["Login", "Register"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Register":
    st.subheader("Create New Account")
    new_user = st.text_input("Username")
    new_password = st.text_input("Password", type='password')

    if st.button("Register"):
        if add_user(new_user, new_password):
            st.success("You have successfully created an account")
            st.info("Go to Login Menu to login")
        else:
            st.warning("Username already exists.")

elif choice == "Login":
    st.subheader("Login")

    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type='password')

    if st.sidebar.button("Login"):
        if authenticate(username, password):
            st.success(f"Logged In as {username}")

            # Document Upload
            uploaded_file = st.file_uploader("Upload a document", type=["pdf", "docx", "txt"])

            if uploaded_file is not None:
                try:
                    st.write(f"Uploaded file name: {uploaded_file.name}")
                    st.write(f"Uploaded file type: {uploaded_file.type}")

                    # Handle different file types
                    if uploaded_file.type == "application/pdf":
                        text = extract_text_from_pdf(uploaded_file)
                    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                        text = extract_text_from_docx(uploaded_file)
                    elif uploaded_file.type == "text/plain":
                        text = extract_text_from_txt(uploaded_file)
                    else:
                        st.error("Unsupported file type.")
                        st.stop()

                    st.write("Extracted Text:")
                    st.write(text[:1000])  # Only show the first 1000 characters

                except Exception as e:
                    st.error(f"An error occurred: {e}")

        else:
            st.warning("Incorrect Username/Password")
