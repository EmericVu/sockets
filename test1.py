code = (b'\xb8\x04\xde\xf7')
a = ""
octet2 = code.hex()
octet = ""
octet += octet2[-2:]
octet += octet2[4:6]
octet += octet2[2:4]
octet += octet2[:2]
print (octet)
for i in range (4) :
    oct1 = octet[:2]
    octet = octet.replace(oct1,"")
    decode = bin(int(oct1, base=16))
    print(decode)
    decode = decode.replace('0b',"")
    for i in range (len(decode)) :
        a += decode[i]

deci = 0
taillebinaire = len(a) 

for i in range (len(a)): 
    deci += int(a[taillebinaire - (i+1)])*pow(2, i) 

print("Valeur en decimal : ", deci)
