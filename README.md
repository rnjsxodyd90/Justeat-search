# JusteatTW

#  Restaurant Viewer Justeat (10 restaurants only for each search)

This application allows users to explore restaurants in the UK using the Just Eat API.  
It is available in **two versions**:

1. A web interface built with **Flask**  
2.  A desktop application built with **Tkinter GUI** 
---

##  Features

- Search by UK postcode ( `M160RA` fixed for flask web interface, tkinter application allows for search)
- View top 10 restaurants in that area
- See cuisines, star ratings, address, and delivery info
- Special Halal badge if applicable ✅
- Sorting by(only in the tkinter application):
  - Rating (High → Low) 
  - Name (A → Z)
  - Delivery Cost (Low → High)
- Paginated results: 3 restaurants per page
- Flag emojis for national cuisines 🇮🇳 🇮🇹 🇺🇸

---

##  Installation

1. Clone the repository:

git clone https://github.com/yourusername/justeat-viewer.git
cd justeat-viewer


2. Create a virtual environment (optional but recommended):


python -m venv venv
source venv/bin/activate  

3. Install dependencies:


pip install -r requirements.txt



## Flask 

python run.py and open your browser and visit 

## tkinter

python gui_app.py

if you want to import to exe file, pip install pyinstaller
pyinstaller --onefile --noconsole gui_app.py


# Assumptions 

From the list inside the restaurant object[cuisines], I assumed that by cusisines it meant all the objects inside it, not just the countries, as in the dictionary cuisines are defined as "coocking characterizef by specific culture or distinctive geographic region). 

Halal classification is assumed true if the word "Halal" is present in the cuisines array — no further validation is available.

The flag used in the UI is based on the first matching national cuisine from a pre-defined list (Italian, Indian, etc.). I could add more nationalities to it as part of an improvement.


# potential improvements

real-time search input in the Flask app (allow user to enter postcode) could be added like in the tkinter application

From GUI, I could instantly resort results on dropdown change (without re-clicking Search button)

More tags from the restaurant object could be added "Open Now" status and opening hours (from API) could be added

I could Package both Flask and GUI into a single launcher for Windows/Mac



