import random
import string

# Tambahkan kata benda
daftar_kata_benda = ["mobil", "motor", "buku", "pulpen", "pensil", "novel", "baju"]

# Tambahkan kata sifat
daftar_kata_sifat = ["berapi", "membeku", "beracun", "berair", "suci"]

# Buat daftar warna
daftar_warna = ["merah", "biru", "kuning", "hijau", "hitam", "orange"]

print('Welcome to Password Picker')

while True:
  # Perbanyak pilihan password yang akan ditampilkan 
  for num in range(5):
    kata_benda = random.choice(daftar_kata_benda)

    kata_sifat = random.choice(daftar_kata_sifat)

    warna = random.choice(daftar_warna)

    angka_acak = random.randrange(0, 100)

    karakter_spesial = random.choice(string.punctuation)

    # Tambahkan Warna
    password = kata_benda + warna + kata_sifat + str(angka_acak) + karakter_spesial
    print('Password baru kamu adalah %s' % password)
    
  response = input('Apakah kamu ingin membuat password lain? (Y/N) : ')
  if response == 'N':
    break