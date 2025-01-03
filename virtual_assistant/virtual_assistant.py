# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 22:30:09 2025

@author: Aayush
"""
import webbrowser
import os
import pyttsx3
import speech_recognition as sr
import sqlite3
import datetime
import dateparser
import re
import wikipedia
import subprocess
import pandas as pd
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

def create_table_for_reminders():
    try:
        with sqlite3.connect("reminders.db") as conn:
            cursor = conn.cursor()
            cursor.execute('''
                       CREATE TABLE IF NOT EXISTS reminders(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           message TEXT NOT NULL,
                           reminder_time TIME NOT NULL,
                           reminder_date DATE NOT NULL,
                           created_at DATETIME DEFAULT CURRENT_TIMESTAMP)''')
            conn.commit()
    except sqlite3.Error as e:
        print(f"Database error occurred: {e}")

def add_reminders_to_db(message, reminder_time):
    try:
        reminder_time = dateparser.parse(reminder_time)
        if reminder_time:
            reminder_date = reminder_time.date()
            reminder_time_str = reminder_time.strftime('%H:%M:%S')

            with sqlite3.connect("reminders.db") as conn:
                cursor = conn.cursor()
                cursor.execute('''INSERT INTO reminders (message, reminder_time, reminder_date) 
                                  VALUES (?, ?, ?)''', (message, reminder_time_str, reminder_date))
                conn.commit()
            print(f"Reminder set: {message} at {reminder_time_str} on {reminder_date}")
        else:
            print("Could not parse the time. Please use a valid time format.")
    except Exception as e:
        print(f"Error while adding reminder: {e}")
        
def update_reminders_in_db(reminder_id, new_message=None, new_time=None):
    try:
        with sqlite3.connect("reminders.db") as conn:
            cursor = conn.cursor()
            if new_message:
                cursor.execute('UPDATE reminders SET message = ? WHERE id = ?', (new_message, reminder_id))
            
            if new_time:
                reminder_time = dateparser.parse(new_time)
                if reminder_time:
                    reminder_date = reminder_time.date()
                    reminder_time_str = reminder_time.strftime("%H:%M:%S")
                    cursor.execute('UPDATE reminders SET reminder_time = ?, reminder_date = ? WHERE id = ?',
                                   (reminder_time_str, reminder_date, reminder_id))
                else:
                    print("Invalid time format.")
                    return
            
            conn.commit()
        print(f"Reminder ID {reminder_id} updated successfully.")
    
    except Exception as e:
        print(f"Error while updating reminder: {e}")

def view_reminders_in_db():
    try:
        with sqlite3.connect("reminders.db") as conn:
            cursor = conn.cursor()
            cursor.execute('''SELECT id, message, reminder_date, reminder_time FROM reminders''')
            rows = cursor.fetchall()
            
            if not rows:
                print("No reminders found in the database.")
                return
            
            df = pd.DataFrame(rows, columns=["ID", "Message", "Date", "Time"])
            df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S', errors ='coerce').dt.strftime("%H:%M:%S")
            df = df.sort_values(by="Date", ascending=True)
            print(f"{'ID':<5}| {'Message':<40}| {'Date':^12}| {'Time':^8}")

            # Print each row with '|' separator after each column
            for index, row in df.iterrows():
                print(f"{row['ID']:<5}| {row['Message']:<40}| {row['Date']:^12}| {row['Time']:^8}")
    
    except Exception as e:
        print(f"Error while viewing reminders: {e}") 
        
def delete_reminder_by_id(reminder_id):
    try:
        with sqlite3.connect("reminders.db") as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM reminders WHERE id = ?", (reminder_id,))
            conn.commit()
        print(f"Reminder ID {reminder_id} deleted successfully.")
    
    except sqlite3.Error as e:
        print(f"Error while deleting reminder: {e}")

def delete_reminder_by_message_or_time(keyword):
    try:
        with sqlite3.connect("reminders.db") as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM reminders WHERE message LIKE ? OR reminder_time LIKE ?', ('%' + keyword + '%', '%' + keyword + '%'))
            reminders_to_delete = cursor.fetchall()
        
        if not reminders_to_delete:
            print(f"No reminders found with the keyword '{keyword}'")
            return
        
        print(f"Found the following reminders to be deleted based on your keyword '{keyword}':")
        for reminder in reminders_to_delete:
            print(f"ID: {reminder[0]} | Message: {reminder[1]} | Date: {reminder[3]} | Time: {reminder[2]}")
        
        while True:
            confirmation_from_user = input("Do you want to delete these reminders? (yes/no):\n").strip().lower()
            if confirmation_from_user == "yes":
                for reminder in reminders_to_delete:
                    delete_reminder_by_id(reminder[0])
                break
            elif confirmation_from_user == "no":
                print("No reminders were deleted.")
                break
            else:
                print("Invalid input. Please type 'yes' or 'no'.")
    
    except sqlite3.Error as e:
        print(f"Error while fetching reminders: {e}")

def open_apps(query):
    app_pattern = r"open (.+)"
    match = re.match(app_pattern, query)
    if match:
        app_name = match.group(1).strip().lower()

        # Try to find the application dynamically on the system
        app_executable = find_application(app_name)
        if app_executable:
            print(f"Opening {app_name}")
            set_voice_for_chatbot(f"Opening {app_name}")
            subprocess.Popen(app_executable)  # Open the application using its executable path
            return True
        else:
            # If no app found, check for a website
            return handle_website(query)
    
    # If it's not an app-related query, check for a website
    return handle_website(query)

def search_wikipedia(query):
    search_pattern = r"search wikipedia for (.+)"
    match = re.match(search_pattern, query)
    if match:
        search_query = match.group(1).strip()
        print(f"Searching Wikipedia for {search_query}")
        set_voice_for_chatbot(f"Searching Wikipedia for {search_query}")
        try:
            # First, get the search results
            search_results = wikipedia.search(search_query)  # Search Wikipedia for the term
            if not search_results:
                print("No results found for that query.")
                set_voice_for_chatbot("No results found for that query.")
                return False
            # If there are multiple results, let the user select one
            if len(search_results) > 1:
                print(f"Multiple results found for '{search_query}':")
                for idx, title in enumerate(search_results, 1):
                    print(f"{idx}. {title}")
                user_choice = input("Please enter the number corresponding to the correct page: ").strip()
                try:
                    user_choice = int(user_choice)
                    if 1 <= user_choice <= len(search_results):
                        page_title = search_results[user_choice - 1]
                    else:
                        print("Invalid choice. Please try again.")
                        set_voice_for_chatbot("Invalid choice. Please try again.")
                        return False
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    set_voice_for_chatbot("Invalid input. Please enter a number.")
                    return False
            else:
                # If only one result, use it directly
                page_title = search_results[0]

            # Now fetch the summary and URL for the correct page
            summary = wikipedia.summary(page_title, sentences=2)  # Get the first two sentences of the page
            page_url = wikipedia.page(page_title).url  # Get the URL of the correct page
            print("According to Wikipedia:")
            set_voice_for_chatbot("According to Wikipedia")
            print(summary)
            set_voice_for_chatbot(summary)
            print(f"For more information, visit the URL: {page_url}")
            set_voice_for_chatbot(f"For more information, visit the URL: {page_url}")

        except wikipedia.exceptions.DisambiguationError as e:
            print("The term is ambiguous. Can you be more specific?")
            set_voice_for_chatbot("The term is ambiguous. Can you be more specific?")
        except wikipedia.exceptions.PageError:
            print("I couldn't find any information on that.")
            set_voice_for_chatbot("I couldn't find any information on that.")
        except Exception as e:
            print(f"An error occurred: {e}")
            set_voice_for_chatbot(f"An error occurred: {e}")
        return True

    return False   

def handle_website(query):
    """Handle opening websites."""
    website_pattern = r"open (.+)"
    match = re.match(website_pattern, query)
    if match:
        website = match.group(1).strip().lower()
        print(f"Opening {website} in your browser.")
        set_voice_for_chatbot(f"Opening {website} in your browser.")
        webbrowser.open(f"https://{website}.com")
        return True
    return False

def find_application(app_name):
    """Dynamically search for an application on the system based on the app name."""
    # Common directories where applications are stored on Windows
    search_dirs = [
        r"C:\Program Files",
        r"C:\Program Files (x86)",
        r"C:\Windows\System32",
        r"C:\Users\Public\Desktop",
    ]

    # Convert app_name to lowercase for case-insensitive comparison
    app_name = app_name.lower()

    for directory in search_dirs:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if app_name in file.lower() and file.endswith(".exe"):
                    app_path = os.path.join(root, file)
                    print(f"Found executable: {app_path}")  # Debugging line
                    return app_path

    # If no match is found, return None
    return None

def hello():
    hour = datetime.datetime.now().hour
    if hour < 12 :
        print("Good Morning!")
        set_voice_for_chatbot("Good Morning!")
    elif hour< 18:
        print("Good Afternoon")
        set_voice_for_chatbot("Good Afternoon")
    else:
        print("Good Evening!")
        set_voice_for_chatbot("Good Evening!")
    print("Please enter 1 if you would like to continue with voice chat or 2 for text chat")
    set_voice_for_chatbot("Please enter 1 if you would like to continue with voice chat or 2 for text chat")

def set_voice_for_chatbot(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty("volume", 1)
    engine.setProperty('rate', 150)
    engine.say(audio)
    engine.runAndWait()
    return engine

def commands_for_chatbot():
    recognize = sr.Recognizer()
    
    while True:
        with sr.Microphone() as source:
            # Adjust microphone for ambient noise levels, with a little more time to adapt
            print("Adjusting for ambient noise...")
            recognize.adjust_for_ambient_noise(source, duration=1)
            
            # Set pause threshold (minimum time between phrases to consider it a new command)
            recognize.pause_threshold = 0.5
            print("Listening for command...")
            
            try:
                # Listen to the source (with timeout and phrase length)
                audio = recognize.listen(source, timeout=5, phrase_time_limit=5)
                
                # Recognize speech using Google's Speech Recognition
                Query = recognize.recognize_google(audio).lower()
                print(f"Recognized: {Query}")
                
                if Query:  # If something is recognized
                    return Query  # Return the recognized command

            except sr.UnknownValueError:
                print("Sorry, I didn't catch that. Please try again.")
                set_voice_for_chatbot("Could not understand the audio. Please try again.")
            except sr.RequestError as e:
                print(f"Service error; {e}")
                set_voice_for_chatbot("There was an error with the speech recognition service. Please try again.")
            except Exception as e:
                print(f"An error occurred: {e}")
                set_voice_for_chatbot("An error occurred. Please try again.")
                
def handle_query(query, mode="text"):
    query = query.lower()
    
    if "how are you" in query:
        response = "I am good, Thanks for asking. How can I help you today?"
        print(response)
        set_voice_for_chatbot(response)
        
    elif "exit" in query:
        response = "Bye. Hope you have a good day"
        print(response)
        set_voice_for_chatbot(response)
        return False  # exit the loop
    
    elif query.startswith("set "):
        user_input = query[len("set "):]  # Strip "set "
        time_match = re.search(r"(tomorrow|next\s+[\w]+|in\s+\d+\s+(minutes|hours|days)|at\s+[\d]{1,2}(:\d{2})?\s*(AM|PM)?)", user_input)

        if time_match:
            message = user_input[:time_match.start()].strip()
            reminder_time_str = time_match.group(0).strip()

            # Handle specific time like "at 3 PM"
            if "at" in reminder_time_str:
                time_match = re.search(r"at\s+(\d{1,2}(:\d{2})?\s*(AM|PM)?)", reminder_time_str)
                if time_match:
                    reminder_time_str = time_match.group(1)
            add_reminders_to_db(message, reminder_time_str)
        else:
            print("Invalid input format. Please try again.")
    
    elif "view" in query and "reminder" in query:
        view_reminders_in_db()
    
    elif query.startswith("delete"):
        user_input = query[len("delete"):].strip()
        if user_input.isdigit():
            reminder_id = int(user_input)
            delete_reminder_by_id(reminder_id)
        else:
            delete_reminder_by_message_or_time(user_input)
    
    elif query.startswith("update"):
        user_input = query[len("update "):].strip()
        parts = user_input.split(" with ")
        
        if len(parts) == 2:
            reminder_id = int(parts[0].strip())
            message_time_parts = parts[1].split(" at ")
            if len(message_time_parts) == 2:
                new_message = message_time_parts[0].strip()
                new_time = message_time_parts[1].strip()
                update_reminders_in_db(reminder_id, new_message, new_time)
            else:
                new_message = message_time_parts[0].strip()
                update_reminders_in_db(reminder_id, new_message)
        else:
            print("Invalid format. Please use 'update reminder [ID] with message [new_message] at [new_time]'.")
    
    elif "open" in query:
        open_apps(query)
    
    elif "search wikipedia" in query:
        search_wikipedia(query)
    
    else:
        print("I'm not sure how to respond to that. Can you ask something else?")
        set_voice_for_chatbot("I'm not sure how to respond to that. Can you ask something else?")
    
    return True  # continue the loop

def start_chat(mode="text"):
    print(f"Welcome to {mode} chat. How may I help you today?")
    set_voice_for_chatbot(f"Welcome to {mode} chat. How may I help you today?")
    
    while True:
        query = input().lower()  # get user input
        if not handle_query(query, mode):
            break

def test_chatbot():
    hello()
    input_user = input()
    if input_user == "1":
        start_chat(mode="voice")
    elif input_user == "2":
        start_chat(mode="text")
    else:
        print("Program Failed. Please Run the Program again")

create_table_for_reminders()            
test_chatbot()
