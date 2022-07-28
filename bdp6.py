#!/usr/local/bin/python3.7

from requests.auth import HTTPBasicAuth
import requests
import json
import configparser,logging



config = configparser.ConfigParser()
config.read('/home/mcarrizo/scripts/stechs/config.ini')

HISTORY_LOG = config['DEFAULT']['HISTORY_LOG']
logging.basicConfig(format='%(asctime)s %(message)s', filename=HISTORY_LOG,filemode='a', level=logging.INFO)
USER = config['DEFAULT']['USER']
PASSWORD = config['DEFAULT']['PASSWORD']
URI = config['DEFAULT']['URL_API_BDP6']
credentials = HTTPBasicAuth(USER, PASSWORD)

def bdp6_cluster_1 ():
    try:
        response = requests.get(URI, auth=credentials, timeout=5, verify=False)

        #if not response.status_code == 200:
            #return "Error: Unexpected response {}".format(response)
        #print(response)
        #print(response.status_code)

        if response.status_code != 200:
            logging.error('BDP6 ERROR EL ENDPOINT NO RESPONDE OK :'+str(e))

            return "Error: Unexpected response {}".format(response)
            


        else:
            dict_bdp6 = response.json()
            logging.info("Diccionario bdp6")
            logging.info(dict_bdp6)

            results = dict_bdp6['bdp6_status']['status']

            if results in 'Running':
                status = 1
                #print('El estado del proceso de DHCPv6 del nodo activo esta: ', status)
            else:
                status = 0
                #print('El estado del proceso de DHCPv6 del nodo activo esta: ', status)

        #return status

        
    #except requests.exceptions.RequestException as err:
    except Exception as e:
        status = 0
        logging.error('BDP6 ERROR AL PROCESAR REQUEST :'+str(e))
        #print('Un error a ocurrido al procesar ', e)
    
    return status

print(bdp6_cluster_1())






    
   
