from pprint import pprint
from argparse import ArgumentParser

import requests
from requests.models import Response

parser = ArgumentParser()
parser.add_argument("--ip")
args = parser.parse_args()

ip_addr = args.ip

token: str = "token"

# response = requests.get(url="https://ipinfo.io/107.22.139.22", headers={"token": token})

def response_maker(ip_address: str) -> Response:
    new_url = f"https://ipinfo.io/{ip_address}"
    print()
    pprint(requests.get(url=new_url, headers={"token": token}).json())

print(response_maker(ip_addr))

