import string 

try:
    key = input("Key: ")
    if key.isalpha() and len(key) != 26:
        raise ValueError("Number of characters must be equal to 26.")
    elif not key.isalpha() and len(key) == 26:
        raise ValueError("Key must only contain alphabetical characters.")
    elif not key.isalpha() and len(key) != 26:
        raise ValueError("Key must contain 26 alphabetical characters.")
    else:
        pass
except ValueError as message:
    print(message)
    exit()

"""
try:
    key = input("Key: ")
    assert len(key) == 26 and key.isalpha()
except:
    print("Key must contain 26 alphabetical characters.")
    quit()
"""
key = key.upper() #key uppercase'e çevrilir

alphabet_list = list(string.ascii_uppercase) #uppercase alfabe karakterleri listelenir.

for char in alphabet_list:
    if key.count(char)!= 1: #count fonksiyonu kullanılarak alfabedeki karakterlerin key içindeki tekrarları incelenir.
        print("Key must contain different characters.")
        exit() #hatayla karşılaşılırsa program sonlarılır.        

"""
#alternatif

buffer = [0] * 26

for i in range(26):
    if buffer[ord(key[i]) - 65] == 0:
        buffer[ord(key[i]) - 65] += 1 
    
    else: 
        print("Key must contain different characters.")
        exit()
"""

plain_text = input("Plain text: ")
cipher_text = list(plain_text) #şifrelenecek text için liste oluşturulur çünkü stringler değiştirilemezdir, kopyalanmış alfabetik olmayan karakterler değiştirilmez.

for i in range(len(plain_text)):
    #harfler dışındaki işaretler şifrelenmez ve büyük harf küçük harf uyumuna dikkat edilir.
    if plain_text[i].isupper():
        cipher_text[i] = key[alphabet_list.index(plain_text[i])] #plain_textte sıradaki harfin, alfabede kaçıncı sırada olduğu öğrenilirek key'de karşılık gelen harfle değiştirilir.

    if plain_text[i].islower():
        cipher_text[i] = key[alphabet_list.index(plain_text[i].upper())].lower() #ord metodu ve char aritmetiği -> ord(plain_text[i]) - 97


print("Cipher text:", "".join(cipher_text))
