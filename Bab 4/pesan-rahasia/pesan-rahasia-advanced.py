# Menambahkan modul untuk menampilkan box pesan
from tkinter import messagebox, simpledialog, Tk

# Membuat fungsi untuk mengambil apa yang user ingin lakukan
def get_task():
  task = simpledialog.askstring('Task', 'Do You want to encrypt or decrypt?')
  return task

# Membuat fungsi untuk mengambil pesan dari user
def get_message():
  message = simpledialog.askstring('Message', 'Enter the secret message')
  return message

# Membuat fungsi pengecekkan total huruf
def is_even(number):
  return number % 2 == 0

# Membuat fungsi untuk mengambil huruf pada posisi genap
def get_even_letters(message):
  even_letters = []
  for counter in range(0, len(message)):
    if is_even(counter):
      even_letters.append(message[counter])
  return even_letters

# Membuat fungsi untuk mengambil huruf pada posisi ganjil
def get_odd_letters(message):
  odd_letters = []
  for counter in range(0, len(message)):
    if not is_even(counter):
      odd_letters.append(message[counter])
  return odd_letters

# Membuat fungsi untuk menukar pesan
def swap_letters(message):
  letter_list = []
  if not is_even(len(message)):
    message = message + 'x'
  even_letters = get_even_letters(message)
  odd_letters = get_odd_letters(message)
  for counter in range(0,int(len(message)/2)):
    letter_list.append(odd_letters[counter])
    letter_list.append(even_letters[counter])
  new_message = ''.join(letter_list)
  return new_message

# Membuat fungsi untuk enkripsi memutar balik kata
def encrypt(message):
  swapped_message = swap_letters(message)
  encrypted_message = ''.join(reversed(swapped_message))
  return encrypted_message

# Membuat fungsi untuk menyusun kembali kata
def decrypt(message):
  unreversed_message = ''.join(reversed(message))
  decrypted_message = swap_letters(unreversed_message)
  return decrypted_message

# Memanggil fungsi Tk
root = Tk()

# Membuat perulangan untuk menjalankan program
while True:
  task = get_task()
  if task == 'encrypt':
    message = get_message()
    encrypted = encrypt(message)
    messagebox.showinfo('Ciphertext of the secret message is : ', encrypted)
  elif task == 'decrypt':
    message = get_message()
    decrypted = decrypt(message)
    messagebox.showinfo('Plaintext of the secret message is : ', decrypted)
  else:
    break
root.mainloop()