status = True
sifatkamu=set([])
while status == True :
    sk=(input("Masukkan sifat kamu: "))
    sifatkamu.add(sk)
    if sk == "selesai":
        break    
status= True
sifatdia=set([])
while status==True:
    sd=(input("Masukkan sifat dia: "))
    sifatdia.add(sd)
    if sd=="selesai":
        break
sifatkamu.remove("selesai")
sifatdia.remove("selesai")
print("SIFAT KAMU".center(50))
print(sifatkamu)
print("SIFAT DIA".center(50))
print(sifatdia)
persamaan=sifatdia.intersection(sifatkamu)
print("Persamaan dari sifat Kamu dan Dia".center(50))
print(persamaan)