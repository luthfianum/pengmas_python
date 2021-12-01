# Membuat fungsi yang akan mengecek kebenaran dari sebuah jawaban
def checkguess(guess,answer):
    global score

    # Jika variabel 'still_guessing' bernilai True maka,
    # user masih dapat menjawab
    still_guessing = True
    attempt = 0
    
    # Perulangan dibawah digunakan untuk memberi kesempatan kepada user untuk menjawab
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('Jawaban Benar')
            
            #Jika user menjawab benar maka nilai bertambah
            score = score + 1
            
            still_guessing = False
        else:
            if attempt < 2:
                guess = input('Maaf Jawaban Salah. Coba Lagi! ')
            attempt = attempt + 1
    if attempt == 3:
        print('Jawaban Yang Benar adalah ' + answer)
        
# Diberikan skor awal yaitu '0' skor akan bertambah jika user menjawab dengan benar
score = 0

# Berikan pertanyaan kepada user untuk menjawab
print('Tebak Hewannya!')
guess1 = input('Hewan apa yang hidup di kutub utara? ')
checkguess(guess1, 'beruang kutub')
guess2 = input('Hewan apa yang paling cepat di darat? ')
checkguess(guess2, 'cheetah')
guess3 = input('Hewan apa yang paling besar? ')
checkguess(guess3, 'paus biru')

# Mencetak skor yang user dapatkan
print('Your score is ' + str(score))
