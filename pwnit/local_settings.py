# Mastercard Developers
# from .settings import *
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


CREDS = {
    'username': 'team4@labshackathon.com',
    'password': '79081A6F6FD3',
    'consumer_key': '8FMfiIcDwjyOVg99uIDWjPqQ4Nb10ShqjJ8ob0N10dca61c8!c77dd89a31f04cca8be58a0a633789500000000000000000',
    'keystore_password': 'keystorepassword',
    'key_alias': 'keyalias',
    'key_store_path': os.path.join(BASE_DIR, 'team4-money2020-1507583124-sandbox.p12'),
}
