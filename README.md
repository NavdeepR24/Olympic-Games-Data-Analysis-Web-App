# 🏅 Olympics Analysis Web App

An interactive data analysis web application built with **Python** and **Streamlit** to explore **120 years of Olympic Games history** — from Athens 1896 to Tokyo 2020.

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red?style=flat&logo=streamlit)
![Pandas](https://img.shields.io/badge/Pandas-1.3+-green?style=flat&logo=pandas)
![Plotly](https://img.shields.io/badge/Plotly-5.0+-purple?style=flat&logo=plotly)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat)

---

## 📌 Table of Contents

- [Demo](#-demo)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Dataset](#-dataset)
- [Installation](#-installation)
- [Usage](#-usage)
- [Technologies Used](#-technologies-used)
- [What I Learned](#-what-i-learned)
- [Future Improvements](#-future-improvements)

---

## 🎥 Demo

> https://olympic-games-data-analysis-web-app-zzb4cjvm4kvgzrrvhceqym.streamlit.app/

---

## ✨ Features

### 🥇 Medal Tally
- View medal standings filtered by **Year** and **Country**
- Supports both **Summer** and **Winter** Olympics
- Sortable table with Gold, Silver, Bronze and Total columns

### 📊 Overall Analysis
- Key statistics — Editions, Host Cities, Sports, Events, Nations, Athletes
- **Participating Nations** over the years (line chart)
- **Events** growth over the years (line chart)
- **Sports heatmap** — number of events per sport per year
- **Most Successful Athletes** filterable by sport

### 🌍 Country-wise Analysis
- Medal tally trend for any country over the years
- Sport-wise performance heatmap per country
- Top 10 athletes of any selected country

### 🏃 Athlete-wise Analysis
- Age distribution of all athletes vs medal winners
- Height vs Weight scatter plot by sport and medal type
- Men vs Women participation trend over the years

---

## 📁 Project Structure

```
olympics-analysis/
│
├── app.py                  # Main Streamlit application & UI
├── preprocessor.py         # Data cleaning & transformation
├── helper.py               # All analysis & computation functions
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
│
└── data/
    ├── athlete_events.csv  # Main Olympics dataset
    └── noc_regions.csv     # NOC code to country mapping
```

---

## 📦 Dataset

This project uses the **120 Years of Olympic History** dataset from Kaggle.

👉 [Download from Kaggle](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results)

**Files needed:**

| `athlete_events.csv` | Every athlete, event, medal from 1896–2016 | ~271,000 |
| `noc_regions.csv` | Maps NOC country codes to region names | 230 |

> ⚠️ Download both files and place them inside a `data/` folder in the project root.

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/olympics-analysis.git
cd olympics-analysis
```

### 2. Create a virtual environment (recommended)
```bash
# Create
python -m venv olympics_env

# Activate — Windows
olympics_env\Scripts\activate

# Activate — Mac/Linux
source olympics_env/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Download the dataset
- Go to [Kaggle Dataset](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results)
- Download `athlete_events.csv` and `noc_regions.csv`
- Place both files inside a `data/` folder

### 5. Run the app
```bash
streamlit run app.py
```

## 📋 Requirements

Create a `requirements.txt` with:

```
streamlit
pandas
numpy
matplotlib
seaborn
plotly
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python 3.8+** | Core programming language |
| **Streamlit** | Web app framework & UI |
| **Pandas** | Data loading, cleaning, analysis |
| **NumPy** | Numerical computations |
| **Plotly** | Interactive charts & visualizations |
| **Matplotlib** | Static chart rendering |
| **Seaborn** | Heatmaps & statistical plots |

---

## 📚 What I Learned

- Building multi-page interactive dashboards with **Streamlit**
- Data cleaning and preprocessing with **Pandas** (handling nulls, merging datasets, type conversion)
- Creating interactive visualizations with **Plotly Express**
- Structuring Python projects with **Separation of Concerns** (`app.py`, `preprocessor.py`, `helper.py`)
- Working with real-world messy datasets and deriving meaningful insights
- Using **virtual environments** and `requirements.txt` for reproducible projects

---

## 🚀 Future Improvements

- [ ] Deploy on Streamlit Cloud for public access
- [ ] Add **Prediction Model** — predict medal count for upcoming Olympics
- [ ] Add **Sport-wise deep dive** analysis page
- [ ] Add **Head-to-Head** country comparison feature
- [ ] Add **Paralympic Games** data
- [ ] Improve mobile responsiveness

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 👨‍💻 Author

**Your Name**
- GitHub: [NavdeepR24](https://github.com/NavdeepR24)
- LinkedIn: [Navdeep Singh](https://www.linkedin.com/in/navdeep-singh-r24/)

---

> ⭐ If you found this project helpful, please give it a star on GitHub!