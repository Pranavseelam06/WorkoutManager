import json 

def load_data(file_name):
     with open(file_name, "r") as file:
        lines = json.load(file)
        list = []
        log = lines["logs"]
        list.append(lines["profile"])
        list.append(lines["logs"])
        list.append(int(log[-1]["day"]))
        return list
     
def write_data(file_name, user_exists, log):
     with open(file_name, "w") as file:
        data = {

        }
        data["profile"] = user_exists
        data["logs"] = log
        json.dump(data, file, indent=4)