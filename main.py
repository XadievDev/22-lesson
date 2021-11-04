#XadievDev
#22-lesson.Moslashuvchan funksiya

#-------------------------------------------------------------------------------------#

# def summa(*sonlar):
#     """Sonlarni yig'indisini hisoblovchi funksiya"""
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi

# print(summa(1,2,3,4,5))

#-------------------------------------------------------------------------------------#

# def avto_info(kompaniya,model,**malumotlar):
#     """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
#     malumotlar['kompaniya']=kompaniya
#     malumotlar['model']=model
#     return malumotlar

# avto1 = avto_info("GM", "malibu", rang='qora', yil=2018)
# avto2 = avto_info("Kia", "K5", rang='qizil', narh=35000)

#-------------------------------------------------------------------------------------#

#Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing

# def kopaytir(*sonlar):
#     kopaytma = 1
#     for son in sonlar:
#         kopaytma *= son
#     return kopaytma
    
# print(kopaytir(2,3,4))

#-------------------------------------------------------------------------------------#

#Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing. Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.

# def talaba_tuz(ism,familya,**malumotlar):
#     malumotlar[ism] = ism
#     malumotlar[familya] = familya
#     return malumotlar

# print(talaba_tuz('amirbek','xadiev',tyil = 2006,fakultitet = 'it'))

#-------------------------------------------------------------------------------------#
