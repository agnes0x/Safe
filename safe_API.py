import requests
import json
import pandas as pd

url = "https://safe-transaction-mainnet.safe.global/api/v1/safes/0xBbA4C8eB57DF16c4CfAbe4e9A3Ab697A3e0C65D8/multisig-transactions/"
response = requests.get(url).json()
df = response["results"]

while response["next"]:
    response = requests.get(response["next"]).json()
    df.extend(response["results"])

df = pd.DataFrame(df)

nrwalletconnect = df['origin'].str.contains('WalletConnect', na=False).sum()
