from Helper.SignUpHelper import dbConnection
    
# Function to sign in an existing user
def signInUser():
    try:
        connection = dbConnection()
        if connection is None:
            return "Failed to connect to the database."
        cursor = connection.cursor()
        email_id = input("Enter your email: ")
        Pword = input("Enter your password: ")
    except Exception as e:
        print("Invalid email or password.")
        return "Error during sign-in: {e}"

    try:
        connection = dbConnection()
        if connection is None:
            return

        cursor = connection.cursor()
        select_query = """
                SELECT * FROM UserDetails WHERE email_id = %s AND Pword = %s AND is_active = TRUE
            """
        cursor.execute(select_query, (email_id, Pword))
        user = cursor.fetchone()

        if user:
            print("User signed in successfully!")
        else:
            print("Invalid email or password.")
    except Exception as e:
            print(f"Error retrieving user data: {e}")
    finally:
            cursor.close()
            connection.close()

# Main execution
if __name__ == "__main__":
    signInUser()
    
