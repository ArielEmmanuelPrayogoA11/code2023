import random
import string


# tahap 1 : shuffing key 
# def shuffle():
number_list = [5,6,7,8]
numberbin = [5,6,7,8]

random.shuffle(number_list)
generatedKey = ''.join(str(num) for num in number_list)
print("key : ",generatedKey)


# tahap 2: generate ke binary
def gen_bin():
    key1 = ""
 
    for i in range(8):
        temp = str(random.randint(0, 1))
        key1 += temp
    return(key1)
 
str1 = gen_bin()
print("\nyour binary number : \n",str1)

#tahap 3: belah jadi 2
Masterkey=str1[4:]
print("\nyour chopped binary:",Masterkey)


# tahap 4: tiap angka biner diberikan value sesuai angka random
def create_couple(list,Masterkey):
    dictionary = {}#template dict kosong

    for i, digit in enumerate(list):
        key = int(digit)  # Mengubah digit menjadi integer
        value = Masterkey[i]  # Mengambil huruf sesuai indeks

        dictionary[key] = value
    return dictionary

dict1=create_couple(numberbin,Masterkey)
print("\nyour new dictionary",dict1)





#tahap 5: ubah setiap digit angka random menjadi sebuah alphabet beurutan
def create_dictionary(number):
    alphabet = string.ascii_uppercase  # Mendapatkan urutan abjad dalam huruf kecil
    dictionary = {}

    for i, digit in enumerate(number):
        value = int(digit)  # Mengubah digit menjadi integer
        key = alphabet[i]  # Mengambil huruf sesuai indeks

        dictionary[key] = value

    return dictionary

generatedKey=create_dictionary(generatedKey)
print("your Generated key :",generatedKey)



# tahap 6 :pilih anggota random dari (AB, AC, AD, BC, BD, CD) & input 2 biner random dimasukan kedalam


my_list = ["AB","AC","AD","BC","BD","CD"]

random_member = random.choice(my_list)

print("\nyour random Member : ",random_member)

colok = input("Enter a random 2 digit biner: ")
print("User input :", colok)

#tahap 7: Subtitusi biner masterkey dengan biner dari user
def get_generatedKey(random_member,generatedKey):
    #menampilkan Member sebagai Key dari generatedKey
    newNum =[]
    for i in random_member:
        angka=generatedKey[i]
        newNum.append(angka)
        newNum.sort()

        
    return newNum

print("The biner where it ll get replaced :",get_generatedKey(random_member,generatedKey))

def subtisusi(colok,newNum,dict1):
    # loop string dari newnum yang tadi 2 angka 
    counter=0
    for i in newNum:
        # semisal 6
        key=int(i) 
        new_val=colok[counter]
        dict1[key]=new_val
        counter+=1
    values_list = list(dict1.values())
    return values_list

finalKey=subtisusi(colok,get_generatedKey(random_member,generatedKey),dict1)
print(finalKey)
finalKey = ''.join(str(bin) for bin in finalKey )

print("\nConverting it into a string : ",finalKey)

















