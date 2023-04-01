import random

def kata():
    list_pertanyaan = ["java", "python", "php", "html", "javascript", "kotlin", "cpp", "css"]
    return random.choice(list_pertanyaan)

def mulai():
    alfabet = 'abcdefghijklmnopqrstuvwxyz'
    pertanyaan = kata()
    sudah_ditebak = []
    percobaan = 3
    nilai = False

    print('MENEBAK BAHASA PEMOGRAMAN')
    print("Kata mengandung", len(pertanyaan), "huruf.")
    print("Anda memiliki", percobaan, "percobaan untuk menebak.")
    print("--------------------")

    while not nilai and percobaan > 0:
        kata_ditebak = ""
        for letter in pertanyaan:
            if letter in sudah_ditebak:
                kata_ditebak += letter
            else:
                kata_ditebak += "_"

        print("Tebakan saat ini: ", kata_ditebak)

        jawaban = input("Masukkan tebakan anda: ").lower()

        if jawaban == pertanyaan:
            nilai = True
            break
        else:
            if jawaban not in alfabet:
                print("Masukkan huruf alfabet.")
            elif jawaban in sudah_ditebak:
                print("Anda sudah menebak huruf tersebut.")
            elif jawaban not in pertanyaan:
                print("Tebakan anda salah, Silahkan Coba lagi.")
                percobaan -= 1
                sudah_ditebak.append(jawaban)
            else:
                print("Tebakan anda benar!")
                sudah_ditebak.append(jawaban)

     
        if kata_ditebak == pertanyaan:
                nilai = True
                break


    if nilai:
        print("Selamat! Kata tebakan anda benar.")
    else:
        print('Maaf Tebakan Anda Masih Salah, kata yang benar adalah', pertanyaan)

mulai()
