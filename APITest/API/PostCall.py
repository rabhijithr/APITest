import requests
import json
import jsonpath
import logging
import configparser
import os
# import coloredlogs

# ------------------------------------------Configs---------------------------------------------------------------

# coloredlogs.install() - to print console logs in color format

JSONdirName = 'POST_API'
os.makedirs(JSONdirName, exist_ok=True)

config = configparser.ConfigParser()
config.read('Config/Config.ini')

LogdirName = 'LogFiles'
os.makedirs(LogdirName, exist_ok=True)  # makedir - to validate if that folder exits, exist_ok=True - dont throw error

logging.basicConfig(filename=os.path.abspath("{}/Logger.txt".format(LogdirName)), filemode="w",
                    format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

# --------------------------------------------Code----------------------------------------------------------------

Base_URL = config['POST/PUT_API_URL']['Base_URL']
Parameters = config['POST/PUT_API_URL']['Parameters']

try:
    # InputFilePath = config['FILE']['InputFilePath']
    Inputfile = open(os.path.abspath("{}/PostApi.json".format(JSONdirName)), "r")
    print("file found")
except IOError:
    print("File not found")

request_json = json.load(Inputfile)  # used to load the value to/from the file
logging.info('File {} has been read'.format(__file__))
print(request_json)

# try catch block
try:
    res = requests.post(Base_URL + Parameters, request_json)
    logging.info("API call happened")
except Exception as e:
    logging.exception("Api call not happened")

# need to write the output to different file in JSON format
Outputfile = open(os.path.abspath("{}/PostApiOutput.json".format(JSONdirName)), "w")
json_output = Outputfile.write(res.text)

# validate responce code
assert res.status_code == 201

# To fetch headers
print("Content Type is = ", res.headers.get("Content-Type"))

res_json = json.loads(res.text)
print(res_json)

# pick id using jsonpath liberary stores and result to id as a list format
ApiId = jsonpath.jsonpath(res_json, 'id')

# fetching the first value in the list
print(ApiId[0])


