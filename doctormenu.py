import mainmenu
import patientmenu
import classes
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
    while answer not in range(0, 6):
        print("It must be between 0-5.")
        answer = input("> ")
        answer = menuinputValidation(answer)
    return answer
# function to display doctor menu
def displayDoctorMenu():
    print('')
    print("Doctor's Menu")
    print('')
    print(format("Selection", "10s"), format("Description", "0s"))
    print(format("=========", "10s"), format("===========", "14s"))
    print(format("    0", "10s"), format("Return to Main Menu", "13s"))
    print(format("    1", "10s"), format("Display Doctors list", "13s"))
    print(format("    2", "10s"), format("Search for doctor by ID", "13s"))
    print(format("    3", "10s"), format("Search for doctor by name", "13s"))
    print(format("    4", "10s"), format("Add doctor", "13s"))
    print(format("    5", "10s"), format("Edit doctor info", "13s"))
#Asks the user to enter doctor information(attributes), then creates and returns a new doctor object
def enterDrInfo():
    id = input("Enter Dr ID: ")
    name = input("Enter Dr name: ")
    specialty = input("Enter Dr specialty: ")
    schedule = input("Enter Dr schedule: ")
    qualification = input("Enter Dr qualifications: ")
    roomnumber = input("Enter Dr room number: ")
    doctor = classes.Doctor(id, name, specialty, schedule, qualification, roomnumber) 
    return doctor
#addDoctorToList
def addDrTolist():
    doctorList.append(enterDrInfo())

#Function that reads "doctors.txt" file into a list of Doctor objects
def readDoctorsFile():
    d_list = []
    file = open('doctors.txt')
    file.readline()
    for line in file:
        attributes = line.strip().split('_')
        doctor = classes.Doctor(attributes[0], attributes[1], attributes[2], attributes[3], attributes[4], attributes[5])
        d_list.append(doctor)
    return d_list

#searchDoctorByID function that searches the list of Doctor objects for a specified doctor ID
#using the doctor ID that the user enters. Returns doctor object or -1 if not found
def searchDoctorById(id):
    x = 0
    for doctor in doctorList:
        idnum = int(doctor.getId())
        if idnum == id:
            print("\nRecord found.\n")
            print("")
            print(format("ID", "4s"), format("Name", "13s"), format("Specialty", "17s"), format("Schedule", "10s"), format("Qualifications", "15s"), format("RoomNbr"))
            print(format("==", "4s"), format("====", "13s"), format("=========", "17s"), format("========", "10s"), format("==============", "15s"), format("======="))
            print(doctor)
        else:
            x += 1
        if x == len(doctorList):
            print(f"\nDoctor with ID {id} not found in file.")
  #searchDoctorByName function that searches the list of Doctor objects for a specified doctor name               
def searchDoctorByName(name):
    x = 0
    for doctor in doctorList:
        realname = doctor.getName()
        if name == realname:
            print("\nRecord found.\n")
            print("")
            print(format("ID", "4s"), format("Name", "13s"), format("Specialty", "17s"), format("Schedule", "10s"), format("Qualifications", "15s"), format("RoomNbr"))
            print(format("==", "4s"), format("====", "13s"), format("=========", "17s"), format("========", "10s"), format("==============", "15s"), format("======="))
            print(doctor)
        else:
            x += 1
        if x == len(doctorList):
            print(f"\nDoctor with name {name} not found in file.")
#Finds doctor ID in the list of doctor objects, prompts for new values and updates the remaining
#attributes.
def editDoctorInfo(id):
    searchDoctorById(id)
    for doctor in doctorList:
        idnum = int(doctor.getId())
        if idnum == id:
            doctor.setName(input("\nEnter new name: "))
            doctor.setSpecialty(input("Enter new specialty: "))
            doctor.setSchedule(input("Enter new schedule: "))
            doctor.setQualification(input("Enter new qualifications: "))
            doctor.setRoomnumber(input("Enter new room number: "))
            print('\nDoctor file edited.')
#Function that displays all the doctor information(attributes) in a doctor list    
def displayDoctorsList():
    print("")
    print(format("ID", "4s"), format("Name", "13s"), format("Specialty", "17s"), format("Schedule", "10s"), format("Qualifications", "15s"), format("RoomNbr"))
    print(format("==", "4s"), format("====", "13s"), format("=========", "17s"), format("========", "10s"), format("==============", "15s"), format("======="))
    for doctor in doctorList:
        print(doctor)
#writeDoctorsListToFile function that writes "doctors.txt" file from the list of doctor objects with correct formatting

def writeDoctorsListToFile():
    file = open('doctors.txt', 'w')
    file.write('ID_Name_Specialty_Schedule_Qualifications_RoomNbr\n')
    for doctor in doctorList:
        file.write(classes.Doctor.formatDoctorInfo(doctor))
    file.close()
#Function that displays the doctor menu options and handles the choices.
def doctorMenu():
    global doctorList
    doctorList = readDoctorsFile()
    while True:  
        displayDoctorMenu()
        answer = (input("\nEnter selection: "))
        answer = menuinputValidation(answer)
        match answer:
            case 0:
                writeDoctorsListToFile()
                print("\nReturning to main menu...")
                mainmenu.main()
            case 1:
                displayDoctorsList()
            case 2:
                id = input("Enter the Doctor ID: ")
                id = patientmenu.numValidation(id)
                searchDoctorById(id)
            case 3:
                name = input("Enter the doctor name: ")
                searchDoctorByName(name)
            case 4:
                addDrTolist()
            case 5:
                id = input("Enter the Doctor ID: ")
                id = patientmenu.numValidation(id)
                editDoctorInfo(id)
    
if __name__ == '__main__':
    doctorMenu()
    
        
