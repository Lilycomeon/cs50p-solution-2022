import requests
import sys
import json

if len(sys.argv) == 2:
    try:
         n = float(sys.argv[1])
    except:
        sys.exit("Command-line argument is not a number")
else:
    sys.exit("Missing command-line argument")


try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    response = r.json()
except requests.RequestException:
    print("RequestException")
    sys.exit("RequestException")
else:
    bitcoin = response['bpi']['USD']['rate_float']
    amount = n * bitcoin
    print(f"${amount:,.4f}")
