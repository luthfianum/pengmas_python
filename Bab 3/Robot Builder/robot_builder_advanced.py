# Pada kode ini kita mengubah wajah dari robot menjadi lebih unik! :D

# Step 1 Mengimport turtle sebagai 't'
import turtle as t

# Step 2 Membuat fungsi untuk menggambar sebuah persegi 
def rectangle(horizontal, vertical, color):
    t.pendown()
    t.pensize()
    t.color(color)
    t.begin_fill()
    for counter in range(1, 3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()

# Step 3 Membuat background berwarna 'Dodger blue' dengan kecepatan turtle slow
t.penup()
t.speed('slow')
t.bgcolor('Dodger blue')

# feet
# Step 4 menggambar kaki dari robot dengan warna 'blue'
t.goto(-100, -150)
rectangle(50, 20, 'blue')
t.goto(-30, -150)
rectangle(50, 20, 'blue')

# legs
# Step 5 menggambar kaki panjang dari robot dengan warna 'grey'
t.goto(-25, -50)
rectangle(15, 100, 'grey')
t.goto(-55, -50)
rectangle(-15, 100, 'grey')

# body
# Step 6 menggambar badan dengan warna merah
t.goto(-90, 100)
rectangle(100, 150, 'red')

# arms
# Step 7 menggambar tangan dari robot
t.goto(-150, 70)
rectangle(60, 15, 'grey')
t.goto(-150, 110)
rectangle(15, 40, 'grey')

t.goto(10, 70)
rectangle(60, 15, 'grey')
t.goto(55, 110)
rectangle(15,40, 'grey')

# neck
# Step 8 menggambar leher dari robot
t.goto(-50, 120)
rectangle(15, 20, 'grey')

# head
# Step 9 menggambar kepala dari robot
t.goto(-85, 170)
rectangle(80, 50, 'red')

# Perubahan dilakukan pada step mata dan mulut untuk membuatnya menjadi lebih unik ;)

# eyes
# Step 10 menggambar mata dari robot
t.goto(-60, 160)
rectangle(30, 10, 'white')
t.goto(-60, 160)
rectangle(5, 5, 'black')
t.goto(-45, 155)
rectangle(5, 5, 'black')

# mouth
# Step 11 menggambar mulut robot
t.goto(-65, 135)
t.right(5)
rectangle(40, 5, 'black')

# Step 12
# Menutup program dengan menyembunyikan turtle
t.hideturtle()