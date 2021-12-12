# Mengimport modul turtle dan juga modul cycle
import turtle
from itertools import cycle

# Menambahkan warna untuk pena
colors = cycle(['red', 'orange', 'yellow','green', 'blue', 'purple'])

# Membuat fungsi menggambar lingkaran
def draw_circle(size, angle, shift):
  turtle.pencolor(next(colors))
  turtle.circle(size)
  turtle.right(angle)
  turtle.forward(shift)
  draw_circle(size + 5, angle + 1, shift + 1)

# Menentukan warna background dari program
# Menentukan kecepatan turtle dan juga ukuran dari pena
turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(4)
draw_circle(30, 0 , 1)

# Menentukan warna dari turtle
turtle.pencolor('red')
turtle.circle(30)
