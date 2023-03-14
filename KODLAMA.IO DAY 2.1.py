print("\t**********Öğrenci Kayıt Sistemine hoşgeldiniz**********\t")

ogrenciler = {}

def ogrenci_ekleme():
    
 
    while True:
        num_of_students = input("Kaç öğrenci eklemek istiyorsunuz? ")
        if not num_of_students.isdigit():
            print("Lütfen geçerli bir sayı girin.")
        else:
            num_of_students = int(num_of_students)
            break
    for i in range(num_of_students):
        ogrenci_no = input("Öğrenci numarasını girin: ")
        name = input("Öğrencinin adını ve soyadını girin: ")
        ogrenciler[ogrenci_no] = name
        print("Öğrenci eklendi.")
    while True:
        secim = input("1. Menüye dön\n2. Devam et\nSeçiminiz: ")
        if secim == "1":
            break
        elif secim == "2":
            ogrenci_ekleme()
        else:
            print("Geçersiz seçim.") 


def ogrenci_silme():
    n = int(input("Kaç öğrenci silmek istiyorsunuz?: "))
    for i in range(n):
        ogrenci_no = input("Silmek istediğiniz öğrenci numarasını girin: ")
        if ogrenci_no in ogrenciler:
            del ogrenciler[ogrenci_no]
            print("Öğrenci silindi.")
        else:
            print("Öğrenci bulunamadı.")


def tum_ogrencileri_goruntule():

 if  not ogrenciler :
        print("Kayıtlı öğrenci yok.")
 else:
        print("Öğrenci numarası\tÖğrenci adı")
        for student_no, name in ogrenciler.items():
            print(student_no, "\t\t", name)

def tek_ogrenci_goruntule():
    ogrenci_no = input("Bilgilerini görüntülemek istediğiniz öğrenci numarasını girin: ")
    if ogrenci_no in ogrenciler:
         print("Öğrenci numarası: ", ogrenci_no)
         print("Öğrenci adı: ", ogrenciler[ogrenci_no])
    else:
        print("Öğrenci bulunamadı.")

while True:
    print("\nÖğrenci Kayıt Sistemi")
    print("1. Öğrenci ekle")
    print("2. Öğrenci sil")
    print("3. Tüm öğrencileri görüntüle")
    print("4. Öğrenci bilgilerini görüntüle")
    print("5. Çıkış yap")


    secim = input("Seçiminizi girin: ")




    if secim == "1":
            ogrenci_ekleme()
    elif secim == "2":
            ogrenci_silme()
    elif secim == "3":
            tum_ogrencileri_goruntule()
    elif secim == "4":
            tek_ogrenci_goruntule()
    elif secim == "5":
        break
    else:
        print("Geçersiz seçim.")