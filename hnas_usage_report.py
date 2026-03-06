#!/usr/bin/env python3
# run: /home/storadm/.venv/bin/python3 /home/storadm/scripts_python/coleta_storages_hitachi/get_hnas_information.py

# IMPORTAÇÃO DE BIBLIOTECAS #
import os
import json
import sqlite3
import smtplib
import warnings
import urllib3
import requests
import pandas as pd
import datetime
from dotenv import load_dotenv
import data_parsec as dparsec

def main():
	# SUPRESSÃO DE AVISOS E CERTIFICADOS SSL #
	warnings.simplefilter(action='ignore', category=FutureWarning)
	urllib3.disable_warnings()

	# INICIALIZAÇÃO .ENV #
	load_dotenv()
	
	# OBTENÇÃO DAS VARIÁVEIS DE AMBIENTE #
	api_key = os.getenv("APIKEY_HNCL03TC")
	hncl03tc = os.getenv("HNCL03TC")
	
	# VALIDAÇÃO (Garante que o script não quebre de forma obscura se o .env falhar)
	if not api_key or not hncl03tc:
		print("Erro: Variáveis de ambiente APIKEY_HNCL03TC ou HNCL03TC não encontradas no arquivo .env.")
		return


	# EXECUÇÃO DA ROTINA PRINCIPAL #
	try:
		data = dparsec.get_filesystem(api_key, hncl03tc)
		hnas_fs_info_df = dparsec._parse_nested_json_to_df(data)
		dparsec._export_report(hnas_fs_info_df)
			
	except Exception as e:
		print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Ocorreu um erro durante a execução: {e}")


	# ENVIO POR E-MAIL #
	try:
		servidor_email = smtplib.SMTP('smtp.gmail.com', 587)
	
	except:
		print("Erro ao se conectar ao servidor de e-mail")
	
	servidor_email.login("user", "password")

	# TRANSFORMA O RELATÓRIO EM STRING #
	report_time = datetime.datetime.now().strftime('%Y-%m-%d')
	df = pd.read_csv(f"./reports/hnas_usage_report_{report_time}.csv")
	texto_hnas_usage = df.to_string()

	remetente = "TS_BRA_STO_SUPPORT@t-systems.com"
	destinatarios = "TS_BRA_STO_SUPPORT@t-systems.com"
	texto = f"Relatório de utilização dos FileSystems - HNCL03TC\n\n\n{texto_hnas_usage}\n\n"

	servidor_email.sendmail(remetente, destinatarios, texto)
	  
if __name__ == "__main__":
	main()
