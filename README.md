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

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/django-auth-system.git

