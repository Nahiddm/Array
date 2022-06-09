print("NOTES TEMAN BARU".center(50))
status=True
teman=[]
while status==True:
    tb=input("Masukkan Nama Teman Baru : ")
    teman.append(tb)
    if tb=="selesai":
        teman.remove("selesai")
        print("Teman-Teman Baru".center(50))
        print(teman)
        break