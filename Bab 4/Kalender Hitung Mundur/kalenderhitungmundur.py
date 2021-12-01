# Mengimport modul tkinter untuk membuat canvas
# Mengimport modul datetime untuk mendapatkan tanggal sekarang dan mengubah teks menjadi tanggal
from tkinter import Tk, Canvas, font
from datetime import date, datetime

# Membuat fungsi untuk mengambil data dari events.txt ke dalam program
def get_events():
    # Semua data pada events.txt akan di simpan pada list_events
    list_events = []
    with open('events.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            current_event = line.split(',')
            event_date = datetime.strptime(current_event[1], '%d/%m/%y').date()
            current_event[1] = event_date
            list_events.append(current_event)
    return list_events

# Membuat fungsi yang akan menghitung selisih waktu dari tanggal sekarang hingga tanggal event
def days_between_dates(date1, date2):
    time_between = str(date1 - date2)
    number_of_days = time_between.split(' ')
    return number_of_days[0]

# Membuat canvas sebagai background dari kalender hitung mundur
root = Tk()
c = Canvas(root, width=800, height=800, bg='black')
c.pack()
c.create_text(100, 50, anchor='w', fill='orange',\
    font = 'Arial 28 bold underline', text='Kalender Hitung Mundur Saya')

# memanggil fungsi get_events() untuk mengambil daftar events
events = get_events()

# Mengambil data tanggal hari ini
today = date.today()

# Mengatur space vertikal agar program terlihat rapi
vertical_space = 100


for event in events:
    event_name = event[0]
    days_until = days_between_dates(event[1], today)
    
    # Menampilkan perhitungan mundur dari event
    display = 'It is %s days until %s' % (days_until, event_name)
    c.create_text(100, 100, anchor='w', fill='lightblue', \
       font='Arial 11 bold', text=display)
    
    #Menambahkan jarak agar kalender hitung mundur terlihat rapi
    vertical_space = vertical_space + 30