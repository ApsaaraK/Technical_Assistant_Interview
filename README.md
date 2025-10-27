# 🧠 AI + Data Automation Project

A small Python project that combines **data automation** and **AI text summarization**.  
It was created to demonstrate how simple tools like Pandas, Matplotlib, and OpenAI’s API can automate repetitive tasks and generate insights efficiently.

---

## 🚀 Features

✅ Clean and summarize raw data using **Pandas**  
✅ Create simple visualizations using **Matplotlib**  
✅ Summarize research text or long articles using **OpenAI API**  
✅ Works with any text or CSV/Excel dataset  

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone [https://github.com/yourusername/](https://github.com/ApsaaraK/Technical_Assistant_Interview.git
cd Technical_Assistant_Interview
```

### 2. Install Dependencies
```bash
pip install pandas matplotlib openai
```

### 3. Set Your OpenAI API Key
Create an API key from [OpenAI Dashboard](https://platform.openai.com/api-keys)  
Then set it in your environment:

#### Windows:
```bash
setx OPENAI_API_KEY "your_api_key_here"
```

#### macOS/Linux:
```bash
export OPENAI_API_KEY="your_api_key_here"
```

*(Or replace directly in the code for quick testing, but don’t commit your key!)*

---

## ▶️ Run the Script
```bash
python ai_data_automation_project.py
```

The script will:
- Print the **original** and **cleaned** dataset
- Generate a **bar chart** (`data_summary_chart.png`)
- Summarize a short research paragraph using the **OpenAI API**

---

## 📊 Example Output

**Console Output:**
```
Original Data:
     Department  Hours Spent
0            AI           15
1  Data Science           20
...

Cleaned Summary:
     Department  Avg Hours Spent
0            AI            15.0
1  Data Science            21.0
...

--- AI Summary ---
AI is a branch of computer science focused on creating systems
that can perform human-like tasks such as learning and decision-making.
Recent advances in deep learning have greatly improved its applications.
```

**Generated Chart:**

![Bar Chart Example](data_summary_chart.png)

---

## 💡 Technologies Used
- Python 3.x  
- Pandas  
- Matplotlib  
- OpenAI API  

---

## 🧩 Author
**Tiruni Karunarathna**  
Computer Science Graduate & Data Science Engineer  
*(Created as part of a technical assistant application project)*

---

## 📄 License
This project is open-source under the [MIT License](LICENSE).
