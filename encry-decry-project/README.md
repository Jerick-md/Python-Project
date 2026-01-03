# EncryptAndDecrypt 🔐

A simple **Python encryption and decryption project** using the `cryptography` library (Fernet).
This program allows users to input a message, encrypt it, and then decrypt it back to its original form.

---

## 📌 Features
- Generates a secure encryption key automatically
- Encrypts user input text
- Decrypts the encrypted message
- Uses **Fernet symmetric encryption**

---

## 🛠 Requirements
- Python 3.8+
- cryptography library

Install the required library:
```bash
pip install cryptography
```

---

## 🚀 How to Run the Program

1. Clone or download this repository
2. Open a terminal in the project folder
3. Run the Python file:

```bash
python EncrypAndDecry.py
```

4. Enter a message when prompted
5. The program will display:
   - Encrypted message
   - Decrypted message

---

## 📂 Project Structure
```
encry-decry-project/
│
├── EncrypAndDecry.py
└── README.md
```

---

## 🧠 How It Works
- The program generates a **Fernet key**
- Converts user input into bytes
- Encrypts the data using the key
- Decrypts it back to readable text

---

## ⚠️ Note
- The encryption key is generated every time the program runs
- Once the program ends, the key is lost
- For real applications, store the key securely

---

## 👨‍💻 Author
Jerick Comedia
comediajerick22@gmail.com
09465481434
---

## 📜 License
This project is for **learning and educational purposes** only.
