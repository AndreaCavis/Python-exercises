'''
Fantastic progress, future space engineer! Now, let's take an even bigger leap with Python dictionaries.

The starter code provided manages space mail received from different space stations. Each station sends a unique ID along with their messages. 
Our system records all incoming messages, removing them once we've read them.

However, we've received a message from an unknown space station not recognized by our current system. 
Should you choose to accept it, your mission is to add this incoming message using a unique ID 
and verify that all received messages, including the new one, are updated in our system.

Venture forth, stellar navigator!
'''

# Initialize an empty dictionary as a Hash Table
spacemail = {}

# Let's populate with incoming messages
spacemail['Station Alpha'] = 'Supply request: cosmic fuel'
spacemail['Station Beta'] = 'Engineering report: engines operational'
spacemail['Station Gamma'] = 'Medical report: crew status healthy'

# Let's print the initial spacemail log
print("Initial Spacemail Log:")
for station, message in spacemail.items():
    print(f"Station: {station}, Message: {message}")

# TODO: Add a new message from Station Delta and verify the updated spacemail log
spacemail['Station Delta'] = "This is a new message from Space Delta, requesting connection"

print("\nUpdated spacemail log")
for station, message in spacemail.items():
    print(f"Station: {station}, Message: {message}")