# Authentication-App
Profileapp is a Django-based authentication system that includes user login, signup, password management, and profile management. The project follows a clean UI design with responsive forms, dynamic validation, and logging to track system events.

## Features

### **User Authentication**

- **Login** with Username or Email and Password.
- Secure user sessions using **Django’s authentication system**.

### **User Signup**

- Register with **Username**, **Email**, and **Password**.
- **Password validation** for security compliance.

### **Password Management**

- **Forgot Password**: Sends a reset link via email.
- **Change Password**: Users can update their password after login.
- **Reset Password**: Allows users to reset passwords via the email link.
- **Note**: App Password | Manage your google account > Security (Enable two step-verification) >App Passwords >Create New App name & Save it where a password will be generated, Copy the 16 character generated password and paste it here.

### **User Dashboard**

- **Greets logged-in users** and provides **Profile & Change Password** options.
- **Logout** option included.

### **Profile Page**

- Displays **Username**, **Email**, **Date Joined**, **Last Active**.
- Provides an option to **logout**.

### **Logging System**

- Logs user actions (signup, login, password changes, etc.).
- Tracks **errors**, **warnings**, and **system activities**.
- Logs are stored in **logs/django_app.log**.

### **Responsive UI**

- Styled using **HTML**, **CSS**, and **JavaScript**.
- Fully mobile-friendly with **media queries**.


![image](https://github.com/user-attachments/assets/1f51e17a-d431-4edb-8342-fd09d857ef83)

![image](https://github.com/user-attachments/assets/459d2498-e08a-488f-82c8-eb2d7d136020)


## Quick Start

To get this project up and running locally on your computer, follow these steps:

1. **Set up a Python virtual environment**.

2. Run the following commands:

   ```bash
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver

3. Open a browser and go to http://127.0.0.1:8000.



