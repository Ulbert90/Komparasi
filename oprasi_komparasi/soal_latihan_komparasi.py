#komparasi

#-----0+++++5------8+++++11------
inputUser = float(input("masukan angka yang bernilai lebih dari 0\n atau\n kurang dari 11\n:" ))

#----0++++
KurangDari= (inputUser <-11)
print("kurang dari 0 =", KurangDari)

#---0+++5
LebihDariSamadengan= (inputUser >=0)
print("lebih  dari 0 =", LebihDariSamadengan)

#+++5----8
KurangDariSamadengan= (inputUser <=5)
print("kurang dari 5 =", KurangDariSamadengan)

#----8++++11
LebihDariSamadengan = (inputUser >=8)
print("lebih  dari 8 =", LebihDariSamadengan)

#++++11-----
KurangDariSamadengan= (inputUser <=11)
print("kurang dari 11 =", KurangDariSamadengan)

Benar = LebihDariSamadengan and KurangDariSamadengan and KurangDari
print("angka yang anda masukan: ", Benar)