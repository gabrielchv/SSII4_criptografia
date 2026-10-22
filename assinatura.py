from datetime import datetime, timedelta, timezone

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.x509.oid import NameOID


def gerar_par_chaves():
    chave_privada = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    return chave_privada, chave_privada.public_key()


def gerar_certificado(chave_privada, chave_publica):
    nome = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "Gabriel Chaves")])
    certificado = (
        x509.CertificateBuilder()
        .subject_name(nome)
        .issuer_name(nome)  # autoassinado
        .public_key(chave_publica)
        .serial_number(x509.random_serial_number())
        .not_valid_before(datetime.now(timezone.utc))
        .not_valid_after(datetime.now(timezone.utc) + timedelta(days=365))
        .sign(chave_privada, hashes.SHA256())
    )
    return certificado


def assinar_arquivo(dados: bytes, chave_privada) -> bytes:
    return chave_privada.sign(dados, padding.PKCS1v15(), hashes.SHA256())


def conferir_assinatura(dados: bytes, assinatura: bytes, chave_publica) -> bool:
    try:
        chave_publica.verify(assinatura, dados, padding.PKCS1v15(), hashes.SHA256())
        return True
    except Exception:
        return False


arquivo = "documento.txt"
conteudo = b"Contrato de compra e venda - valor R$ 1.000,00"

chave_privada, chave_publica = gerar_par_chaves()
certificado = gerar_certificado(chave_privada, chave_publica)

assinatura = assinar_arquivo(conteudo, chave_privada)

print("Certificado gerado (autoassinado):", certificado.subject)
print("Assinatura (documento original):", assinatura.hex()[:64], "...")
print("Assinatura confere (original):", conferir_assinatura(conteudo, assinatura, chave_publica))
print("Assinatura confere (adulterado):", conferir_assinatura(b"texto alterado", assinatura, chave_publica))
