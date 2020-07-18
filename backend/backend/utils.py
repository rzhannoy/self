import secrets


def gen_random_string(limit=20, n_bytes=32):
    return secrets.token_hex(n_bytes)[:limit]
