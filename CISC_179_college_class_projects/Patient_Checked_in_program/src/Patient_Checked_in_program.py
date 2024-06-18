#prompt:
#create a function in PyCharm that 
#counts the number of patience in a hospital
#that are currently checked in,
#and then prints out in the console area
#their name, patient number, room number

Sharp_Hospital_Patient_Data = [
    {
        "Patient_Name":"Eric",
        "Patient_Number":50215,
        "Room_Number":511,
        "Checked_In":True,
    },
    {
        "Patient_Name":"Ryan",
        "Patient_Number":50123,
        "Room_Number":521,
        "Checked_In":False,
    },
    {
        "Patient_Name":"Karen",
        "Patient_Number":50168,
        "Room_Number":520,
        "Checked_In":True,
    },
    {
        "Patient_Name":"Matthew",
        "Patient_Number":50898,
        "Room_Number":410,
        "Checked_In":False,
    },
    {
        "Patient_Name":"Kim",
        "Patient_Number":50999,
        "Room_Number":120,
        "Checked_In":False,
    },
    {
        "Patient_Name":"Toby",
        "Patient_Number":50741,
        "Room_Number":123,
        "Checked_In":False,
    },
    {
        "Patient_Name":"Johanna",
        "Patient_Number":50233,
        "Room_Number":330,
        "Checked_In":True,
    },
]

#patient_checked_in_info function will loop through patient data to find out 
#the patient that are currently checked in and print out their name, patient number, and room number

def patient_checked_in_info(patient_data):
    try:
        for patient in patient_data:
            if patient["Checked_In"] == True:
                print(f'Patient Name: {patient["Patient_Name"]}. ' 
                      f'Patient Number: {patient["Patient_Number"]}. ' 
                      f'Room Number: {patient["Room_Number"]}')
                
    except Exception as e:
        print("There's an error occured!!! Error information: ", e)
        

print("***This is Sharp Hospital Patient Checking Data App***\n",
"Here are the patients that are currently checked in:\n",sep="")

patient_checked_in_info(Sharp_Hospital_Patient_Data)