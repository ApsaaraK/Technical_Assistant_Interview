# Combined AI + Data Automation Project
# Author: Tiruni Karunarathna
# Description: Cleans data, creates visualization, and summarizes text using OpenAI API

import pandas as pd
import matplotlib.pyplot as plt
import openai
import os

# ---------- SETUP ----------
openai.api_key = os.getenv("OPENAI_API_KEY")  # or directly assign your key for testing

# ---------- PART 1: DATA AUTOMATION ----------

data = {
    'Department': ['AI', 'Data Science', 'AI', 'Web Dev', 'Data Science', 'Web Dev', 'AI'],
    'Hours Spent': [15, 20, 18, 25, 22, 30, 12]
}

df = pd.DataFrame(data)
print("Original Data:\n", df)

# Clean and summarize data
summary = df.groupby('Department')['Hours Spent'].mean().reset_index()
summary.rename(columns={'Hours Spent': 'Avg Hours Spent'}, inplace=True)
print("\nCleaned Summary:\n", summary)

# Create a visualization
plt.figure(figsize=(6, 4))
plt.bar(summary['Department'], summary['Avg Hours Spent'], color='skyblue')
plt.title('Average Hours Spent per Department')
plt.xlabel('Department')
plt.ylabel('Average Hours Spent')
plt.tight_layout()
plt.savefig('data_summary_chart.png')
plt.show()

# ---------- PART 2: AI RESEARCH ASSISTANT ----------

text_to_summarize = """
Artificial Intelligence (AI) is a branch of computer science that aims to create systems
capable of performing tasks that normally require human intelligence, such as understanding
natural language, recognizing patterns, making decisions, and learning from experience.
Recent advances in deep learning have greatly expanded AI capabilities across industries.
"""

print("\n--- AI Summary ---\n")

try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes text clearly."},
            {"role": "user", "content": f"Summarize this in 3 lines:\n{text_to_summarize}"}
        ]
    )
    summary_text = response['choices'][0]['message']['content']
    print(summary_text)
except Exception as e:
    print("Error calling OpenAI API:", e)

# ---------- END ----------
print("\nProcess completed successfully!")