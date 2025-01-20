# Hangman Games using Python
# by Nadhif Rif'at Rasendriya

import bahan
import random

# Judul
print(bahan.title)

# Aturan permainan
print('''Aturan Permainan :
1. Selamatkan 'Nadhif' dengan cara menjawab pertanyaan dengan benar!
2. Budi hanya memiliki 6 nyawa!
3. 1 Kesalahan akan mengurangi 1 nyawa Nadhif!
''')

ready = input('Nyawa Budi ada di tanganmu, apakah kamu siap (y/n)? ').strip().lower()

if ready == 'y':
    with open('Day14_Project2/pertanyaan.txt', 'r') as f:
        list_pertanyaan = f.readlines()
    
    with open('Day14_Project2/jawaban.txt', 'r') as f:
        list_jawaban = f.readlines()
    
    nyawa_budi = 6  
    
    while nyawa_budi > 0:
        # Print hangman dari bahan sesuai jumlah kesalahan
        print(bahan.hangman[6 - nyawa_budi])

        # Pilih pertanyaan secara acak
        choose = random.randint(0, len(list_pertanyaan) - 1)

        print(f'Pertanyaan: {list_pertanyaan[choose]}', end='')
        
        user_answ = input('Jawabanmu: ').strip().lower()
        correct_answer = list_jawaban[choose].strip().lower()

        # Cek jawaban
        if user_answ == correct_answer:
            print('Jawaban benar!')
            print(bahan.congrats)
        else:
            print(f'Jawaban salah! Jawaban yang benar: {correct_answer}')
            nyawa_budi -= 1
            
        if nyawa_budi == 0:
            print(bahan.rose)
            print('Kamu gagal menyelamatkan Budi!')
            break

        next_question = input('Lanjut ke pertanyaan berikutnya? (y/n): ').strip().lower()
        if next_question != 'y':
            print('Terima kasih telah bermain!')
            break
# End
else:
    print(bahan.hangman[5])
    print('Terima kasih telah bermain!')
