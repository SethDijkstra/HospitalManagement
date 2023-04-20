import patientmenu
import doctormenu
import facility
import laboratory

#Displays the main menu
def menu():
    print('')
    print("Main Menu")
    print('')
    print(format("Selection", "10s"), format("Description", "0s"))
    print(format("=========", "10s"), format("===========", "14s"))
    print(format("    0", "10s"), format("Close Application", "13s"))
    print(format("    1", "10s"), format("Doctors", "13s"))
    print(format("    2", "10s"), format("Facilities", "13s"))
    print(format("    3", "10s"), format("Laboratories", "13s"))
    print(format("    4", "10s"), format("Patients", "13s"))

def main():
    menu()
    answer = input("\nEnter option: ")
    answer = patientmenu.menuinputValidation(answer)
    match answer:
        #If 0 it will exit the program.
        case 0:
            print("You have chosen to exit the program")
            print("\nThe program is now closing... goodbye.")
            exit()
        #If 1 it will run the doctor menu module to handle the doctor file system
        case 1:
            doctormenu.doctorMenu()
        #If 1 it will run the facility menu module to handle the facilities file system
        case 2:
            facility.facilityMenu()
        #If 1 it will run the lab menu module to handle the laboratories file system
        case 3:
            laboratory.labMenu()
        #If 1 it will run the paitent menu module to handle the paitent file system
        case 4:
            patientmenu.patientMenu()

if __name__ == '__main__':
    # patientList = (patientmenu.readPatientsFile())
    print("\nWelcome to the Alberta Rural Patient Care Management System\n")
    main()
