from cryptography.fernet import Fernet

def criptografar_mensagem(mensagem_texto: str) -> tuple[bytes, bytes]:
    chave = Fernet.generate_key()
    f_encriptador = Fernet(chave)
    
    mensagem_bytes = mensagem_texto.encode()
    dados_criptografados = f_encriptador.encrypt(mensagem_bytes)
    
    return dados_criptografados, chave



def descriptografar_mensagem(dados_criptografados: bytes, chave_para_abrir: bytes) -> str:
    f_descriptador = Fernet(chave_para_abrir)
    
    mensagem_bytes = f_descriptador.decrypt(dados_criptografados)
    return mensagem_bytes.decode()



texto_secreto = "Minha senha ultrassegreta 123"
token, minha_chave = criptografar_mensagem(texto_secreto)

print("Dados Criptografados:", token)
print("Chave gerada (você precisa enviar isso):", minha_chave)

texto_original = descriptografar_mensagem(token, chave_para_abrir=minha_chave)
print("Texto Descriptografado passando a chave:", texto_original)
