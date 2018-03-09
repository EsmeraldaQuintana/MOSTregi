
# MOST Registration
Visit registration software suite for the Museum of South Texas History.

### For now, this homepage will serve as the **README**

### Current features:
+ this README
+ Can register events under "New Booking"
 + After booking event, you can view the inputted information
+ Can add/edit/delete events with the Django Administrative Login

### Currently working on:
+ user authentication
 + We have added another user, **employee**, but the authentication isn't fully functional.
+ styling: forms need to look prettier.
+ booking functionality: add, edit, delete.
 + employees should be given the option to edit the form after registering (in the page following submit)
 + "needs auth" feature for bookings registered online
 + easy views for booking information: this week, this month, etc
 + Museum Event handling: ability to see what bookings coincide with official museum events
+ finishing this list...

### Build Dependencies
+ Python3
+ pip3
+ Django >=2
+ django-bootstrap3 >=9
+ django-phonenumber-field >=2.0
+ psycopg2 >=2.7
