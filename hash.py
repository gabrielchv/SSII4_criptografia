import hashlib


def calcular_hash(mensagem: str) -> str:
    return hashlib.sha256(mensagem.encode()).hexdigest()


def calcular_hash_arquivo(caminho: str) -> str:
    h = hashlib.sha256()
    with open(caminho, "rb") as f:
        for bloco in iter(lambda: f.read(4096), b""):
            h.update(bloco)
    return h.hexdigest()


def conferir_hash(mensagem: str, hash_esperado: str) -> bool:
    return calcular_hash(mensagem) == hash_esperado


mensagem = "Minha senha ultrassegreta 123"
hash_gerado = calcular_hash(mensagem)

print("Mensagem original:", mensagem)
print("Hash SHA-256 calculado:", hash_gerado)
print("Hash confere (mensagem correta):", conferir_hash(mensagem, hash_gerado))
print("Hash confere (mensagem adulterada):", conferir_hash("mensagem diferente", hash_gerado))
