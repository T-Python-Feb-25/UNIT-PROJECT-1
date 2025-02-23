import os,json
METADATA_PATH  = r"C:\Users\Mohamed\tuwaiq\projects\EventManagement\UNIT-PROJECT-1\data\metadata.json"
EVENTS_PATH = r"C:\Users\Mohamed\tuwaiq\projects\EventManagement\UNIT-PROJECT-1\data\events.json"
USERS_FILEPATH  = r"C:\Users\Mohamed\tuwaiq\projects\EventManagement\UNIT-PROJECT-1\data\users.json"
def generate_unique_id(name,type=0,file_path=METADATA_PATH):
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            json.dump({name: 0}, file)

    with open(file_path, "r+") as file:
        data = dict(json.load(file))
        if name not in data:
            data[name] = 0  
        data[name] += 1
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()
    return data[name]   

