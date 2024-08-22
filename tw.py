import random
import tkinter

# Daftar warna yang digunakan
colors_name = ['Red', 'White', 'Pink', 'Blue', 'Black', 'Brown', 'Purple', 'Green']

score = 0
time_left = 60

def startGame(play):
    global time_left
    
    if time_left == 60:
        countdown()
    
    changeColor()

def changeColor():
    global score
    global time_left

    if time_left > 0:
        e.focus_set()
        
        # Jika tebakan benar
        if e.get().lower() == label.cget("fg").lower():
            score += 1

        # Mengosongkan entry box
        e.delete(0, tkinter.END)
        
        # Mengacak urutan warna
        random.shuffle(colors_name)
        
        # Mengupdate warna dan teks label
        label.config(fg=str(colors_name[1]), text=str(colors_name[0]))
        scoreLabel.config(text="Score: " + str(score))

def countdown():
    global time_left
    if time_left > 0:    
        time_left -= 1
        timeLabel.config(text='Time Left: ' + str(time_left))
        # Mengatur countdown berulang setiap 1 detik
        timeLabel.after(1000, countdown)

# Membuat GUI Tkinter
root = tkinter.Tk()
root.title("The COLORGAME")
root.geometry("600x400")

# Instruksi permainan
instruct = tkinter.Label(root, text="Which Color", font=("san-serif", 20))
instruct.pack()

# Label skor
scoreLabel = tkinter.Label(root, text="Press Enter Key To Start", font=("san-serif", 24))
scoreLabel.pack()

# Label waktu yang tersisa
timeLabel = tkinter.Label(root, text="Time Left: " + str(time_left), font=("san-serif", 18))
timeLabel.pack()

# Label untuk menunjukkan warna dan kata
label = tkinter.Label(root, font=("san-serif", 60))
label.pack()

# Entry box untuk input pemain
e = tkinter.Entry(root)
root.bind('<Return>', startGame)
e.pack()
e.focus_set()

# Menjalankan loop utama Tkinter
root.mainloop()
