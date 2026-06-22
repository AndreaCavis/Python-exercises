'''
Congratulations on completing your first run, Space Voyager! 
Now, it's time for a deeper dive. Assume you are managing events within an event system.

Could you modify the starter code to update the description of the Python Webinar and verify the final event list? 
We need to clarify the Python Webinar is going to be focused on Data Structures, and we should also reschedule it to a different time.

Let's venture forth, astronaut!
'''

# Create a Python dictionary that acts as a hash table
event_system = {}

# Add upcoming events
event_system[1] = "Coding Bootcamp - Monday, 8:00 AM"
event_system[2] = "Python Webinar - Tuesday, 10:00 AM"
event_system[3] = "Data Science Meetup - Wednesday, 6:00 PM"

# TODO: Update the Python Webinar description
# Note: don't change previous definitions of `event_system` elements.
event_system[2] = "Python Webinar (Data Structures) - Tuesday, 9:00 AM"

# Print the updated events list
print("\nUpdated upcoming events:")
for event_id, event_desc in event_system.items():
    print(f"Event ID: {event_id}, Description: {event_desc}")