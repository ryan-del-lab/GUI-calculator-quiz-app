import tkinter as tk
from tkinter import messagebox

# Quiz Questions
questions = [
    {
        "question": "What year was the University of Ilorin established?",
        "options": ["1975", "1980", "1962", "1990"],
        "answer": "1975"
    },
    {
        "question": "What is the motto of UNILORIN?",
        "options": ["Knowledge for Service", "Probitas Doctrina", "Learning and Character", "Truth and Excellence"],
        "answer": "Probitas Doctrina"
    },
    {
        "question": "In which state is UNILORIN located?",
        "options": ["Lagos", "Kwara", "Oyo", "Abuja"],
        "answer": "Kwara"
    },
    {
        "question": "What is the main campus of UNILORIN known for?",
        "options": ["Permanent Site", "Mini Campus", "Main Block", "Central Campus"],
        "answer": "Permanent Site"
    },
    {
        "question": "What does UNILORIN stand for?",
        "options": [
            "University of Lagos Ilorin",
            "University of Ilorin",
            "United Nigeria Ilorin",
            "Universal Ilorin Institution"
        ],
        "answer": "University of Ilorin"
    }
]

current_question = 0
score = 0

# Window
root = tk.Tk()
root.title("UNILORIN Quiz")
root.geometry("600x400")
root.configure(bg="lightgray")

# Score Label
score_label = tk.Label(
    root,
    text="Score: 0",
    font=("Arial", 14, "bold"),
    bg="lightgray"
)
score_label.pack(pady=10)

# Question Label
question_label = tk.Label(
    root,
    text="",
    font=("Arial", 16),
    wraplength=500,
    bg="lightgray"
)
question_label.pack(pady=20)

selected_option = tk.StringVar()

# Radio Buttons
radio_buttons = []
for i in range(4):
    rb = tk.Radiobutton(
        root,
        text="",
        variable=selected_option,
        value="",
        font=("Arial", 12),
        bg="lightgray"
    )
    rb.pack(anchor="w", padx=50)
    radio_buttons.append(rb)

def load_question():
    q = questions[current_question]

    question_label.config(
        text=f"Question {current_question + 1}: {q['question']}"
    )

    selected_option.set(None)

    for i, option in enumerate(q["options"]):
        radio_buttons[i].config(text=option, value=option)

def next_question():
    global current_question, score

    if selected_option.get() == "":
        messagebox.showwarning("Warning", "Please select an answer.")
        return

    if selected_option.get() == questions[current_question]["answer"]:
        score += 1

    score_label.config(text=f"Score: {score}")

    current_question += 1

    if current_question < len(questions):
        load_question()
    else:
        messagebox.showinfo(
            "Quiz Finished",
            f"Your final score is {score}/{len(questions)}"
        )
        root.destroy()

# Next Button
next_btn = tk.Button(
    root,
    text="Next",
    command=next_question,
    font=("Arial", 12, "bold"),
    bg="gray",
    fg="white"
)
next_btn.pack(pady=20)

load_question()

root.mainloop()