z = {
                "patient": {
                    "gender": "female",
                    "first_name": "Sally",
                    "last_name": "Adams",
                    "dob": "1950-01-01",
                    "generalPractitioner": [
                        {
                            "display": "Dr. Jonathan Chang",
                            "specialty": "Cardiologist"
                        }
                    ],
                    "address": {
                        "display": "58 STETSON PL, DUXBURY, MA, 02332-4507, US",
                        "use": "home"
                    }, 
                    "timezone": "America/New_York",
                    "preferred_pharmacy": {
                        "id": "dfd40c44-f79f-4b07-9b51-fcc53f286e06"
                    }
                },
                "conditions": [
                    {
                        "display": "Congestive Heart Failure",
                        "active": True
                    }
                ],
                "procedures": [],
                "medications": [
                    {
                        "name": "Lasix",
                        "display": "Lasix 20 mg oral tablet",
                        "dosage": "20mg oral twice a day",
                        "active": True,
                        "new": True,
                        "pharmacy": {
                            "id": "dfd40c44-f79f-4b07-9b51-fcc53f286e06"
                        }
                    },
                    {
                        "name": "potassium",
                        "display": "Potassium 20 milliequivalent oral tablet",
                        "dosage": "40 milliequivalent once a day",
                        "active": True
                    },
                    {
                        "name": "Metoprolol",
                        "display": "Metoprolol 25 mg oral tablet",
                        "dosage": "12.5 mg once a day",
                        "active": True,
                        "pharmacy": {
                            "id": "dfd40c44-f79f-4b07-9b51-fcc53f286e06"
                        }
                    },
                    {
                        "name": "Lisinopril",
                        "display": "Lisinopril 10 mg oral tablet",
                        "dosage": "10 mg daily",
                        "active": True,
                        "new": True,
                        "pharmacy": {
                            "id": "dfd40c44-f79f-4b07-9b51-fcc53f286e06"
                        }
                    },
                    {
                        "name": "Tylenol",
                        "display": "Tylenol 500 mg oral tablet",
                        "dosage": "1000mg every 8 hours as needed",
                        "active": True
                    }
                ],
                "clinical_notes": []
            }

def print_patient_info(patient_info):
    patient_str = ""
    patient_str += "Name:" + patient_info["patient"]["first_name"] + " " + patient_info["patient"]["last_name"]


    print(patient_str)

print_patient_info(z)