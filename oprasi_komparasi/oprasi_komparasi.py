#oprasi komparasi 

#sertiap hasil oprasi adallah boolean
#true/false
# >, <, >=, <=, ==, !=, is not

a = 4
b = 5

#lebih besar dari >
print("=>LEBIH BESAR DARI (>)")
hasil = a > 2
print(a, '>' , 2 ,'=', hasil )
hasil = b > 8
print(a, '>' , 8 ,'=', hasil )
hasil = a > 4
print(a, '>' , 4 ,'=', hasil )

#kurang dari >
print("=>KURANG DARI (<)")
hasil = a < 2
print(a, '<' , 2 ,'=', hasil )
hasil = b < 8
print(a, '<' , 8 ,'=', hasil )
hasil = a < 4
print(a, '<' , 4 ,'=', hasil )

#leibh dari sama dengan >=
print("=>LEBIH DARI SAMADENGAN (>=)")
hasil = a >= 2
print(a, '>=' , 2 ,'=', hasil )
hasil = b >= 8
print(a, '>=' , 8 ,'=', hasil )
hasil = a >= 4
print(a, '>=' , 4 ,'=', hasil )

#kurang dari samadengan <=
print("=>KURANG DARI SAMADENGAN (<=)")
hasil = a <= 2
print(a, '<=' , 2 ,'=', hasil )
hasil = b <= 8
print(a, '<=' , 8 ,'=', hasil )
hasil = a <= 4
print(a, '<=' , 4 ,'=', hasil )

#leibh dari sama dengan ==
print("=>SAMADENGAN(==)")
hasil = a == 4
print(a, '==' , 4 ,'=', hasil)
hasil = b == 4
print(b, '==' , 4 ,'=', hasil)

#leibh dari sama dengan ==
print("=>SAMADENGAN(!=)")
hasil = a != 4
print(a, '!=' , 4 ,'=', hasil)
hasil = b != 4
print(b, '!=' , 4 ,'=', hasil)

# 'is' sebagai komparasi object identity
x = 5 #sebagai assigment membuat object
y = 5
print("nilai x =", x, "id =", hex(id(x)))
print("nilai x =", y, "id =", hex(id(y)))
hasil = x is not y
print("x is y =", hasil)
