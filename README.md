# Birthday Reminder Application

## Description  
A simple Flask-based web application designed to help users manage and track birthdays efficiently. The app allows users to add names and birthdates, which are stored in a database. Each day, the application automatically checks for birthdays and sends personalized email reminders. It's a lightweight solution for staying organized with birthdays and sending timely wishes.

## Features  
- **Birthday Management**: Users can add names and birthdates using an interactive form.  
- **Automated Email Reminders**: Sends daily email reminders for birthdays occurring on the current date using Gmail's SMTP service.  
- **Database Integration**: Stores all user-entered birthdays persistently using SQLite.  
- **Threaded Email Sending**: Ensures email notifications are sent asynchronously, preventing delays in app functionality.  
- **Responsive Design**: Powered by Flask-Bootstrap for a clean, modern user interface.  

## Technologies  
- **Backend**: Python, Flask  
- **Database**: SQLite for storing birthday details.  
- **Frontend**: HTML, CSS, and Flask-Bootstrap for styling and layout.  
- **Email Service**: Gmail's SMTP server to send email reminders.  
- **Forms**: Flask-WTF for form validation and handling.  

## Usage  
1. Open the application in your web browser at `http://127.0.0.1:5000/`.  
2. Add birthdays using the form on the home page.  
3. Emails for current day's birthdays will be sent automatically.  

## Notes  
- Ensure Gmail's App Passwords are enabled and replace placeholders in the code with your credentials.  
- This project demonstrates foundational web development concepts, including CRUD operations, database handling, email automation, and Flask integration.
