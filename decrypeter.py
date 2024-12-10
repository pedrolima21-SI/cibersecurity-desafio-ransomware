import os
import pyaes


def descriptografar_arquivo(file_name):
 
    encrypted_file = file_name + ".ransomwaretroll"
    key_file = file_name + ".key"

   
    if not os.path.exists(encrypted_file):
        print(f"Erro: O arquivo criptografado {encrypted_file} não existe.")
        return
    if not os.path.exists(key_file):
        print(f"Erro: O arquivo de chave {key_file} não existe.")
        return

  
    with open(encrypted_file, "rb") as file:
        encrypted_data = file.read()

  
    with open(key_file, "rb") as keyfile:
        key = keyfile.read()

 
    aes = pyaes.AESModeOfOperationCTR(key)
    decrypted_data = aes.decrypt(encrypted_data)

   
    os.remove(encrypted_file)

  
    new_file = file_name
    with open(new_file, "wb") as new_file_obj:
        new_file_obj.write(decrypted_data)

    print(f"Arquivo descriptografado salvo como: {new_file}")


file_name = "teste.txt"  
descriptografar_arquivo(file_name)
