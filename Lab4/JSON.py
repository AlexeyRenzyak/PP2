import json
file = open("Lab4\sample-data.json")
data = json.load(file)
print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")
for x in data["imdata"]:
    print(x["l1PhysIf"]["attributes"]["dn"],"                           ", x["l1PhysIf"]["attributes"]["descr"], x["l1PhysIf"]["attributes"]["speed"], " ", x["l1PhysIf"]["attributes"]["mtu"])
