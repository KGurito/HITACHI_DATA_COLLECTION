#IMPORTAÇÃO DE BIBLIOTECAS#
import pandas as pd
import datetime as dt
import requests, warnings, urllib3, json, sqlite3, os
from dotenv import load_dotenv


#SUPRESSÃO DE CERTIFICADOS SL#
warnings.simplefilter(action='ignore', category=FutureWarning)
urllib3.disable_warnings()

#INICIALIZAÇÃO .ENV#
load_dotenv()
api_key = os.getenv("APIKEY_HNCL03TC")
hncl03tc = os.getenv("HNCL03TC")



def get_filesystem(api_key, hnas_storage):
	url = f"https://{hnas_storage}:8444/v9/storage/filesystems"
	payload={}
	headers = {"X-Api-Key": api_key}

	try:
		response = requests.request("GET", url, headers=headers, data=payload, verify=False)
		response.raise_for_status()

		json_export = json.loads(response.text)
		return json_export

	except requests.exceptions.RequestException as e:
		print("ERROR na requisição!")
		print(f"Detalhes do erro: {e}")
		return None # Retorna vazio caso dê erro

data = get_filesystem(api_key, hncl03tc)
print(data)