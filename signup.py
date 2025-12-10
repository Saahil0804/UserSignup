
from Helper.SignUpHelper import *
from datetime import datetime

# Function to sign up a new user
def signUpUser():
    try:

        Username = input("Enter your username: ")
        ValidUsername = validationForUsername(Username)
        if ValidUsername:
            pass
        else:
            return "Entered username is not valid. Please try again."
                
        Pword = input("Enter your password: ")
        Validpword = validationForPassword(Pword)
        if Validpword:
            pass
        else:
            return "Entered password is not valid. Please try again."
        
        f_name = input("Enter your first name: ")
        l_name = input("Enter your Last name: ")
        FullName = validationForFName(f_name, l_name)
        if not FullName:
            print("Entered full name is not valid. Please try again.")
            return False
        
        email_id = input("Enter your email: ")
        Validemail = validationForEmail(email_id)
        if not Validemail:
            return "Entered email is not valid. Please try again." 
               
        phone_no = int(input("Enter your phone number: "))
        Validphone = validationForPhone(phone_no)
        if not Validphone:
            return "Entered phone number is not valid. Please try again."

        result = insert_user_data(Username, Pword, FullName, email_id, phone_no, created_at=datetime.now(), updated_at=datetime.now(), created_by=FullName, updated_by=FullName)
        return result
    except ValueError:
        print("Invalid input. Please enter the correct data types.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Function to insert user data into the database
def insert_user_data(Username, Pword, FullName, email_id, phone_no,created_at=datetime.now(), updated_at=datetime.now(), created_by="", updated_by=""):
    try:
        connection = dbConnection()
        if connection is None:
            return "Failed to connect to the database."
        cursor = connection.cursor()
        isUserExist = check_existing_email(email_id)
        if not isUserExist:
            return "User already exists with this email."
        insert_query = """
                INSERT INTO UserDetails (Username, Pword, FullName, email_id, phone_no, created_at, updated_at, created_by, updated_by)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
        cursor.execute(insert_query, (Username, Pword, FullName, email_id, phone_no, created_at, updated_at, created_by, updated_by))
        connection.commit()
        return "User signed up successfully!"
    except Exception as e:
            print(f"Error inserting user data: {e}")
    finally:
            cursor.close()
            connection.close()

# Function to check if the email already exists
def check_existing_email(email_id):
    try:
        connection = dbConnection()
        if connection is not None:
            cursor = connection.cursor()
            email_check_query = "SELECT * FROM UserDetails WHERE email_id = %s and is_active = true"
            cursor.execute(email_check_query, (email_id,))
            existing_user = cursor.fetchone()
            if existing_user:
                print("User is already registered with this email.")
                return False    
            else:
                print("Email is available for registration.")        
            return True
    except Exception as e:
            print(f"Error checking existing email: {e}")
            return False
    finally:
            if connection:
                cursor.close()
                connection.close()

# Main execution
if __name__ == "__main__":
    signUpUser()
            
