import requests

TWILIO_USER='AC9003466da274a63ce3b89cc7af77206c'
TWILIO_KEY='3547afae7bc6914767e5c0328742867a'

url = 'https://studio.twilio.com/v2/Flows/FW8a7532d88b376c20325797feaa2a6d89/Executions'




def initiate_human_call(phone_number):
    # initiate human call
    #print("initiating human call to {}".format(phone_number))

    body={
        "To": f"+1{phone_number}",
        "From": "+16413816523"
    }

    x = requests.post(url, data=body, auth=(TWILIO_USER,  TWILIO_KEY))

    print(x.text)