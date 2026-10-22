from cryptography.hazmat.primitives.asymmetric import rsa, padding

def criptografar_mensagem(mensagem_texto: str) -> tuple[bytes, rsa.RSAPrivateKey]:
    chave_privada = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    chave_publica = chave_privada.public_key()
    
    dados_criptografados = chave_publica.encrypt(mensagem_texto.encode(), padding.PKCS1v15())
    return dados_criptografados, chave_privada



def descriptografar_mensagem(dados_criptografados: bytes, chave_para_abrir: rsa.RSAPrivateKey) -> str:
    mensagem_bytes = chave_para_abrir.decrypt(dados_criptografados, padding.PKCS1v15())
    return mensagem_bytes.decode()



texto_secreto = "Minha senha ultrassegreta 123"
token, minha_chave = criptografar_mensagem(texto_secreto)

print("Dados Criptografados:", token)
print("Chave gerada:", minha_chave)

texto_original = descriptografar_mensagem(token, chave_para_abrir=minha_chave)
print("Texto Descriptografado passando a chave:", texto_original)
