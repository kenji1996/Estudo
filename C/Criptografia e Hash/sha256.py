import hashlib

senha = 'testandosenha'
senha_bytes = str.encode(senha)

"""essa função converte uma senha EM BYTES para um hash
Password Based Key Derivation function 2
Hash-based Message Authentication Code
Desgraca confusa do caralho"""

senha_sha256 = hashlib.pbkdf2_hmac("sha256", senha_bytes, b"", 100000).hex()

print(senha)
type(senha_bytes)