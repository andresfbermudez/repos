import requests

r = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/afb38")
ids = r.json()

blood_types = [requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/"+ids["Donor"]).text,
               requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/"+ids["Recipient"]).text]
if blood_types[0] == blood_types[1]:
   print("Match")
out_data = {"Name": "afb38", "Match": "Yes"}
r = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check", json=out_data)
print(r.text)
