from Helper.updateHelper import dbConnection
from Helper.updateHelper import update_user_data
from datetime import datetime




# Function to allow user to update phone number and full name only after signing in
def updateUserDetails():
    try:
        email_id = input("Enter your registered email: ")
        connection = dbConnection()
        if connection is None:
            return "Failed to connect to the database."
        cursor = connection.cursor()
        auth_query = "SELECT * FROM UserDetails WHERE email_id = %s AND is_active = true"    
        cursor.execute(auth_query, (email_id,))
        user = cursor.fetchone()
        if not user:
            print("Authentication failed. Please check your email and try again.")
            return False   
        else:
            print("Authentication successful. You can now update your details.")
            return email_id
    except Exception as e:
        print(f"An error occurred during user authentication: {e}")
        return False

def updatechoices():
            try:
                update_choice = input("What would you like to update? (1) Name (2) Phone Number (3) Both (Enter 1, 2, or 3): ")
                if update_choice == '1':
                    return 1
                elif update_choice == '2':
                    return 2    
                elif update_choice == '3':
                    return 3                  
                else:
                    return "Invalid choice. Please enter 1, 2, or 3."
            except Exception as e:
                print(f"An error occurred during update choice selection: {e}")
           



if __name__ == "__main__":
    email_id = updateUserDetails()
    if email_id: 
        choice = updatechoices()
        if choice :
             update_user_data(email_id, choice)
            
        