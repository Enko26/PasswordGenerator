
import random

harfler = [
    'a', 'b', 'c','ç', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö'
    'p', 'q', 'r', 's', 't', 'u','ü', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö','P', 'Q', 'R', 'S',
    'T', 'U','Ü', 'V', 'W', 'X', 'Y', 'Z'
]
sayilar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
semboller = ['!','?', '#', '$', '%', '&', '(', ')', '*', '+']

print("           Random güçlü şifreni oluştur! \n -12 karakter altında şifre oluşturmamaya özen göster- \n ")
harf_sayisi = int(input("Şifrenizde kaç adet harf olsun?\n"))
sembol_sayisi = int(input(f"Şifrenizde kaç adet sembol bulunsun?\n"))
numara_sayisi = int(input(f"Şifrenizde kaç adet sayı bulunsun?\n"))

sifre_listesi = []
for char in range(1, harf_sayisi + 1):
    sifre_listesi.append(random.choice(harfler))

for char in range(1, sembol_sayisi + 1):
    sifre_listesi += random.choice(semboller)

for char in range(1, numara_sayisi + 1):
    sifre_listesi += random.choice(sayilar)


random.shuffle(sifre_listesi)
sifre = ""
for char in sifre_listesi:
    sifre += char

print(f"Oluşturulan Şifren: {sifre}")
