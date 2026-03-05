#IMPORTAÇÃO DE BIBLIOTECAS#
import pandas as pd
import datetime as dt
import requests, warnings, urllib3, json, sqlite3

#SUPRESSÃO DE CERTIFICADOS SL#
warnings.simplefilter(action='ignore', category=FutureWarning)
urllib3.disable_warnings()

#DECLARAÇÃO DOS HNAS#
hncl03tc = '1.128.51.112'
hncl01sto = '1.128.51.155'
hncl02bkp = '1.128.51.143'


payload={}
headers = {
  'Authorization': 'Basic aG5hc2FwaTphcHByb290MQ=='
}