import json


with open("config.json", "r") as read_file:
    student = json.load(read_file)
    read_file.close()


student["text_lines"][0]["x"] = "10"
print(student["text_lines"][0]["text"])

with open("config.json", "w") as read_file:
    json.dump(student,read_file, indent=4)
    read_file.close()






