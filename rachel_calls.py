import requests


url = 'https://eval.hippocraticdev.com:447/dt/api/patients/890dcd9c-c591-45fb-1989-7c8bda3f68b5/calls'


# call_id = requests.post(url)
# call_id = call_id.json()['call_id']
# print(call_id)
call_id = ''

start_call_url = 'https://eval.hippocraticdev.com:447/dt/api/patients/890dcd9c-c591-45fb-1989-7c8bda3f68b5/calls/' + call_id

data = {
    "llm_model": "G16:llama-base__loracpt-3__align-5",
    "script_id": "ba2cfc19-df30-4659-9995-43406c505407",
    "nurse_id": "ed9ca802-fb12-46d8-8298-dae2d2e7f81c",
    "asr_service": "dg-on-prem-nova-2-medical",
    "patient_name": "Eduardo Hardy",
    "llm_streaming": True,
    "template_name": "neel_v2",
    "tts_streaming": False,
    "other_settings": {
      "USE_TOPIC_DETECTION": False
    },
    "support_engines": [
      "dob-verification-engine",
      "identity-verification-engine",
      "lab-engine"
    ],
    "phone_number": "707-653-6854"
  }


# start_call = requests.post(start_call_url, json=data)
# print(start_call.text)

def initiate_rachel_call(phone_number):
    # initiate human call
    print("initiating rachel call to {}".format(phone_number))