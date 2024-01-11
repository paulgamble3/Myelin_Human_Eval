import streamlit as st
import random
import glob
import random
import json

from human_calls import initiate_human_call
from rachel_calls import initiate_rachel_call

call_probs = {
    "rachel": 0,
    "human": 1
}

def sample_patient_info():
    patient_files = glob.glob("patient_info/*json")
    patient_file = random.choice(patient_files)
    with open(patient_file, "r") as f:
        patient_info = json.load(f)

    return patient_info

def display_patient_info(patient_info):
    st.write("Here is some information about your patient:")
    st.subheader("Name")
    st.write(patient_info["patient"]["first_name"] + " " + patient_info["patient"]["last_name"])
    st.subheader("Date of Birth")
    st.write(patient_info["patient"]["dob"])
    st.subheader("Conditions")
    for cond in patient_info["conditions"]:
        st.write(cond["display"])
    st.subheader("Medications")
    for med in patient_info["medications"]:
        st.write(med["display"] + " " + med["dosage"])

    if "numerical_observations" in patient_info:
        st.subheader("Numerical Observations")
        for obs in patient_info["numerical_observations"]:
            st.write(obs["name"] + " " + str(obs["value"]) + " " + obs["unit"])




with st.form("phone call form"):
    # text input for phone number
    phone_number = st.text_input("Enter your phone number:")

    # option = st.selectbox(
    #     'Are you a patient or a nurse?',
    #     (
    #         'Patient',
    #         'Nurse',
    #     )
    # )

    z = st.form_submit_button("I am ready for another call")

    if z:
        # call logic goes here

        # validate phone number
        # check if phone number has () or - in it
        # if so, remove them
        phone_number = phone_number.replace("(", "")
        phone_number = phone_number.replace(")", "")
        phone_number = phone_number.replace("-", "")
        phone_number = phone_number.replace(" ", "")
        phone_number = phone_number.replace("+", "")
        if len(phone_number) != 10:
            call_type = "invalid phone number"
        else:
            #sample rachel or human
            call_type = random.choices(list(call_probs.keys()), weights=list(call_probs.values()))[0]
            print(call_type)
        
        if call_type == "rachel":
            initiate_rachel_call(phone_number)
        elif call_type == "human":

            # also need to check if humans are available
            # how to handle if they're not?

            # just use twilio simulring
            # but still need to handle if they're not available

            initiate_human_call(phone_number)

            

        else:
            st.write("Invalid phone number - please check and try again")

        patient_data = sample_patient_info()
        display_patient_info(patient_data)



