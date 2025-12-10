import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()

# Validating new full name
def validationForNewFname ():
    try :
        newfname= input("Enter your new first name: ")
        newlname= input("Enter your new last name: ")
        NewFullName = newfname + " " + newlname   
        NewFullName = str(NewFullName).strip()
        if len(NewFullName) < 3:
            print("Entered name is not valid. Please try again.")
            return False
        else:
            print("Full name validated successfully.")
            return NewFullName
    except Exception as e:
        print(f"An error occurred during full name validation: {e}")
        return False

# Validating new phone number
def validationForNewPhone():
    try :
        newphone= int(input("Enter your new phone number: "))
        newphone = str(newphone).strip()
        if len(str(newphone)) != 10:
            print ("Entered phone number is not valid. Please try again.")
            return False
        else:
            print("Phone number validated successfully.")
            return newphone
    except Exception as e:
        print(f"An error occurred during phone number validation: {e}")
        return False
    
# Function to connect to the database
def dbConnection():
    try:
        connection = psycopg2.connect(
            host=os.getenv("HOSTNAME"),
            user=os.getenv("USER_NAME"),
            password=os.getenv("PASSWORD"),
            database=os.getenv("DATABASE"),
            port=os.getenv("PORT")
        )
        print("Database connected successfully")
        return connection
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None  
    
# Function to update user data into the database
def update_user_data(email_id, choice):
    try:
        if choice not in [1, 2, 3]:
            return "Invalid choice. Please enter 1, 2, or 3."
        if choice == 1:             
            name_update= validationForNewFname()
            if not name_update:
                return "Name update failed."
        if choice == 2:
            phone_update= validationForNewPhone()
            if not phone_update:
                return "Phone number update failed."
        if choice == 3:
            name_update= validationForNewFname()
            if not name_update:
                return "Name update failed."
            phone_update= validationForNewPhone()
            if not phone_update:
                return "Phone number update failed."            
        connection = dbConnection()
        if connection is None:
            return "Failed to connect to the database."
        cursor = connection.cursor()
        if choice == 1:
            update_query = """
                UPDATE UserDetails
                SET FullName = %s
                WHERE email_id = %s
            """
            cursor.execute(update_query, (name_update, email_id))
        if choice == 2:
            update_query = """
                UPDATE UserDetails
                SET phone_no = %s
                WHERE email_id = %s
            """
            cursor.execute(update_query, (phone_update, email_id))
        if choice == 3:
            update_query = """
                    UPDATE UserDetails
                    SET FullName = %s, phone_no = %s
                    WHERE email_id = %s
            """
            cursor.execute(update_query, (name_update, phone_update, email_id))
        connection.commit()
        cursor.close()
        connection.close()
        return "User details updated successfully."
    except Exception as e:
        print(f"An error occurred while updating user data: {e}")
        return "Failed to update user details."