import requests
import json
import os
import configparser
import logging

# ------------------------------------------Configs---------------------------------------------------------------

JSONdirName = 'JSONFiles'
os.makedirs(JSONdirName, exist_ok=True)

config = configparser.ConfigParser()
config.read('Config/Config.ini')

LogdirName = 'LogFiles'
os.makedirs(LogdirName, exist_ok=True)

logging.basicConfig(filename=os.path.abspath("{}/VerifyLogger.txt".format(LogdirName)), filemode="w",
                    format='%(asctime)s - %(message)s - %(levelname)s', level=logging.INFO)
logging.info("#############################------------- GET CALL ---------------################################")

try:
    # Outputfile = open(os.path.abspath("{}\STAGE_GetApiOutput.json".format(JSONdirName)), "w")
    Outputfile = open(os.path.abspath("{}\FINAL_GetApiOutput.json".format(JSONdirName)), "w")
except IOError:
    print("File Not Found")
    logging.info("File Not Found")

# ------------------------------------------Code------------------------------------------------------------------

# Base_URL = "https://reqres.in"
# param = "/api/users?page=2"

Base_URL = config['GET_API_URL']['Base_URL']
Parameters = config['GET_API_URL']['Parameters']

try:
    res = requests.get(Base_URL + Parameters)
    logging.info("API GET call happened")
except IOError:
    logging.exception("Api Call not happened")
# print(res)

jres = res.json()

Jparentlen = str(len(jres))
Jchildlen = str(len(jres['data']))

Jresponce = json.dumps(jres)


# if __name__ == "__main__":

# print(json.dumps(jres, indent=4))  # indednt responce with 4 spaces
json_output = Outputfile.write("RAW/STAGE GET call responce:\n {}".format(Jresponce))
Outputfile.write("\n\n")

Outputfile.write("Lenth of STAGE Parent Json is = {}\n".format(Jparentlen))
Outputfile.write("Lenth of STAGE Child Json is = {} \n\n".format(Jchildlen))
# Outputfile.write("\n")

print("Lenght of parent JSON = {}\nLength of child JSON = {}".format(Jparentlen, Jchildlen))

logging.info("Get Call Completed")
pass
