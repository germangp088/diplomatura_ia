import requests
import json

# Configuración
BASE_URL = "https://integration-api-staging.seedtalent.com"  # Cambia esto por la URL de tu servidor
LOGIN_ENDPOINT = f"{BASE_URL}/api/v1/auth/login"
GROUPS_ENDPOINT = f"{BASE_URL}/api/v1/groups/"

# Credenciales
login_data = {
    "integratorId": "d99a0161-c7ab-462a-9dfa-21dbd1b2853a",
    "apiKey": "3bf85747-9a28-4479-964f-01d9bd3f35fa"
}

def main():
    print("Login in...")
    login_response = requests.post(
        LOGIN_ENDPOINT,
        json=login_data,
        headers={"Content-Type": "application/json"}
    )

    if login_response.status_code != 200:
        print(f"Error en login: {login_response.status_code}")
        print(f"Respuesta: {login_response.text}")
        return
    
    login_result = login_response.json()
    bearer_token = login_result.get("token")
    
    if not bearer_token:
        print("Error: No se recibió token en la respuesta")
        print(f"Respuesta completa: {json.dumps(login_result, indent=2)}")
        return
    
    print(f"Login successful! Token obtained: {bearer_token[:20]}...")
    
    print("\nGetting groups...")
    groups_response = requests.get(
        GROUPS_ENDPOINT,
        headers={
            "Authorization": f"Bearer {bearer_token}",
            "Content-Type": "application/json"
        }
    )
    
    # Verificar si la petición fue exitosa
    if groups_response.status_code != 200:
        print(f"Error getting groups: {groups_response.status_code}")
        print(f"Response: {groups_response.text}")
        return
    
    # Mostrar los grupos obtenidos
    groups = groups_response.json()
    print(f"\nGroups obtained successfully!")
    print(f"Total groups: {len(groups)}")
    print(f"\nGroups:")
    print(json.dumps(groups, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()

