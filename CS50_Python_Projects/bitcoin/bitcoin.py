from sys import argv, exit
import requests

if len(argv) < 2:
    exit("Missing command-line argument")
elif argv[1].isalpha():
    exit("Command-line argument is not a number")
elif len(argv) > 2:
    exit("Too many command-line arguments")
try:
    float_argv = float(argv[1])
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    dic = r.json()
    dic = dic["bpi"]["USD"]["rate"]
    dic = dic.replace(",", "")
    amount = float(dic) * float_argv

    print(f"${amount:,.4f}", end="")
except requests.RequestException:
    exit("There was an ambiguous exception that occurred while handling your request.")
