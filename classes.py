#Defines a class named Doctor with attributes
class Patient:
    
    #Define all attributes
    def __init__(self, id, name, diagnosis, gender, age):
        self.id = id
        self.name = name
        self.diagnosis = diagnosis
        self.gender = gender
        self.age = age
    
    #Getter functions to return ID
    def getId(self):
        return self.id
    
    #Setter functions to set or change each attribute
    def setName(self, name):
        self.name = name
    def setDiagnosis(self, diagnosis):
        self.diagnosis = diagnosis
    def setGender(self, gender):
        self.gender = gender
    def setAge(self, age):
        self.age = age
    
    #Function that returns a formatted print out of Patient's attributes
    def __str__(self):
        return f'{self.id : <5}{self.name : <9}{self.diagnosis : <11}{self.gender : <8}{self.age}'
    
    #Function that formats doctor's information(attributes) in the same format used in the "patients.txt" file
    def formatPatientInfo(self):
        formatted = f'{self.id}_{self.name}_{self.diagnosis}_{self.gender}_{self.age}\n'
        return formatted

#Defines a class named Doctor with certain attributes
class Doctor:
    
    #Define all attributes
    def __init__(self, id, name, specialty, schedule, qualification, roomnumber):
        self.id, self.name, self.specialty, self.schedule, self.qualification, self.roomnumber = id, name, specialty, schedule, qualification, roomnumber
        
    #Getter functions to return name and/or id
    def getId(self):
        return self.id
    def getName(self):
        return self.name
    
    #Setter functions to set or change each attribute
    def setName(self, name):
        self.name = name
    def setSpecialty(self, specialty):
        self.specialty = specialty
    def setSchedule(self, schedule):
        self.schedule = schedule
    def setQualification(self, qualification):
        self.qualification = qualification
    def setRoomnumber(self, roomnumber):
        self.roomnumber = roomnumber
        
    #Function that returns a formatted print out of Doctor's attributes
    def __str__(self):
        return f'{self.id : <5}{self.name : <14}{self.specialty : <18}{self.schedule : <11}{self.qualification: <16}{self.roomnumber}'
    
    #Function that formats doctor's information(attributes) in the same format used in the "doctors.txt" file
    def formatDoctorInfo(self):
        formatted = f'{self.id}_{self.name}_{self.specialty}_{self.schedule}_{self.qualification}_{self.roomnumber}\n'
        return formatted

#Defines a class named Facility with certain attributes
class Facility:
    
    #Define all attributes
    def __init__(self, name):
        self.name = name
        
    #Function that returns a formatted print out of Facility's attributes
    def __str__(self):
        return f'{self.name}'
    
    #Function that formats doctor's information(attributes) in the same format used in the "facilities.txt" file
    def formatFacilityInfo(self):
        formatted = f'{self.name}\n'
        return formatted

#Defines a class named Laboratory with certain attributes    
class Laboratory:
    
    #Define all attributes
    def __init__(self, name, cost):
        self.name, self.cost = name, cost
        
    #Function that returns a formatted print out of Laboratory's attributes
    def __str__(self):
        return f'{self.name : <24}{self.cost}'
    
    #Function that formats doctor's information(attributes) in the same format used in the "laboratories.txt" file
    def formatLaboratoryInfo(self):
        formatted = f'{self.name}_{self.cost}\n'
        return formatted
