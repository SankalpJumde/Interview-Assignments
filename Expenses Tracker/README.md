# 💸 Personal Expense Tracker (AI-Powered Internship Task)

An interactive **Expense Tracker App** built as part of my AI/ML Internship task.  
It allows users to enter **daily, weekly, and monthly** expenses, and provides a detailed breakdown with **visual insights** (pie chart, bar chart, histogram).  

👉 Built in **Python + Streamlit**, with a fallback **CLI version** for terminal lovers.

---

## ✨ Features
- 🧑 Personal profile section (Name, Age, Gender, Profession)  
- 📅 Track **Daily, Weekly, and Monthly** expenses separately  
- 📊 Visualize spending with **Pie Chart, Bar Chart, Histogram**  
- 💾 Export results to **CSV/JSON**  
- 🌐 Streamlit app for interactive use  
- 🖥️ CLI app for offline quick entry  

---

## 🚀 Demo Screenshots

### 👤 Profile Section
Personalized dashboard with user info  
![Profile Demo](Expenses Tracker/assets/Screenshot 2025-10-04 105616.png)

### 📊 Expense Breakdown
View expenses grouped by **Daily, Weekly, Monthly**  
![Breakdown Demo](Expenses Tracker/assets/Screenshot 2025-10-04 105931.png)

### 📈 Visualizations
Pie chart (monthly distribution), bar chart (frequency totals), histogram (expense spread)  
![Pie Chart Demo](Expenses Tracker/assets/Screenshot 2025-10-04 105946.png)
![Bar Graph Demo](Expenses Tracker/assets/Screenshot 2025-10-04 105957.png)
![Histogram Demo](Expenses Tracker/assets/Screenshot 2025-10-04 110012.png)

---

## 🛠️ Installation & Setup

1. Clone the repo:
```bash
git clone https://github.com/SankalpJumde/expenses-tracker.git
cd expense-tracker 
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run CLI version:
```bash
python expenses_tracker.py
```

4. Run Streamlit version:
```bash
streamlit run streamlit.py
```

📂 Project Structure
├── expenses_tracker.py         # CLI version

├── streamlit.py   # Streamlit UI version

├── outputs/                       # Saved JSON/CSV reports

├── requirements.txt               # Dependencies

└── README.md                      # Project documentation

---
## 📝 My Journey (Learning & Effort)
✅ Did you try hard and document your journey?
Yes! I started with a simple CLI version that only calculated daily → weekly → monthly by scaling.
Then I realized weekly and monthly expenses should be separate, so I redesigned the model.
Finally, I extended it into a Streamlit app with visualizations and export options.
I documented each step, errors, and fixes in the repo.

✅ Did you Google/ChatGPT things and figure it out?
Yes!
Googled how to save CSV/JSON properly in Python
Used Streamlit docs for charts & download buttons
Asked ChatGPT for structuring daily, weekly, monthly inputs and for UI polishing ideas
Searched examples for matplotlib pie chart & histogram integration with Streamlit

✅ Did you go beyond the minimum?
Absolutely 
Added personal info card for aesthetics
Provided both CLI & Streamlit versions
Added Pie chart, Bar chart, Histogram visualizations
CSV export for users to download their data
Planning to add a Smart Advisor (rule-based suggestions on overspending categories)

🌟 Future Improvements
Add AI-powered advisor (e.g., “Your Food expenses are 40% of monthly budget — try reducing to 30%”)
Deploy on Streamlit Cloud / HuggingFace Spaces for public access
Add PDF report export for monthly summaries
Income vs Expense → show savings %

---

🧑‍💻 Author

Sankalp Jumde
🚀 AI/ML Intern
💼 Passionate about building practical AI-powered apps
🌐  [[LikendIn](https://www.linkedin.com/in/sankalp-jumde/)] | [[GitHub](https://github.com/SankalpJumde)] | [[Mail](sankalpkrishna1103@gmail.com)]
