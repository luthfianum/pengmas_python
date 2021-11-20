# Module yang dibutuhkan 
import random
import string

# Daftar Kata Benda
daftar_kata_benda = ["mobil", "motor", "buku", "pulpen", "pensil", "novel", "baju"]

# Daftar Kata Sifat
daftar_kata_sifat = ["berapi", "membeku", "beracun", "berair", "suci"]

# Judul Aplikasi
print('Welcome to Password Picker')

while True:
  # Memilih kata benda
  kata_benda = random.choice(daftar_kata_benda)

  # Memilih kata sifat
  kata_sifat = random.choice(daftar_kata_sifat)

  # Memilih angka acak
  angka_acak = random.randrange(0, 100)

  # Memilih karakter spesial 
  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
  karakter_spesial = random.choice(string.punctuation)

  # Membuat password yang aman
  password = kata_benda + kata_sifat + str(angka_acak) + karakter_spesial
  print('Password baru kamu adalah %s' % password)
  
  # menerima response mau membuat password lain?
  response = input('Apakah kamu ingin membuat password lain? (Y/N) : ')
  if response == 'N':
    break