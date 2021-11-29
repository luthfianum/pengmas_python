import random

# Tambahkan tingkat kesulitan 
difficulty = input('Pilih level (ketik 1, 2 or 3):\n 1 Easy\n 2 Normal\n 3 Hard\n')
if difficulty == '1':
  nyawa = 12
elif difficulty == '2':
  nyawa = 6
else:
  nyawa = 3

# perbanyak pilihan kata
daftar_kata_rahasia = ['twitter', 'spotify', 'webtoon', 'discord', 'facebook', 'google', ]

kata_rahasia = random.choice(daftar_kata_rahasia)

# Ubah panjang kata-kata dapat divariasikan
clue = list('?'*len(kata_rahasia))

heart_symbol = u'\u2764'

sudah_tertebak = False

unknown_letter = len(kata_rahasia)

def update_clue(huruf_tebakan, kata_rahasia, clue, unknown_letter):
  index = 0
  
  while index < len(kata_rahasia):
    if(huruf_tebakan == kata_rahasia[index]):
      clue[index] = huruf_tebakan
      unknown_letter = unknown_letter - 1
    index = index + 1
  return unknown_letter

while nyawa > 0:
  print(clue)
  
  print('Sisa nyawa : ' + (" " + heart_symbol) * nyawa )
  
  huruf_tebakan = input('Masukkan huruf tebakan anda : ')
  
  if huruf_tebakan == kata_rahasia :
    sudah_tertebak = True
    break
  
  if huruf_tebakan in kata_rahasia:
    unknown_letter = update_clue(huruf_tebakan, kata_rahasia, clue, unknown_letter)
  else: 
    print('Tebakan anda kurang tepat, nyawa anda berkurang 1')
    nyawa = nyawa - 1
    
  if unknown_letter == 0:
    sudah_tertebak = True
    break

if sudah_tertebak == True:
  print('Selamat, anda berhasil menebak kata rahasianya !')
else:
  print('Jangan menyerah, silahkan coba lagi nanti !')
  

