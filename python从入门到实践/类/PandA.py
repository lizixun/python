from user import User
class Admin(User):
    def __init__(self,first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges=[]
    def show_privileges(self):
        for privilege in self.privileges:
            print("-"+privilege)

class Privileges():
    """A class to store an admin's privileges."""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege)
        else:
            print("- This user has no privileges.")
