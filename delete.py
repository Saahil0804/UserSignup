from Helper.deletehelper import dbConnection

# Function to allow user to soft delete or hard delete their account
def deleteUserAccount():
    try:
        email_id = input("Enter your registered email: ")
        connection = dbConnection()
        if connection is None:
            return "Failed to connect to the database."
        cursor = connection.cursor()
        auth_query = "SELECT * FROM UserDetails WHERE email_id = %s"    
        cursor.execute(auth_query, (email_id,))
        user = cursor.fetchone()
        if not user:
            print("Authentication failed. Please check your email and try again.")
            return False   
        else:
            print("Authentication successful. You can now delete your account.")
            delete_choice = input("Do you want to (1) Soft Delete or (2) Hard Delete your account? (Enter 1 or 2): ")
            if delete_choice == '1':
                soft_delete_query = "UPDATE UserDetails SET is_active = false WHERE email_id = %s"
                cursor.execute(soft_delete_query, (email_id,))
                connection.commit()
                print("Your account has been soft deleted.")
            elif delete_choice == '2':
                hard_delete_query = "DELETE FROM UserDetails WHERE email_id = %s"
                cursor.execute(hard_delete_query, (email_id,))
                connection.commit()
                print("Your account has been hard deleted.")
            else:
                print("Invalid choice. Please enter 1 or 2.")
            return True
    except Exception as e:
        print(f"An error occurred during account deletion: {e}")
        return False
    
if __name__ == "__main__":
    deleteUserAccount()