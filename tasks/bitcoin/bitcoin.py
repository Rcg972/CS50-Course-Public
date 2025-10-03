import sys
import requests

API_KEY = "4d84bafcf6af3cfe027095c04f7adc6c48200e9af9890e4069a8a74ac1df8aa1"
url = "https://rest.coincap.io/v3/assets/bitcoin"
headers = {"Authorization": f"Bearer {API_KEY}"}

def main():
    try:
        if len(sys.argv) < 2:
            sys.exit("Missing command-line argument")
        inputan = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    price_btc(inputan)


def get_resp():
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        sys.exit(f"Error: {e}")


def price_btc(a):
    data = get_resp().json()
    harga_btc = a * float(data["data"]["priceUsd"])
    print(f"${harga_btc:,.4f}")

main()
