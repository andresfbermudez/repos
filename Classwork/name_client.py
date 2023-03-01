import requests

out_data = {"name": "Andres Bermudez", "net_id": "afb38",
            "email": "afb38@duke.edu"}
r = requests.post("http://vcm-21170.vm.duke.edu:5000/student", json=out_data)
print(r.status_code)