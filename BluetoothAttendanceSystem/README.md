# Bluetooth Attendance System 📡📊

A **basic Bluetooth-based attendance system** built with Python.  
This project scans nearby Bluetooth devices and records detected device names into an Excel file.

> ⚠️ This is a **blueprint / prototype** for a future project.  
> Some features and functionality are still missing.

---

## 📌 Project Description

This program:
- Scans nearby **Bluetooth devices**
- Collects detected device names
- Stores the data into an **Excel file**
- Reads and displays the attendance data

⚠️ **Limitations:**
- Works only on **laptops and mobile phones**
- Does **NOT** work with:
  - Bluetooth speakers
  - Wireless microphones
- Device name must be visible to be detected

---

## 🛠 Requirements

- Python 3.9+
- Bluetooth-enabled device

### Python Libraries
Install required libraries using:

```bash
pip install bleak pandas openpyxl
```

---

## 📂 Project Structure

```
BluetoothAttendanceSystem/
│
├── AttendanceSystem.py
├── StudentDeviceAttendance.xlsx
└── README.md
```

---

## 🚀 How to Run the Program

1. Clone or download this repository
2. Open a terminal inside the project folder
3. Run the script:

```bash
python AttendanceSystem.py
```

4. The program will:
   - Scan nearby Bluetooth devices
   - Create an Excel file: `StudentDeviceAttendance.xlsx`
   - Display the detected devices

---

## 🧠 How It Works

1. Uses **BleakScanner** to discover Bluetooth devices
2. Extracts device names
3. Saves data into a Pandas DataFrame
4. Exports the data to an Excel file
5. Reads and prints the attendance record

---

## ⚠️ Notes & Warnings

- Bluetooth must be **enabled**
- Run the program with proper permissions
- Some devices may hide their names and won't appear
- Excel file is overwritten each run

---

## 🔮 Future Improvements

- Student name matching
- Timestamp logging
- Database support
- GUI interface
- Device MAC address tracking
- Authentication system

---

## 👨‍💻 Author

Jerick Comedia
comediajerick22@gmail.com
09465481434

---

## 📜 License

This project is intended for **educational and experimental purposes only**.
