# Vlad Chevdar | CS302 | Aug 25
# Purpose of this program is to report weather to the user
# based on the provided locations or access old reports
from Avl     import * 
from random  import sample

# Sign up user and add to the tree
def sign_up(tree):
    print('🌟 Welcome to the Signup Portal 🌟')

    # Find user by given name
    first_name = input("Enter your first name: ") 
    last_name = input("Enter your last name: ")
    new_user = User(first_name, last_name)

    if tree.find(new_user):
        print(f'{first_name} is already registered! Consider logging in instead.')
        return False

    # Give user three tries to create password
    count = 0
    while count < 3:
        password = input('Choose a password: ')
        confirm = input('Re-enter your password for confirmation: ')

        if password != confirm:
            count += 1
            if count < 3:
                print(f"Oops! Passwords didn't match. Please try again.")
            else:
                print('Too many failed attempts. Please take a moment and try the signup process later.')
                return False
        else:
            new_user.setPassword(password)
            tree.insert(new_user)
            print(f'Your signup was successful. Enjoy our services!')
            return tree.get_user(new_user)

# Search if the user is in the tree, if yes then access data
def log_in(tree):
    print('Log in')
    first_name = input("Enter your first name: ") 
    last_name = input("Enter your last name: ")
    user = User(first_name, last_name)

    try:
        isFound = tree.find(user)
    except Exception as e:
        print(f'Error: {e}')
        return False

    # If user is found, give the user three tries to enter password
    count = 0
    if isFound:
        for count in range(3):
            password = input("Enter your password: ")
            user.setPassword(password)
            verified = tree.verify(user)
            if verified:
                print(f'Welcome, {first_name.title()}! You are now logged in.')
                return tree.get_user(user)
            else:
                print(f'Oops! Incorrect password. Try again. ({count+1}/3 attempts used)')
                if count == 2:
                    print('Incorrect password! You have exhausted all attempts. Please try again later.')
                    return False
    else:
        print('No account found with that name. Ensure you have signed up or check the spelling and try again.')
        return False

# Display all signed up users
def display_tree(tree):
    access_code = input('Access code: ')
    if access_code == 'Vlad':
        tree.display()
    else:
        print('Access denied')

# Search weather and store it in the user's search history
def search_weather(user, weather_report):
    city = input("\nCity: ")
    state = input("Country or State: ")
    city = city.upper() if len(city) < 4 else city.title()
    state = state.upper() if len(state) < 4 else state.title()
    location = (city + ', ' + state)
    print(f'🌍 Searching for the weather in {location}...')
    user.add_new_activity(f'You requested for the weather in {location}')

    if weather_report.get_weather(location):
        user.add_to_history(location)
        weather_report.display()

# Report data based on the option user chooses
def reportWeather(user):
    print('\n(1) - Look Up Weather')
    print('(2) - View Recent Weather Lookup')
    print('(3) - View All Previous Weather Lookups')
    print('(4) - Remove Last Weather Lookup')
    print('(5) - Clear All Weather Lookups')
    print('(6) - Show My Activity History')
    print('(0) - Log out')
    option = input('\nOption: ')

    if option == '0':
        user.add_new_activity("You logged out")
        print('You successfully logged out')
        return

    if option in ['1', '2', '3']:
        print('\n(1) - Snapshot Weather Report')
        print('(2) - In-Depth Weather Analysis')
        print('(3) - Weather with a Twist of Humor')
        report_option = input('\nOption: ')

        # Based on the user's choice, create the weather report
        report_activity = ''
        if report_option == '1':
            report_activity = "Brief report"
            weather_report = BriefReport()
        elif report_option == '2':
            report_activity = "Detailed report"
            weather_report = DetailedReport()
        elif report_option == '3':
            report_activity = "Funny report"
            weather_report = FunnyReport()
        else:
            print("Invalid option! Try again.")
            return reportWeather(user)

        if option == '1':
            user.add_new_activity(f'You requested: {report_activity} for one location')
            search_weather(user, weather_report)
        elif option == '2':
            user.add_new_activity(f'You requested: {report_activity} for recent location')
            user.get_recent_weather(weather_report)
        elif option == '3':
            user.add_new_activity(f'You requested: {report_activity} for all searched locations')
            user.get_all_weather(weather_report)

    elif option == '4':
        user.add_new_activity("You deleted last weather search")
        user.clear_last_search()
    elif option == '5':
        user.add_new_activity("You deleted all weather searches")
        user.clear_all_searches()
    elif option == '6':
        user.add_new_activity("You viewed activity history")
        user.display_activity()
    else:
        print("Invalid option! Try again.")

    return reportWeather(user)

# Display a little help for a user
def print_help():
    print("\n" + "="*40)
    print("WELCOME TO WEATHER WIZARD!".center(40))
    print("="*40)
    
    print("\n🌦 SIGN UP 🌦")
    print("- Explore weather data from cities worldwide.")
    print("- Get personalized weather alerts and updates.")
    print("- Benefit: Stay informed and plan your day efficiently!")

    print("\n🌍 LOG IN 🌍")
    print("- Revisit your previous searches effortlessly.")
    print("- Save and manage your favorite cities.")
    print("- Benefit: A tailored weather experience at your fingertips!")

    print("\nWhat would you like to do next? (Choose an option from the main menu!)")

# Display main menu options, and call the necessary functions
def main_menu():
    print('\n(1) - Create New Account')
    print('(2) - Access Your Account')
    print('(3) - Learn More')
    print('(0) - Exit Application')
    option = input('\nOption: ')

    user = None
    if option == '1':
        user = sign_up(tree)
        if user:
            user.add_new_activity(f'You signed up')
    elif option == '2':
        user = log_in(tree)
        if user:
            user.add_new_activity(f'You logged in')
    elif option == '3':
        print_help()
    elif option == '4':
        display_tree(tree)
    elif option == '0':
        tree.save_data('data.txt')
        print('Thank you for using Weather Wizard app. Goodbye!')
        return
    else:
        print("Invalid option! Try again.")

    if option == '1' or option == '2':
        if user:
            reportWeather(user)

    return main_menu()

if __name__ == '__main__':
    tree = AVL()
    tree.load_data('data.txt')
    print_help()
    main_menu()
