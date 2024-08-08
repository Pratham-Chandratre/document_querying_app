This application allows users to upload and process documents in .pdf, .docx, and .txt formats. Users can register, log in, upload documents, and query the content. It features a secure authentication mechanism and text extraction functionality.

Features
User Registration & Authentication: Secure user management with hashed passwords.
Document Upload: Support for .pdf, .docx, and .txt files.
Text Extraction: Extracts text from uploaded documents.
Error Handling: Proper handling of unsupported file types and extraction errors.
Prerequisites
Python 3.7 or higher
Virtual environment (optional but recommended)

Usage
Register a New Account

Go to the "Register" menu.
Enter a username and password.
Click "Register" to create a new account.
Log In

Go to the "Login" menu.
Enter your username and password.
Click "Login" to access the document upload and querying features.
Upload Documents

After logging in, use the file uploader to upload a .pdf, .docx, or .txt file.
The extracted text from the document will be displayed.
Query Document Content

Enter a query in the input box.
Click "Submit" to search the uploaded documents for the query.
View and Download Chat History

Click the "Download Chat History" button to download your chat history as a .txt file.
Troubleshooting
File Upload Issues: Ensure the file format is supported (.pdf, .docx, .txt) and check for errors in the Streamlit logs.
Authentication Errors: Verify that the username and password are entered correctly. Ensure the password is hashed and compared correctly.
Encryption Key: If there are issues with encryption, regenerate the key using setup_db.py.
