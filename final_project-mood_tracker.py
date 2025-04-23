import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import os
import turtle


mood_options = ["Srećno", "Tužno", "Umorno", "Motivisano", "Anksiozno", "Zahvalno"]

root = tk.Tk()
root.title("Mood Tracker")
root.geometry("400x470")
root.config(padx=20, pady=20, bg="#e0f2f7")



def save_entry():
    mood = var_mood.get()
    rating = scale_rating.get()
    note = entry_note.get("1.0", tk.END).strip()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not note:
        messagebox.showwarning("Upozorenje", "Unesi kratak opis!")
        return
    
    zapis = f"{date} | Raspoloženje: {mood} | Ocjena: {rating}/10 | Opis: {note}\n"

    with open("mood_log.txt", "a", encoding="utf-8") as f:
        f.write(zapis)

    messagebox.showinfo("Uspjeh", "Unos je sačuvan!")
    entry_note.delete("1.0", tk.END)
    scale_rating.set(5)
    var_mood.set(mood_options[0])
    show_history()

    if mood == "Srećno":
        draw_happy_face()
    elif mood == "Tužno":
        draw_sad_face()
    elif mood == "Umorno":
        draw_tired_face()
    elif mood == "Motivisano":
        draw_motivated_face()
    elif mood == "Anksiozno":
        draw_anxious_face()
    elif mood == "Zahvalno":
        draw_grateful_face()

# Crtaj smajli sa turtle
def draw_happy_face():
    window = turtle.Screen()
    window.title("Smajli za srećno raspoloženje")
    t = turtle.Turtle()
    t.speed(10)

    # Glava
    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    # Levo oko
    t.penup()
    t.goto(-35, 40)
    t.dot(20, "black")

    # Desno oko
    t.goto(35, 40)
    t.dot(20, "black")

    # Osmeh
    t.penup()
    t.goto(-40, -20)
    t.setheading(-60)
    t.pendown()
    t.circle(50, 120)

    t.hideturtle()
    turtle.done()


def draw_sad_face():
    window = turtle.Screen()
    window.title("Tužni smajli")
    t = turtle.Turtle()
    t.speed(10)
    
    # Glava
    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    # Levo oko
    t.penup()
    t.goto(-35, 40)
    t.dot(20, "black")

    # Desno oko
    t.goto(35, 40)
    t.dot(20, "black")

    # Suza ispod levog oka
    t.penup()
    t.goto(-35, 20)
    t.dot(10, "blue")

    # Tužna usta (luk nadole)
    t.penup()
    t.goto(-50, -50)
    t.setheading(90)
    t.pendown()
    t.circle(-50, 180)

    t.hideturtle()
    turtle.done()
    
def draw_tired_face():
    window = turtle.Screen()
    window.title("Umorno lice")
    t = turtle.Turtle()
    t.speed(3)

    # Glava
    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.fillcolor("#f5e642")  # bleda žuta
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    # Zatvoreno levo oko (linija)
    t.penup()
    t.goto(-40, 40)
    t.setheading(0)
    t.pendown()
    t.pensize(4)
    t.forward(20)

    # Zatvoreno desno oko (linija)
    t.penup()
    t.goto(20, 40)
    t.setheading(0)
    t.pendown()
    t.forward(20)

    # Ravna usta
    t.penup()
    t.goto(-30, -40)
    t.setheading(0)
    t.pendown()
    t.forward(60)

    # "Zzz..." simbol
    t.penup()
    t.goto(60, 80)
    t.pendown()
    t.write("Zzz...", font=("Arial", 18, "normal"))

    t.hideturtle()
    turtle.done()

def draw_motivated_face():
    window = turtle.Screen()
    window.title("Motivisano lice")
    t = turtle.Turtle()
    t.speed(3)

    # Glava
    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.fillcolor("lightgoldenrod")
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    # Veliko levo oko
    t.penup()
    t.goto(-35, 40)
    t.dot(30, "black")

    # Veliko desno oko
    t.goto(35, 40)
    t.dot(30, "black")

    # Širok osmeh
    t.penup()
    t.goto(-40, -20)
    t.setheading(-60)
    t.pendown()
    t.pensize(3)
    t.circle(50, 120)

    angles = [0, 90, 180, 270, 45, 135, 225, 315]

    for angle in angles:
        t.penup()
        t.goto(0, 0)
        t.setheading(angle)
        t.forward(100)
        t.pendown()
        t.forward(20)

    t.hideturtle()
    turtle.done()
    
def draw_anxious_face():
    window = turtle.Screen()
    window.title("Anksiozno lice")
    t = turtle.Turtle()
    t.speed(3)

    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.fillcolor("#fff176")  # svetložuta boja
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    # Velike oči (izražena panika)
    t.penup()
    t.goto(-35, 40)
    t.dot(25, "black")

    t.goto(35, 40)
    t.dot(25, "black")

    # Talasasta usta (anksiozna grimasa)
    t.penup()
    t.goto(-40, -40)
    t.pendown()
    t.pensize(3)
    
    for i in range(3):
        t.setheading(-20)
        t.circle(15, 60)
        t.setheading(20)
        t.circle(-15, 60)

    # Kap znoja iznad desnog oka
    t.penup()
    t.goto(50, 70)
    t.dot(10, "blue")

    t.hideturtle()
    turtle.done()

def draw_grateful_face():
    window = turtle.Screen()
    window.title("Zahvalno lice")
    t = turtle.Turtle()
    t.speed(3)

    # Glava
    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.fillcolor("#fff8dc")  # svetla bež boja
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    t.pensize(3)

    # Zatvoreno levo oko (luk)
    t.penup()
    t.goto(-40, 40)
    t.setheading(-60)
    t.pendown()
    t.circle(15, 120)

    # Zatvoreno desno oko (luk)
    t.penup()
    t.goto(25, 40)
    t.setheading(-120)
    t.pendown()
    t.circle(-15, 120)

    # Blagi osmeh
    t.penup()
    t.goto(-30, -30)
    t.setheading(-60)
    t.pendown()
    t.circle(30, 120)

    t.hideturtle()
    turtle.done()
       

def show_history() :
    if not os.path.exists("mood_log.txt"):
        open("mood_log.txt", "w", encoding="utf-8").close()
    with open("mood_log.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        last_5 = lines[-5:]

    history_text.config(state="normal")
    history_text.delete("1.0", tk.END)
    for line in reversed(last_5):
        history_text.insert(tk.END, line)
    history_text.config(state="disabled")


font_title = ("Arial", 14, "bold")
font_text = ("Helvetica", 11)

tk.Label(root, text="Kako se osjećaš danas?😃", font=font_title, bg="#e0f2f7").pack(anchor="w")
var_mood = tk.StringVar(value=mood_options[0])
mood_menu = tk.OptionMenu(root, var_mood, *mood_options)
mood_menu.config(font=font_text, bg="lightblue", fg="black")
mood_menu["menu"].config(font=font_text, bg="lightblue", fg="black")
mood_menu.pack(fill="x", pady=5)

tk.Label(root, text="Ocjeni dan (1-10):", font=font_title, bg="#e0f2f7").pack(anchor="w", pady=10)
scale_rating = tk.Scale(root, from_=1, to=10, orient="horizontal", bg="#f0f8ea", fg="green", font=font_text)
scale_rating.set(5)
scale_rating.pack(fill="x")


tk.Label(root, text="Šta ti je popravilo dan?❤", font=font_title, bg="#e0f2f7").pack(anchor="w", pady=10)
entry_note = tk.Text(root, height=4, bg="#fffacd", fg="black", font=font_text)
entry_note.pack(fill="x")

tk.Button(root, text="Sačuvaj unos", command=save_entry, bg="lightgreen", fg="white", font=font_text, relief=tk.RAISED, borderwidth=2).pack(pady=15)

tk.Label(root, text="Posljednjih 5 unosa:", font=font_title, bg="#e0f2f7").pack(anchor="w", pady=10)

frame = tk.Frame(root, bg="#e0f2f7")
frame.pack(fill="both", expand=True)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

history_text = tk.Text(frame, height=10, bg="#f4f4f4", yscrollcommand=scrollbar.set, wrap="word", font=font_text)
history_text.pack(side="left", fill="both", expand=True)
scrollbar.config(command=history_text.yview)
history_text.config(state="disabled")

show_history()

root.mainloop()
