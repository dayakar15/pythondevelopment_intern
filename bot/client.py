from binance.client import Client

API_KEY = "0Clusy4hhVIUn7oxA3YOsWQJPaQB5RMfr8Z8cc2EBaG0sL055MEnQRwfoG33D2yu"
API_SECRET = "O1JFyERayQJL45JIdCeLejqIR4mP1vibhSd6KmPy6DPkhseh1zuhfWUc1cGOnZW3"

def get_client():
    return Client(API_KEY, API_SECRET, testnet=True)