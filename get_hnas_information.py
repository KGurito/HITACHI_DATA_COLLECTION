#run: /home/storadm/.venv/bin/python3 /home/storadm/scripts_python/coleta_storages_hitachi/get_hnas_information.py
#IMPORTAÇÃO DE BIBLIOTECAS#
import pandas as pd
import datetime as dt
import requests, warnings, urllib3, json, sqlite3, os
from dotenv import load_dotenv
import data_parsec as dparsec


#SUPRESSÃO DE CERTIFICADOS SL#
warnings.simplefilter(action='ignore', category=FutureWarning)
urllib3.disable_warnings()


#INICIALIZAÇÃO .ENV PARA TESTES DE FUNÇÕES#
load_dotenv()

api_key = os.getenv("APIKEY_HNCL03TC")
hncl03tc = os.getenv("HNCL03TC")

data = dparsec.get_filesystem(api_key, hncl03tc)
hnas_fs_info_df = dparsec._parse_nested_json_to_df(data)
dparsec._export_report(hnas_fs_info_df)

print(hnas_fs_info_df)