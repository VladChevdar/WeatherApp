# Vlad Chevdar | CS302 | Aug 25
# Purpose of this file is to have a user data type
from Weather import *

class User:
    def __init__(self, first_name, last_name, password = 'default'):
        self.__first_name = first_name.title()
        self.__last_name = last_name.title()
        self.__password = password
        self.__username = f'{first_name.lower()}{last_name.lower()}@weather.com'
        self.__report_history = [] # Stores locations of previous reports
        self.__activity_history = [] # Stores everything user was doing on the program
    
    def __del__(self):
        self.__first_name = ''
        self.__last_name = ''
        self.__password = ''
        self.__username = ''
        self.__report_history = []
        self.__track_history = []

    # Add a new activity to the track history
    def add_new_activity(self, new_activity):
        self.__activity_history.append(new_activity)

    # Display all user's activity
    def display_activity(self):
        for activity in self.__activity_history:
            print(activity)

    # Return data packed for external file use
    def get_data(self):
        reports = ''
        for location in self.__report_history:
            reports += (location + '|')

        return(f'{self.__first_name}|{self.__last_name}|{self.__password}|{reports}')

    #  Delete report history
    def clear_all_searches(self):
        if self.__report_history:
            self.__report_history = []
            print('All searches have been arased!')
        else:
            print('You search history is empty!')

    # Delete last element of the report history
    def clear_last_search(self):
        if self.__report_history:
            self.__report_history.pop()
            print('Last search has been deleted!')
        else:
            print('You search history is empty!')

    # Change password
    def setPassword(self, password):
        self.__password = password

    # Compare names 
    def compare(self, user):
        if (self.__username > user.__username):
            return 1
        elif (self.__username < user.__username):
            return -1
        else:
            return 0

    # Add a report to the history 
    def add_to_history(self, location):
        if location not in self.__report_history:
            self.__report_history.append(location)

    # Display weather for all locations in the report history
    def get_all_weather(self, report):
        if not self.__report_history:
            print('History is empty')
        else:
            for location in self.__report_history:
                report.get_weather(location)
                report.display()

    # Display the weather of the last element of the report history
    def get_recent_weather(self, report):
        if not self.__report_history:
            print('History is empty')
        else:
            last = len(self.__report_history) - 1
            location = self.__report_history[last]
            report.get_weather(location)
            report.display()

    # Return true if username and password match
    def login(self, user):
        return self.__username == user.__username and self.__password == user.__password

    # Display user, user for testing purposes, hidden from ordinary users
    def display(self):
        print(f'\n{self.__first_name}, {self.__last_name}')        
        print(f'Username: {self.__username}')        
        print(f'Password: {self.__password}')        