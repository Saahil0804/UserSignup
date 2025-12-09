import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()

# Function to connect postgreSQL to the database
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
# Function to sign in an existing user
def signInUser():
    try:
        connection = dbConnection()
        if connection is None:
            return

        cursor = connection.cursor()

        email_id = input("Enter your email: ")
        Pword = input("Enter your password: ")
    except Exception as e:
        print("Invalid email or password.")
        return

    try:
        connection = dbConnection()
        if connection is None:
            return

        cursor = connection.cursor()
        select_query = """
                SELECT * FROM UserDetails WHERE email_id = %s AND Pword = %s
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
    dbConnection()
    signInUser()
    
