from py_aaio.AAIO import AAIO
from py_aaio import models
from dotenv import load_dotenv
import os

load_dotenv()

AAIO_ID = os.getenv("AAIO_ID")
AAIO_KEY = os.getenv("AAIO_KEY")
AAIO_SECRET_1 = os.getenv("AAIO_SECRET_1")
AAIO_SECRET_2 = os.getenv("AAIO_SECRET_2")

def run():
    aaio = AAIO(AAIO_ID, AAIO_SECRET_1, AAIO_SECRET_2, AAIO_KEY)
    url = AAIO.get_ips()
    balance = aaio.get_balance()
    print(balance.balance)

if __name__ == "__main__":
    run()