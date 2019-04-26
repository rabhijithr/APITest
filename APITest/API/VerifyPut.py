import requests
import json
# import jsonpath
import logging
import os
import configparser
from API.GetCall import Jparentlen, Jchildlen

# ------------------------------------------Configs---------------------------------------------------------------

config = configparser.ConfigParser()
config.read('Config/Config.ini')

JSONdirName = 'JSONFiles'
os.makedirs(JSONdirName, exist_ok=True)

LogdirName = 'LogFiles'
os.makedirs(LogdirName, exist_ok=True)

logging.info("#############################------------- PUT CALL ---------------################################")

logging.basicConfig(filename=os.path.abspath("{}/VerifyLogger.txt".format(LogdirName)), filemode="a",
                    format='%(asctime)s - %(message)s - %(levelname)s', level=logging.INFO)

try:
    # DWOutputfile = open(os.path.abspath("{}\DWH_GetApiOutput.json".format(JSONdirName)), "w")
    DWOutputfile = open(os.path.abspath("{}\FINAL_GetApiOutput.json".format(JSONdirName)), "a")
except IOError:
    print("File Not Found")

# --------------------------------------------Code----------------------------------------------------------------

Base_URL = config['POST/PUT_API_URL']['Base_URL']
Parameters = config['POST/PUT_API_URL']['Parameters']
try:
    res = requests.put(Base_URL + Parameters)
    logging.info("API PUT call happened")
except Exception as e:
    logging.exception("Api PUT Call not happened")

print(res.json())


if res.status_code == 200:
    Base_URL = config['GET_API_URL']['Base_URL']
    Parameters = config['GET_API_URL']['Parameters']

    res = requests.get(Base_URL + Parameters)
    # print(res)

    jres = res.json()

    Jresponce = json.dumps(jres)

    # print(jres)
    # print(json.dumps(jres, indent=4)) # printing output in JSON format with 4 space indent

    Jparentlen1 = str(len(jres))
    Jchildlen1 = str(len(jres['data']))

    DWOutputfile.write("PUT call responce code: {}\n\n ".format(res.status_code))
    json_output = DWOutputfile.write("DWH GET call responce:\n {}".format(Jresponce))
    DWOutputfile.write("\n")
    DWOutputfile.write("Lenth of DWH Parent Json is = {}\n".format(Jparentlen1))
    DWOutputfile.write("Lenth of DWH Child Json is = {}\n".format(Jchildlen1))

    if Jparentlen1 == Jparentlen:
        DWOutputfile.write("\nDW Parent count is same.\nParent count {}, DW Parent count {}, Difference = {}\n".format(Jparentlen, Jparentlen1, int(Jparentlen) - int(Jparentlen1)))
        print("DW Parent count is same.\nParent count {}, DW Parent count {}, Difference = {}\n".format(Jparentlen, Jparentlen1, int(Jparentlen) - int(Jparentlen1)))
    else:
        print("DW Parent count is not same.\nParent count {}, DW Parent count {}, Difference {}\n".format(Jparentlen, Jparentlen1, int(Jparentlen) - int(Jparentlen1)))

    if Jchildlen1 == Jchildlen:
        DWOutputfile.write("DW Child count is same.\nChild count {}, DW Child count {}, Difference = {}".format(Jchildlen, Jchildlen1, int(Jchildlen) - int(Jchildlen1)))
        print("DW Child count is same.\nChild count {}, DW Child count {}, Difference = {}".format(Jchildlen, Jchildlen1, int(Jchildlen) - int(Jchildlen1)))
    else:
        print("DW Child count not same.\nChild count {}, DW Child count {}, Difference = {}".format(Jchildlen, Jchildlen1, int(Jchildlen) - int(Jchildlen1)))
else:
    print("Actual responce code is = ", res.status_code)
    DWOutputfile.write("PUT call responce code is not 200, Actual Responce code: {}\n ".format(res.status_code))

