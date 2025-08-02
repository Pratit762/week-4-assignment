# ✈️ Flight Booking Debug & Optimization – Week 4 Assignment

## 📌 Project Overview
This project focuses on debugging and optimizing a Python automation script for processing synthetic flight reservation data. It involves fixing critical errors, improving data validation, and enhancing performance to ensure reliable and efficient automation.

---

## 📁 Folder Structure
```
.
├── booking_processor.py
├── data/
│   └── reservations.csv
├── generate_sample_data.py
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Environment Setup

1. **Clone the Repository**
   ```bash
   git clone <your-repo-url>
   cd <project-directory>
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate Virtual Environment**
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🧪 Data Generation

To create sample reservation records:

```bash
python generate_sample_data.py
python main.py
```

This generates a `reservations.csv` file in the `data/` folder with 200 mock flight booking entries.

---

## 🐞 Debugging Summary

| ID | Error Description                       | Root Cause                        | Fix Description                    | Impact                                |
|----|----------------------------------------|----------------------------------|------------------------------------|----------------------------------------|
| 1  | FileNotFoundError for `reservations.csv` | Data file not pre-generated      | Ensured correct file generation flow | Script now executes without failure    |
| 2  | Blank passenger names processed        | No input validation in script    | Added validation in `booking_processor.py` | Prevents invalid email processing      |

---

## 🚀 Performance Optimizations

Two major changes improved performance and reliability:

- ✅ **Skipped invalid rows** using `pandas` filtering
- ✅ **Replaced row-by-row loop** with efficient list comprehensions

These changes significantly reduced processing time and improved the script's ability to handle malformed or incomplete data.

---

## 📤 Sample Output

After running the final script:

```bash
python main.py
```

Output:
```
Email sent to John Doe for PNR: 8asdhj2k
Email sent to Jane Smith for PNR: c9f3f7a1
...
```

---

## 🧠 Reflection

This project gave me practical exposure to:

- Real-world debugging and testing
- Writing production-ready Python scripts
- Improving code reliability and efficiency
- Using Git for source control
- Leveraging GitHub Copilot for suggestions, while ensuring manual validation and logic correctness

---

## 📚 Tech Stack

- Python 3.x
- pandas
- Git & GitHub
- GitHub Copilot (assistive)

---

## ✅ Next Steps (Optional Ideas)

- Add logging instead of print statements
- Integrate with real email API (e.g., SendGrid or SMTP)
- Automate scheduling using cron or Task Scheduler
- Build a small dashboard to visualize sent bookings

---

## 📬 Author

- **Name:** *[Your Full Name]*
- **Course:** MANG6093 – Robotic Process Automation
- **Week:** 4