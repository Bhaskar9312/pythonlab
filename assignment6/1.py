class Password_manager:
    def __init__(self):
        self.old_passwords=[]
    def get_password(self):
        if self.old_passwords:
            return self.old_passwords[-1]
        else:
            return None
    def set_password(self,new_password):
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            print(f"passsword has been changed to {new_password}")
        else:
            print("This password has been used before.Please enter another password")
    def is_correct(self,password):
        return password==self.get_password()
pm=Password_manager()
pm.set_password("Bhaskar123")
print(pm.get_password())
pm.set_password("Bhaskar456")
pm.set_password("Bhaskar789")
print(pm.is_correct("Bhaskar789"))


