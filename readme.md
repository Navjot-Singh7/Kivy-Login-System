# 🔐 Kivy Authentication System

A clean and functional authentication system built with Kivy, featuring login and registration screens with comprehensive form validation.

## ✨ Features

- **User Registration** - Create new accounts with name, email, and password
- **Secure Login** - Email and password authentication
- **Form Validation** - Comprehensive input checking and error handling
- **Error Popups** - Specific error messages for different scenarios
- **Smooth Navigation** - Screen transitions between login and registration
- **Data Persistence** - Simple file-based user data storage

## 🛠️ Tech Stack

- **Python 3** - Backend logic and application structure
- **Kivy** - Cross-platform GUI framework
- **Kivy Language (KV)** - Declarative UI design

## 🚀 Installation & Usage

### Prerequisites
```bash
pip install kivy
```

Running the Application

```bash
python main.py
```

📸 Application Flow

1. Login Screen - Enter email and password
2. Registration Screen - Create new account with name, email, password
3. Success Screen - Welcome message after successful authentication
4. Error Handling - Specific popups for invalid email, password, or empty fields

🎯 Validation Scenarios

· ✅ Correct credentials → Success
· ❌ Wrong email → "Wrong Email" popup
· ❌ Wrong password → "Wrong Password" popup
· ❌ Empty fields → "Please enter all information" popup
· ❌ No account exists → "You don't have any account" popup
· ❌ General invalid input → "Check Everything" popup

💡 Code Architecture

· Screen Management - Separate classes for each screen
· Popup System - Custom popups for different error types
· Form Handling - Input validation and data processing
· File I/O - Simple user data storage and retrieval

🔧 Key Components

· LoginWindow - Handles user login logic
· Create_account_window - Manages user registration
· MainWindow - Success screen after authentication
· Multiple popup classes for error handling

🎨 UI Features

· Clean dark blue theme
· Responsive layout with FloatLayout
· Large, readable fonts and inputs
· Intuitive button placement and navigation

🤝 Contributing

Feel free to contribute by:

· Enhancing security features
· Improving UI/UX design
· Adding password hashing
· Implementing email validation

---

A practical authentication system demonstrating Kivy's capabilities for building multi-screen applications with form validation.

```

## 📋 **requirements.txt:**
```txt
kivy
```

🎯 Repository Description:

```
Kivy Authentication System - Login/Register app with form validation, error handling & multi-screen navigation