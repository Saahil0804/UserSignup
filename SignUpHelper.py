# Validating username
def validationForUsername(Username):
    try : 
        Username = str(Username).strip()
        if len(Username) < 6 or len(Username) > 20 or not Username.isalnum():
            return False
        else:
            return True
    except Exception as e:
        print(f"An error occurred during username validation: {e}")
        return False

# Validating password
def validationForPassword(Pword):
    try :   
        Pword = str(Pword).strip()
        if len(Pword) < 8:
            return False
        else:
            return True
    except Exception as e:
        print(f"An error occurred during username validation: {e}")
        return False

# Validating email
def validationForEmail(Email):
    try : 
        Email = str(Email).strip()
        if "@" not in Email or ".com" not in Email:
            return False
        else:
            return True
    except Exception as e:
        print(f"An error occurred during username validation: {e}")
        return False

# Validating phone number
def validationForPhone(Phone):
    try :
        Phone = str(Phone).strip()
        if len(str(Phone)) != 10:
            return False
        else:
            return True
    except Exception as e:
        print(f"An error occurred during username validation: {e}")
        return False

# Validating full name
def validationForFName (fname, lname):
    try :
        FullName = fname + " " + lname   
        FullName = str(FullName).strip()
        if len(FullName) < 3:
            return False
        else:
            return True
    except Exception as e:
        print(f"An error occurred during username validation: {e}")
        return False