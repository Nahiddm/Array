status = True
peserta=[]
while status == True :
    print("===Just===")
    print(" 1.Mendaftarkan Peserta\n 2.Menghapus Peserta\n 3.Mencetak semua Peserta\n 0.Exit\n")
    pil=input("Masukkan pilihan anda:")
    if pil == "1":
        peserta.append(input("Masukkan Nama Peserta: "))
    elif pil =="2":
        peserta.remove(input("Masukkan Nama Peserta yang ingin di hapus:"))
    elif pil=="3":
        print (peserta)
    else:
        status= False 