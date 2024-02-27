# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List
import mysql.connector
from mysql.connector import Error
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import sqlite3
import random
from fuzzywuzzy import process


class DbQueryingMethods:

    def get_closest_value(conn, slot_name, slot_value):
        """ Given a database column & text input, find the closest 
        match for the input in the column.
        """
        # get a list of all distinct values from our target column
        fuzzy_match_cur = conn.cursor()
        fuzzy_match_cur.execute(f"""SELECT DISTINCT {slot_name} 
                                FROM products""")
        column_values = fuzzy_match_cur.fetchall()

        top_match = process.extractOne(slot_value, column_values)

        return(top_match[0])
    

class ActionProduct(Action):

    def name(self) -> Text:
        return "action_product"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            # Connect to MySQL database
            connection = mysql.connector.connect(
                host='localhost',
                port='3306',
                database='esquery',
                user='root',
                password='Ujjwal@123',
                charset='utf8'
            )

            if connection.is_connected():
                dispatcher.utter_message("Connected to MySQL!")

                # Execute your SQL query here
                sql_select_Query = "SELECT * FROM products LIMIT 5"
                cursor = connection.cursor()    
                # cursor = connection.cursor()
                cursor.execute(sql_select_Query)
                records = cursor.fetchall()

                for row in records:
                    dispatcher.utter_message(f"{row}")
               

            else:
                dispatcher.utter_message("Error: Unable to connect to MySQL database.")

        except Error as e:
            dispatcher.utter_message(f"Error while connecting to MySQL: {e}")

        finally:
            # Close the database connection in the 'finally' block to ensure it always happens
            if 'connection' in locals() and connection.is_connected():
                connection.close()

        return []

from fuzzywuzzy import process

# Define a list of known entity values
known_entity_values = ["Bangles", "Headset", "Hairclip", "Choker", "Necklace", "Tops", "Jali belt", "Vankey", "jumky"]

# Function to perform fuzzy matching and extract entity
def extract_entity(text):
    # Use fuzzy matching to find the closest match to the input text from the list of known entity values
    match, score = process.extractOne(text, known_entity_values)
    
    # If the similarity score is above a certain threshold, consider it a match
    if score >= 80:  # Adjust threshold as needed
        return match
    else:
        return None

class ActionShowImages(Action):

    def name(self) -> Text:
        return "action_show_images"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            # Connect to MySQL database
            connection = mysql.connector.connect(
                host='localhost',
                port='3306',
                database='esquery',
                user='root',
                password='Ujjwal@123',
                charset='utf8'
            )

            
            if connection.is_connected():
                dispatcher.utter_message("Connected to MySQL!")

                entities = tracker.latest_message.get("entities", [])
                for ent in entities:
                    dispatcher.utter_message(f"The entities of the user's prompt is: {ent}")
                
                # Extracting the intent of the user's latest message
                intent = tracker.latest_message['intent'].get('name')
                dispatcher.utter_message(f"The intent of the user's prompt is: {intent}")
                
                latest_message = tracker.latest_message.get('text', '')
                dispatcher.utter_message(f"The user said: {latest_message}")


                # Example usage
                # user_input = "I'm looking for a nacklace"
                user_input = latest_message
                entity = extract_entity(user_input)
                if entity:
                    dispatcher.utter_message(f"Entity extracted: {entity}")
                else:
                    dispatcher.utter_message("Entity not found.")

                if entity:
                    resource_topic = entity
                    # resource_topic = tracker.get_slot("resource_topic")
                    # adding fuzzy matching
                    dispatcher.utter_message(text=resource_topic)
                    # resource_topic = DbQueryingMethods.get_closest_value(conn=connection,slot_name="title",slot_value=resource_topic)[0]
                    # Execute your SQL query here
                    # sql_select_Query = "SELECT * FROM products LIMIT 10"
                    # Execute your SQL query here using the 'resource_topic' value
                    # dispatcher.utter_message(text=resource_topic)
                    sql_select_Query = f"SELECT image_link FROM products WHERE title LIKE '%{resource_topic}%' LIMIT 10"
                    
                    cursor = connection.cursor()    
                    # cursor = connection.cursor()
                    cursor.execute(sql_select_Query)
                    records = cursor.fetchall()

                    for row in records:
                        if row:
                            dispatcher.utter_message(text = row[0])
                            # dispatcher.utter_message(image= row)
                        else:
                            dispatcher.utter_message(text="Sorry, I couldn't find information for that product.")
                else:
                    dispatcher.utter_message(text="No such product found in database!")
                # if entities:
                #     resource_topic = entities[0].get("value", "")
                #     # resource_topic = tracker.get_slot("resource_topic")
                #     # adding fuzzy matching
                #     dispatcher.utter_message(text=resource_topic)
                #     resource_topic = DbQueryingMethods.get_closest_value(conn=connection,slot_name="title",slot_value=resource_topic)[0]
                #     # Execute your SQL query here
                #     # sql_select_Query = "SELECT * FROM products LIMIT 10"
                #     # Execute your SQL query here using the 'resource_topic' value
                #     dispatcher.utter_message(text=resource_topic)
                #     sql_select_Query = f"SELECT image_link FROM products WHERE title LIKE '%{resource_topic}%' LIMIT 10"
                    
                #     cursor = connection.cursor()    
                #     # cursor = connection.cursor()
                #     cursor.execute(sql_select_Query)
                #     records = cursor.fetchall()

                #     for row in records:
                #         if row:
                #             dispatcher.utter_message(text = row[0])
                #             # dispatcher.utter_message(image= row)
                #         else:
                #             dispatcher.utter_message(text="Sorry, I couldn't find information for that product.")
                # else:
                #     dispatcher.utter_message(text="No such product found in database!")
            else:
                dispatcher.utter_message("Error: Unable to connect to MySQL database.")

        except Error as e:
            dispatcher.utter_message(f"Error while connecting to MySQL: {e}")

        finally:
            # Close the database connection in the 'finally' block to ensure it always happens
            if 'connection' in locals() and connection.is_connected():
                connection.close()

        return []
    

