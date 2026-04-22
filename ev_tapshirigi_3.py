metn = "Men Baki seherinde yasayiram. Son zamanlar hava seraiti cox deyiskendir."
temiz_metn = metn.replace(".", "")
sozler = metn.split()
soz_sayi = len(sozler)

unikal_sozler = []
en_uzun_soz = ""
yeni_siyahi = []

for soz in sozler:
    if 'salam' in soz:
        break

    temiz_soz = soz.lower()
    if temiz_soz not in unikal_sozler:
     unikal_sozler.append(temiz_soz)

     if len(soz) > len(en_uzun_soz):
         en_uzun_soz = soz

     if len(soz) <= 4:
         continue

    yeni_siyahi.append(soz)



print(f"Umumi soz sayi: {soz_sayi}")
print(f"Unikal sozler:  {unikal_sozler}")
print(f"Unikal soz sayi: {len(unikal_sozler)}")
print(f"Ən uzun söz: {en_uzun_soz}")
print(f"4 hərfdən böyük olanlar: {yeni_siyahi}")