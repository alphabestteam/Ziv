import json

with open("person_info.json", "r") as json_file:
    converted_json_dict = json.load(json_file)
print(converted_json_dict)

converted_json_dict["Name"] = "Ziv"
converted_json_dict["Age"] = "19"
converted_json_dict["City"] = "Kiryat Ono"

with open("new_json.json", "w") as loading_file:
    json.dump(converted_json_dict, loading_file)
