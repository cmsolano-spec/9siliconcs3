class Patient:
    def __init__(self, name, bill_amount):#attribute "name" and "bill_amount" is in the class Patient
        self.__name = name
        self.__bill_amount = bill_amount

    @property #gets the attribute name
    def name(self): #makes the private attribute accessible for inheritance
        return (f"Patient Name: {self.__name}")


    @name.setter #sets the attribute name
    def name(self, name):
        self.__name = name

    @property #gets the attribute name
    def bill_amount(self): #makes the private attribute accessible for inheritance
        return (f"Original:  ₱{self.__bill_amount}")

    @bill_amount.setter #sets the attribute name
    def bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    def calculate_bill(self):
      if self.__bill_amount >= 0: #Needs to be positive or zero to be valid
        print(f"Final Bill:  ₱{self.__bill_amount}")
      else:
        print("Invalid.")

    def display_patient_type(self):
      print("Patient Type: Regular Patient")

class Senior(Patient):
  def calculate_bill(self):
      if self._Patient__bill_amount >= 0: #Needs to be positive or zero to be valid
        self.__bill_amount = self._Patient__bill_amount * 0.80 #subtracts the discount
        print(f"Final Bill:  ₱{self.__bill_amount:.2f}")
      else:
        print("Invalid.")
    
  def display_patient_type(self):
      print("Patient Type: Senior Citizen")
        
class Philhealth_Patient(Patient):
  def calculate_bill(self):
      if self._Patient__bill_amount >= 0: #Needs to be positive or zero to be valid
        self.__bill_amount = self._Patient__bill_amount * 0.85 #subtracts the discount
        print(f"Final Bill:  ₱{self.__bill_amount:.2f}")
      else:
        print("Invalid.")

  def display_patient_type(self):
      print("Patient Type: PhilHealth Member")

regular_patient = Patient("Juan Dela Cruz", 15000)
senior_patient = Senior("Claire Olano", 111211)
philhealth_patient = Philhealth_Patient("Conner Scientific", 123456)

patients = [regular_patient, senior_patient, philhealth_patient]

print("Hospital Biling System")
print("- - - - - - - - - - - - - - ")
for patient in patients:
  print(patient.name)
  patient.display_patient_type()
  print(patient.bill_amount)
  patient.calculate_bill()
  print(" ")

