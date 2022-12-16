class Doctor:
    def __init__(self, ID, name, specialization, working_time, qualification, room_number):
        self.ID = ID
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number

    def formatDrInfo(self):
        doctor_info=f"{self.ID}_{self.name}_{self.specialization}_{self.working_time}_{self.qualification}_{self.room_number}"
        return doctor_info

    def enterDrInfo(self):
        print("Enter the doctor's ID: ")
        self.ID = int(input())
        print("Enter the doctor's name: ")
        self.name = input()
        print("Enter the doctor's  specility: ")
        self.specialization = input()
        print("Enter the doctor's timing (e.g., 7am-10pm): ")
        self.working_time = input()
        print("Enter the doctor's qualification: ")
        self.qualification = input()
        print("Enter the doctor's room number: ")
        self.room_number = int(input())
        doctor_info=Doctor(self.ID, self.name, self.specialization, self.working_time, self.qualification, self.room_number)
        return doctor_info

    def readDoctorsFile(self):
        doctors_list=[]
        file= open("./files/doctors.txt", "r")
        file_content = file.readlines()
        for line in file_content:
            self.doctors_list = line.split("_")
            doctors=Doctor(self.doctor_info[0], self.doctor_info[1], self.doctor_info[2], self.doctor_info[3], self.doctor_info[4], self.doctor_info[5])
            self.doctors_list.append(doctors)
            print(doctors_list)

    def displayDoctorsList(self):
        file=open("./files/doctors.txt", "r")
        file_content = file.readlines()
        for line in file_content:
            self.doctors_list = line.split("_")
            doctors=Doctor(self.doctor_info[0], self.doctor_info[1], self.doctor_info[2], self.doctor_info[3], self.doctor_info[4], self.doctor_info[5])
            self.doctors_list.append(doctors)
            print(f' {self.doctor_info[0]}, {self.doctor_info[1]}')

    def searchDoctorById(self, doctors_list):
        print("Enter the doctor id:")
        ID=int(input())
        for i in range(len(doctors_list)):
            if ID == self.doctors_list[i].ID:
                print(self.doctors_list[i].ID, self.doctors_list[i].name, self.doctors_list[i].specialization, self.doctors_list[i].qualification, self.doctors_list[i].room_number)
            else:
                print("Can't find the doctor with the same ID on the system!")

    def searchDoctorByName(self,doctors_list):
        print("Enter the doctor name:")
        name=input()
        for i in doctors_list:
            if name == self.doctors_list[i].name:
                print(self.doctors_list[i].ID, self.doctors_list[i].name, self.doctors_list[i].specialization, self.doctors_list[i].qualification, self.doctors_list[i].room_number)
            else:
                print("Can't find the doctor with the same name on the system!")

    def editDoctorInfo(self):
        print("Please enter the id of the doctor that you want to edit their information:")
        self.ID=int(input())
        print("Enter new name:")
        self.name=input()
        print("Enter new specilist in:")
        self.specialization=input()
        print("Enter new timing:")
        self.working_time=input()
        print("Enter new qualification:")
        self.qualification=input()
        print("Enter new room number:")
        self.room_number=int(input)
        doctor_info=Doctor(self.ID, self.name, self.specialization, self.working_time, self.qualification, self.room_number)
        return doctor_info

    def writeListOfDoctorsToFile(self, doctors_list):
        file= open("./files/doctors.txt", "w")
        for doctor in range(len(doctors_list)):
            file.write(self.doctors_list)
            
    def addDrToFile(self):
        file= open("./files/doctors.txt", "a")
        new_doctor=self.enterDrInfo()
        file.write(new_doctor)
        file.close()

class Facility:
    def __int__(self, name):
        self.name = name

    def displayFacilities(self):
        facilities_list=[]
        file= open("./files/facilities.txt", "r")
        file_content = file.readlines()
        for line in file_content:
            self.facilities_list = line.split("_")
            facilities=Facility(self.facility_info[0])
            self.facilities_list.append(facilities)
            print('{self.facility_info[0]}')

    def addFacility(self):
        file= open("./files/facilities.txt", "a")
        print("Enter Facility name:")
        new_name = input()
        file.write(new_name)
        file.close()
        
    
    def writeListOfFacilitiesToFile(self, facilities_list):
        file= open("./files/facilities.txt", "w")
        for facility in range(len(facilities_list)):
            file.write(self.facilities_list)

class Laboratory:
    def __init__(self, lab_name, lab_cost ):
        self.lab_name=lab_name
        self.lab_cost=lab_cost

    def formatLabInfo(self):
        lab_info=f"{self.lab_name}_{self.cost}"
        return lab_info

    def enterLaboratoryInfo(self):
        print("Enter laboratory facility:")
        self.lab_name = input()
        print("Enter laboratory cost:")
        self.lab_cost = float(input())
        lab_info=Laboratory(self.lab_name, self.lab_cost)
        return lab_info

    def readLaboratoriesFile(self):
        lab_list=[]
        file = open ("./files/laborartories.txt", "r")
        file_content = file.readlines()
        for line in file_content:
            self.lab_list = line.split("_")
            labs = Laboratory(self.lab_info[0], self.lab_info[1])
            lab_list.append(labs)
        print(lab_list)

    def displayLabsList(self):
        file = open ("./files/laborartories.txt", "r")
        file_content = file.readlines()
        for line in file_content:
            self.lab_list = line.split("_")
            labs = Laboratory(self.lab_info[0], self.lab_info[1])
            self.lab_list.append(labs)
        print(f'  {self.lab_info[0]}, {self.lan_info[1]} ')

    def addLabToFile(self):
        file = open ("./files/laboratories.txt", "a")
        new_lab = self.enterLaboratoryInfo()
        file.write(new_lab)
        file.close()

    def writeListOfLabsToFile(self, lab_list):
        file = open ("./files/laboratories.txt", "w")
        for lab in range(len(lab_list)):
            file.write(self.lab_list)

class Patient:
    def __init__(self, p_id, p_name, p_disease, p_gender, p_age):
        self.p_id = p_id
        self.p_name = p_name
        self.p_disease = p_disease
        self.p_gender = p_gender
        self.p_age = p_age

    def formatPatientInfo(self):
        patient_info=f"{self.p_name}_{self.p_name}_{self.p_disease}_{self.p_gender}_{self.p_age}"
        return patient_info

    def enterPatientInfo(self):
        print("Enter patient id:")
        self.p_id = int(input)
        print("Enter patient name:")
        self.p_name = input()
        print("Enter patient disease:")
        self.p_disease = input()
        print("Enter patient gender:")
        self.p_gender = input()
        print("Enter patient age:")
        self.p_age = int(input)
        patient_info=Patient(self.p_id, self.p_name, self.p_disease, self.p_gender, self.p_age)
        return patient_info

    def readPatientsFile(self):
        patient_list=[]
        file=open("./files/patients.txt", "r")
        file_content = file.readlines()
        for line in file_content:
            self.patient_list=line.split("_")
            patients=Patient(self.patient_info[0], self.patient_info[1], self.patient_info[2], self.patient_info[3], self.patient_info[4])
            self.patient_list.append(patients)
        print(patient_list)

    def displayPateintsList(self):
        file=open("./files/patients.txt", "r")
        file_content = file.readlines()
        for line in file_content:
            self.patient_list=line.split("_")
            patients=Patient(self.patient_info[0], self.patient_info[1], self.patient_info[2], self.patient_info[3], self.patient_info[4])
            self.patient_list.append(patients)
        print(f'  {self.patient_info[0]}, {self.patient_info[1]} ')

    def serachPateintById(self, patient_list):
        print("Enter the patient ID:")
        p_id=int(input())
        for i in range(len(patient_list)):
            if p_id == self.patient_list[i].p_id:
                print(self.patient_list[i].p_id, self.patient_list[i].p_name, self.patient_list[i].disease, self.patient_list[i].gender, self.patient_list[i].age)
            else:
                print("Can't find the patient with the same name on the system!")

    def editPatientInfo(self):
        print("Enter patient id:")
        self.p_id=int(input())
        print("Enter patient name:")
        self.p_name=input()
        print("Enter patient disease:")
        self.p_disease=input()
        print("Enter patient gender:")
        self.p_gender=input()
        print("Enter patient age:")
        self.p_age=int(input)
        patient_info=Patient(self.p_id, self.p_name, self.p_disease, self.p_gender, self.p_age)
        return patient_info

    def writeListOfPatientsToFile(self, patient_list):
        file=open("./files/patients.txt", "w")
        for patient in range(len(patient_list)):
            file.write(self.patient_list)

    def addPatientToFile(self):
        file=open("./files/patients.txt", "a")
        new_patient=self.enterPatientInfo()
        file.write(new_patient)
        file.close()

class Management:
    def DisplayMenu(self):
        print ("Welcome to Alberta Hospital (AH) Management System!\nSelect from the following options, or select 0 to stop:\n1 - Doctors\n2 - Facilities\n3 - Laboratories\n4 - Patients")
        count=int(input())
        while count >= 0:
            if count == 0:
                break
            elif count == 1:
                print("Doctors Menu:\n1 - Display Doctors list\n2 - Search for Doctor by ID\n3 - search for doctor by name\n4 - Add Doctor\n5- Edit doctor info\n6- Back to the MAin Menu")
                count1=int(input())
                while count1 >= 0:
                    if count1 == 6:
                        break
                    elif count1 == 1:
                        Doctor.displayDoctorsList('')
                    elif count1 == 2:
                        Doctor.searchDoctorById('')
                    elif count1 == 3:
                        Doctor.searchDoctorByName('')
                    elif count1 == 4:
                        Doctor.addDrToFile('')
                    elif count1 == 5:
                        Doctor.editDoctorInfo('')
                    print ("Back to the previous Menu")
            elif count == 2:
                print("Facilities Menu:\n1 - Display Facilities list\n2 - Add Facility\n3 - Back to the Main Menu")
                count1=int(input)
                while count1 >= 0:
                    if count1 == 3:
                        break
                    elif count1 == 1:
                        Facility.displayFacilities()
                    elif count1 == 2:
                        Facility.addFacility()
                    print ("Back to the previous Menu")
            elif count == 3:
                print("Laboratories Menu:\n1 - Display laboratories list\n2 - Add labpratory\n3 - Back to the Main Menu")
                count1=int(input)
                while count1 >= 0:
                    if count1 == 3:
                        break
                    elif count1 == 1:
                        Laboratory.displayLabsList()
                    elif count1 == 2:
                        Laboratory.addLabToFile()
                    print ("Back to the previous Menu")
            elif count == 4:
                print("Patients Menu:\n1 - Display patients list\n2 - Search for patient by ID\n 3- Add patient\n4 - Edit patient info\n5 - Back to the Main Menu")
                count1=int(input)
                while count1 >= 0:
                    if count1 == 5:
                        break
                    elif count1 == 1:
                        Patient.displayPateintsList()
                    elif count1 == 2:
                        Patient.serachPateintById()
                    elif count1 == 3:
                        Patient.addPatientToFile()
                    elif count1 == 4:
                        Patient.editPatientInfo()
                    print ("Back to the previous Menu")

display=Management.DisplayMenu('')
print(display)