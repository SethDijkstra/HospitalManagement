#CPRG-216-C Date 22/12/05
#Made By Seth, Jesse, Tansima Fiana
#Patient management application that deals with patient.txt and class objects
#to add, edit, or search for patient records.


import mainmenu
import classes

#Function to display patient menu screen
def patientMenuDisplay():
    print('')
    print("Patient Menu")
    print('')
    print(format("Selection", "10s"), format("Description", "0s"))
    print(format("=========", "10s"), format("===========", "14s"))
    print(format("    0", "10s"), format("Return to Main Menu", "13s"))
    print(format("    1", "10s"), format("Display patient's list", "13s"))
    print(format("    2", "10s"), format("Search for patient by ID", "13s"))
    print(format("    3", "10s"), format("Add patient", "13s"))
    print(format("    4", "10s"), format("Edit patient info", "13s"))

#Asks the user to enter patient information(attributes), then creates and returns a new Patient object
def enterPatientinfo():
    id = input("Enter Patient ID: ")
    name = input("Enter Patient name: ")
    diagnosis = input("Enter Patient diagnosis: ")
    gender = input("Enter Patient gender: ")
    age = input("Enter Patient age: ")
    patient = classes.Patient(id, name, diagnosis, gender, age)
    return patient

#Function that reads "patient.txt" file into a list of Patient objects
def readPatientsFile():
    p_list = []
    file = open('patients.txt', 'r')
    file.readline()
    for line in file:
        attributes = line.strip().split('_')
        patient = classes.Patient(attributes[0], attributes[1], attributes[2], attributes[3], attributes[4])
        p_list.append(patient)
    file.close()
    return p_list

#Function that displays all the patient information(attributes) in a patient list
def displayPatientsList():
    print("")
    print(format("ID", "5s"), format("Name", "7s"), format("Diagnosis", "10s"), format("Gender", "7s"), format("Age", "10s"))
    print(format("==", "4s"), format("======", "8s"), format("=========", "10s"), format("======", "7s"), format("===", "10s"))
    for patient in patientList:
        print(patient)
    
#writePatientsListToFile function that writes "patient.txt" file from the list of Patient objects
#maintaing correct formatting.               
def writePatientsListToFile():
    file = open('patients.txt', 'w')
    file.write("ID_Name_Diagnosis_Gender_Age\n")
    for patient in patientList:
        file.write(classes.Patient.formatPatientInfo(patient))
    file.close()
    
#searchPatientByID function that searches the list of Patient objects for a specified patient ID
#using the patient ID that the user enters. Returns Patient object or -1 if not found
def patientSearch(id):
    x = 0
    for patient in patientList:
        idnum = int(patient.getId())
        if idnum == id:
            print("\nRecord found.\n")
            print(patient)
        else:
            x += 1
        if x == len(patientList):
            print("\nRecord not found.")
         
#addPatientToList function that gets new Patient object (with user entered patient information)
#and adds it to the patient list.
def patientAdd():
    patientList.append(enterPatientinfo())

#Finds patient ID in the list of Patient objects, prompts for new values and updates the remaining
#attributes.
def patientEdit(id):
    patientSearch(id)
    for patient in patientList:
        idnum = int(patient.getId())
        if idnum == id:
            patient.setName(input("Enter new patient name: "))
            patient.setDiagnosis(input("Enter new patient diagnosis: "))
            patient.setGender(input("Enter new patient gender: "))
            patient.setAge(input("Enter new patient age: "))
            print("\nPatient file edited.")
            break
        else:
            continue
        
#input validation function to check if input is a number and convert to int. If not will loop
#for new input.
def menuinputValidation(answer):
    while True:
        try:
            answer = int(answer)
            break
        except ValueError:
            print("It must be a number.")
            answer = input("> ")
    while answer not in range(0, 5):
        print("It must be between 0-4.")
        answer = input("> ")
        answer = menuinputValidation(answer)
    return answer

def numValidation(answer):
    while True:
        try:
            answer = int(answer)
            break
        except ValueError:
            print("It must be a number.")
            answer = input("> ")
    return answer

#Function that displays the patient menu options and handles the choices.      
def patientMenu():
    global patientList
    #Creates patient list of objects using readPatientFile function.
    patientList = (readPatientsFile())
    while True:
        patientMenuDisplay()
        answer = input("\nEnter selection: ")
        answer = menuinputValidation(answer)
        match answer:
            #If user enters 0 the patient.txt will be written to from the list of objects
            #and the program will be exited
            case 0:
                writePatientsListToFile()
                print("\nReturning to main menu...")
                mainmenu.main()
            
            #If user enters 1 it will display a list of patients from the list of patient
            #objects.
            case 1:
                displayPatientsList()
                
            #If user enters 2 it will ask for ask for a patient ID as input and search for 
            #patient record
            case 2:
                id = input("Enter the patient ID: ")
                id = numValidation(id)
                patientSearch(id)
                
            #If user enters 3 it will add new patient to the list of patient objects
            #using enterPatientInfo function to handle user inputs
            case 3:
                patientAdd()
                
            #If user enters 4 it will ask for a patient ID as input and search the 
            #list of patient objects for that ID, if found it will prompt user
            #for new inputs for the attributes
            case 4:
                id = input("Enter the patient ID: ")
                id = numValidation(id)
                patientEdit(id)

if __name__ == '__main__':
    patientMenu()
