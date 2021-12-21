# import library
import os
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES

# memanggil key
def getKey(keysize): # untuk membuat kunci
    key = os.urandom(keysize) # membuat kunci secara random
    return key # mengembalikan nilai key


def getIV(blocksize): # membuat blok
    iv = os.urandom(blocksize) # membuat blok secara random
    return iv # mengembalikan nilai blok

# fungsi untuk enkripsi 
def encrypt_image(filename, key, iv):
    BLOCKSIZE = 16 # membuat ukuran blok 16
    encrypted_filename = "encrypted_" + filename

    with open(filename, "rb") as file1: # membuka file sebagai file1
        data = file1.read() # membaca file1

        # chiper melakukan method dari proses AES dengan key blocksize yang telah di tentukan
        cipher = AES.new(key, AES.MODE_CBC, iv)
        # proses enkripsi yang di gunakan chipertext dan data gambar yang sebelumnya
        ciphertext = cipher.encrypt(pad(data, BLOCKSIZE))

        # membuka file enkripsi tadi sebagai file 2
        with open(encrypted_filename, "wb") as file2:
        # pada file 2 di tuliskan di chipertext    
            file2.write(ciphertext)
    return encrypted_filename

# fungsi deskripsi 
def decrypt_image(filename, key, iv):
    BLOCKSIZE = 16 # membuat ukuran blok sepanjang 16
    decrypted_filename = "decrypted_" + filename # berfungsi untuk menampung nama file yang telah di deskripsikan kemudian menyimpan nya

    with open(filename, "rb") as file1: # membuka file sebagai file1
        data = file1.read() # membaca file1

        cipher2 = AES.new(key, AES.MODE_CBC, iv)
        decrypted_data = unpad(cipher2.decrypt(data), BLOCKSIZE)

        with open(decrypted_filename, "wb") as file2:
            file2.write(decrypted_data)

    return decrypted_filename # mengembalikan file yang di deskripsi


KEYSIZE = 16 # ukuran key yang di gunakan
BLOCKSIZE = 16 # ukuran blok yang di gunakan 
filename = "hacker.JPG"

key = getKey(KEYSIZE) # untuk memanggil nilai key
iv = getIV(BLOCKSIZE) # untuk memanggil nilai block

encrypted_filename = encrypt_image(filename, key, iv) # variabel encrypted_filename berfungsi menerima hasil encrypt_image
decrypted_filename = decrypt_image(encrypted_filename, key, iv) # variabel decrypted_filename menerima hasil dari fungsi decrypt_image
