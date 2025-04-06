# Justeat-search

# 🍽 Just Eat Restaurant Viewer

This application allows users to explore restaurants in the UK using the Just Eat API.  
It is available in **two versions**:

1. 🌐 A web interface built with **Flask**  
2. 🖥 A desktop application built with **Tkinter GUI**

---

## 📦 Features

- Search by UK postcode (e.g. `M160RA`)
- View top 10 restaurants in that area
- See cuisines, star ratings, address, and delivery info
- Special Halal badge if applicable ✅
- Sorting by:
  - Rating (High → Low)
  - Name (A → Z)
  - Delivery Cost (Low → High)
- Paginated results: 3 restaurants per page
- Flag emojis for national cuisines 🇮🇳 🇮🇹 🇺🇸
- Two platforms:
  - Flask Web App
  - Tkinter Desktop App

---

## 🛠 Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/justeat-viewer.git
cd justeat-viewer


Create a virtual environment (optional but recommended):


python -m venv venv
source venv/bin/activate  # on Windows use: venv\Scripts\activate

Install dependencies:


pip install -r requirements.txt



## Flask 

python run.py and open your browser and visit 

## tkinter

python gui_app.py

if you want to import to exe file, pip install pyinstaller
pyinstaller --onefile --noconsole gui_app.py