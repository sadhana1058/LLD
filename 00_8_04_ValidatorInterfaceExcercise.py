from abc import ABC, abstractmethod

class Validator(ABC):
    @abstractmethod
    def validate(self,inp):
        pass

class EmailValidator(Validator):
    def validate(self,inp):
        return '@' in inp

class PasswordValidator(Validator):
    def validate(self,inp):
        return len(inp)>=8



class RegistrationService:
    def __init__(self,validators : list[Validator]):
        self._validators=validators
    
    def register(self,inp):
        for v in self._validators:
            a=v.validate(inp)
            w=''
            if a:
                w +="PASSED"
            else:
                w+="FAILED"

            print('\''+inp+'\'-' +w)
















if __name__ == "__main__":
    email_reg = RegistrationService([EmailValidator()])
    email_reg.register("user@example.com")  # Should pass
    email_reg.register("invalid-email")      # Should fail

    pass_reg = RegistrationService([PasswordValidator()])
    pass_reg.register("strongpassword")  # Should pass
    pass_reg.register("short")            # Should fail