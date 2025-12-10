# Function to connect to the database
import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()


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