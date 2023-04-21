import random
import tkinter
import tkinter as tk
from PIL import Image, ImageTk


phrases = [
 "It is certain",
 "It is decidedly so",
 "Without a doubt",
 "Yes — definitely",
 "You may rely on it",
 "As I see it, yes",
 "Most likely",
 "Outlook good",
 "Signs point to yes",
 "yes",
 "Reply hazy, try again",
 "Ask again later",
 "Better not tell you now",
 "Cannot predict now",
 "Concentrate and ask again",
 "Don’t count on it",
 "My reply is no",
 "My sources say no",
 "Outlook not so good",
 "Very doubtful"
]


def random_phrase_widget():
    x = random.randint(0, 19)
    answer = str(phrases[x])
    label = tk.Label(text=answer, fg="white", bg="green", font=("arial", 16), anchor='center')
    label.place(relx=0.5, rely=0.5, anchor="center", width=200)


window = tk.Tk()
window.title("Get the answer")
window.geometry("600x600+290+10")

# Header of the app
header_text = "Ask magic ball yes/no question"
header = tk.Label(text=header_text, fg="white", bg="orange", font=("arial", 18))
header.pack(ipadx= 10, ipady=10, pady=20)

# Magic ball image
image1 = Image.open("pictures/Magic_eight_ball.png")
resized_image = image1.resize((400, 400))
test = ImageTk.PhotoImage(resized_image)
ball_image = tkinter.Label(image=test)
ball_image.image = test
ball_image.place(relx=0.5, rely=0.5, anchor="center")

# Button "Get the answer|
button = tk.Button(text="Get the answer", width=25, height=2, bg="white",
                   fg="black", command=random_phrase_widget, anchor='center')
button.place(y=500, x=290, anchor="center")

window.mainloop()
