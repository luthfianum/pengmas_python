# Import module yang dibutuhkan 
import random

# Buatlah Variable nyawa 
nyawa = 9

# Buatlah daftar kata rahasia yang akan ditebak
daftar_kata_rahasia = ['twitter', 'spotify', 'webtoon', 'discord']

# Pilih kata rahasia yang akan ditebak
kata_rahasia = random.choice(daftar_kata_rahasia)

# Membuat Clue huruf yang benar
clue = list('???????')

# simbol hati/nyawa yang dimengerti komputer
heart_symbol = u'\u2764'

# Menyimpan hasil
sudah_tertebak = False

def update_clue(huruf_tebakan, kata_rahasia, clue):
  index = 0
  
  while index < len(kata_rahasia):
    # Cek apakah huruf tebakan ada di kata rahasia
    if(huruf_tebakan == kata_rahasia[index]):
      clue[index] = huruf_tebakan
    index = index + 1

while nyawa > 0:
  # tampilan clue yang ada
  print(clue)
  
  # Tampilkan sisa nyawa pemain
  print('Sisa nyawa : ' + heart_symbol * nyawa)
  
  # Minta pemain menebak huruf
  huruf_tebakan = input('Masukkan huruf tebakan anda : ')
  
  # Cek apakah huruf tebakan adalah kata rahasianya
  if huruf_tebakan == kata_rahasia :
    sudah_tertebak = True
    break
  
  if huruf_tebakan in kata_rahasia:
    update_clue(huruf_tebakan, kata_rahasia, clue)
  else: 
    print('Tebakan anda kurang tepat, nyawa anda berkurang 1')
    nyawa = nyawa - 1

if sudah_tertebak == True:
  print('Selamat, anda berhasil menebak kata rahasianya !')
else:
  print('Jangan menyerah, silahkan coba lagi nanti !')
  

