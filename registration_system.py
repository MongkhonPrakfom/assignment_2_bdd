class RegistrationSystem:

    def register_student(self, name, email):

        if email == "":
            return "Error: Email is required"

        return "Registration Successful"