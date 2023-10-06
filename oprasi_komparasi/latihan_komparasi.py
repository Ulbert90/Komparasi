#latihan logika dan komparasi

#membuat gabungan area rentang dari angka

#+++++++5=========10++++++++

inputUser =  float(input("masukan angka yang bernilai \nkurang dari 5 \natau \nlebih besar dari 10 \n:"))

#+++++5=======
#memeriksa angka kurang dari 5
isKurangDari = (inputUser < 5)
print("kurang  dari 5 =", isKurangDari)

#====10+++++
#memeriksa angka kurang dari 5
isLebihDari = (inputUser > 10)
print("Lebih  dari 10 = ", isLebihDari)

#+++++++5=========10++++++++

isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukan: ", isCorrect)


#-----5+++++10-----
#kasus irisan
print("\n",10*"=","\n")
inputUser =  float(input("masukan angka yang bernilai \nlebih dari 5 \ndan \nlkurang  dari 10 \n:"))

#-----5++++
#lebih dari 5
isLebihDari = inputUser > 5
print("lebih dari 5 =", isLebihDari)

#++++10-----
#kurang dari 10
isKurangDari = inputUser < 10
print("kurang dari 10 =", isKurangDari)

#-----5+++++10-----
isCorrect = isKurangDari and isLebihDari
print("angka yang anda masukan: ", isCorrect)