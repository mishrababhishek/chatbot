import json 
config_file_path = "config.json"
config_file_object = open(config_file_path, "r")
config_file = json.load(config_file_object)
