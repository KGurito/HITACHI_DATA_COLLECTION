import pandas as pd
import json, requests, datetime

# Run: /home/storadm/.venv/bin/python3 /home/storadm/scripts_python/nas_monitoring/hnas-api_collect_to_db.py

def _parse_nested_json_to_df(data):
    new_df = pd.json_normalize(data.json()['filesystems'])
    return new_df

def _export_report(df):
	report_time = datetime.datetime.now().strftime('%Y-%m-%d')
	output = df.to_csv(f"./reports/hnas_usage_report_{report_time}.csv",index=False)
	return output

def get_filesystem(api_key, hnas_storage):
	url = f"https://{hnas_storage}:8444/v9/storage/filesystems"
	payload = {}
	headers = {"X-Api-Key": api_key}

	try:
		response = requests.request("GET", url, headers=headers, data=payload, verify=False)
		response.raise_for_status()
		#json_export = json.loads(response.text)
		return response

	except requests.exceptions.RequestException as e:
		print("ERROR na requisição!")
		print(f"Detalhes do erro: {e}")
		return None # Retorna vazio caso dê erro
