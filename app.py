################################################
####                                        ####
#### Written By: SATYAKI DE                 ####
#### Written On: 24-Nov-2020                ####
#### Briefcase, Toga, json, requests needs  ####
#### to install to run this package.        ####
####                                        ####
#### Objective: This script will create a   ####
#### native I/OS App using native Python.   ####
####                                        ####
################################################
 
"""
Calling Azure Microservice from Native Mobile App
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import requests
import json
 
class online_checkin(toga.App):
 
    def startup(self):
        """
        Construct and show the Toga application.
 
        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))
 
        # Adding Individual Layout details
        name_label = toga.Label("Full Name", style=Pack(padding=(0, 5)))
        self.name_input = toga.TextInput(style=Pack(flex=1))
 
        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)
 
        mobile_label = toga.Label("Mobile", style=Pack(padding=(0, 5)))
        self.mobile_input = toga.TextInput(style=Pack(flex=1))
 
        mobile_box = toga.Box(style=Pack(direction=ROW, padding=5))
        mobile_box.add(mobile_label)
        mobile_box.add(self.mobile_input)
 
        email_label = toga.Label("Email", style=Pack(padding=(0, 5)))
        self.email_input = toga.TextInput(style=Pack(flex=1))
 
        email_box = toga.Box(style=Pack(direction=ROW, padding=5))
        email_box.add(email_label)
        email_box.add(self.email_input)
 
        source_label = toga.Label("Source Airport", style=Pack(padding=(0, 5)))
        self.source_input = toga.TextInput(style=Pack(flex=1))
 
        source_box = toga.Box(style=Pack(direction=ROW, padding=5))
        source_box.add(source_label)
        source_box.add(self.source_input)
 
        destination_label = toga.Label("Destination Airport", style=Pack(padding=(0, 5)))
        self.destination_input = toga.TextInput(style=Pack(flex=1))
 
        destination_box = toga.Box(style=Pack(direction=ROW, padding=5))
        destination_box.add(destination_label)
        destination_box.add(self.destination_input)
 
        boardingclass_label = toga.Label("Boarding Class", style=Pack(padding=(0, 5)))
        self.boardingclass_input = toga.TextInput(style=Pack(flex=1))
 
        boardingclass_box = toga.Box(style=Pack(direction=ROW, padding=5))
        boardingclass_box.add(boardingclass_label)
        boardingclass_box.add(self.boardingclass_input)
 
        preferredSeatNo_label = toga.Label("Preferred Seat", style=Pack(padding=(0, 5)))
        self.preferredSeatNo_input = toga.TextInput(style=Pack(flex=1))
 
        preferredSeatNo_box = toga.Box(style=Pack(direction=ROW, padding=5))
        preferredSeatNo_box.add(preferredSeatNo_label)
        preferredSeatNo_box.add(self.preferredSeatNo_input)
 
        mealBreakfast_label = toga.Label("Breakfast Choice", style=Pack(padding=(0, 5)))
        self.mealBreakfast_input = toga.TextInput(style=Pack(flex=1))
 
        mealBreakfast_box = toga.Box(style=Pack(direction=ROW, padding=5))
        mealBreakfast_box.add(mealBreakfast_label)
        mealBreakfast_box.add(self.mealBreakfast_input)
 
        mealLunch_label = toga.Label("Lunch Choice", style=Pack(padding=(0, 5)))
        self.mealLunch_input = toga.TextInput(style=Pack(flex=1))
 
        mealLunch_box = toga.Box(style=Pack(direction=ROW, padding=5))
        mealLunch_box.add(mealLunch_label)
        mealLunch_box.add(self.mealLunch_input)
 
        mealDinner_label = toga.Label("Dinner Choice", style=Pack(padding=(0, 5)))
        self.mealDinner_input = toga.TextInput(style=Pack(flex=1))
 
        mealDinner_box = toga.Box(style=Pack(direction=ROW, padding=5))
        mealDinner_box.add(mealDinner_label)
        mealDinner_box.add(self.mealDinner_input)
 
        passPort_label = toga.Label("Passport Details", style=Pack(padding=(0, 5)))
        self.passPort_input = toga.TextInput(style=Pack(flex=1))
 
        passPort_box = toga.Box(style=Pack(direction=ROW, padding=5))
        passPort_box.add(passPort_label)
        passPort_box.add(self.passPort_input)
 
        localAddress_label = toga.Label("Local Address", style=Pack(padding=(0, 5)))
        self.localAddress_input = toga.TextInput(style=Pack(flex=1))
 
        localAddress_box = toga.Box(style=Pack(direction=ROW, padding=5))
        localAddress_box.add(localAddress_label)
        localAddress_box.add(self.localAddress_input)
 
        bookingNo_label = toga.Label("Confirmed Booking No", style=Pack(padding=(0, 5)))
        self.bookingNo_input = toga.TextInput(style=Pack(flex=1))
 
        bookingNo_box = toga.Box(style=Pack(direction=ROW, padding=5))
        bookingNo_box.add(bookingNo_label)
        bookingNo_box.add(self.bookingNo_input)
 
        # End Of Layout details
 
        boardingStatus_box_label = toga.Label("Boarding Status", style=Pack(padding=(0, 5)))
        self.boardingStatus_box_input = toga.MultilineTextInput(readonly=True, style=Pack(flex=1))
        boardingStatus_box = toga.Box(style=Pack(direction=ROW, padding=5))
        boardingStatus_box.add(boardingStatus_box_label)
        boardingStatus_box.add(self.boardingStatus_box_input)
 
        button = toga.Button("On-Board Now", on_press=self.onBoarding, style=Pack(padding=5))
 
        # Adding all the visual layout in the main frame
 
        main_box.add(name_box)
        main_box.add(mobile_box)
        main_box.add(email_box)
        main_box.add(source_box)
        main_box.add(destination_box)
        main_box.add(boardingclass_box)
        main_box.add(preferredSeatNo_box)
        main_box.add(mealBreakfast_box)
        main_box.add(mealLunch_box)
        main_box.add(mealDinner_box)
        main_box.add(passPort_box)
        main_box.add(localAddress_box)
        main_box.add(bookingNo_box)
        main_box.add(button)
        main_box.add(boardingStatus_box)
 
        # End Of Main Frame
 
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()
 
    def onBoarding(self, widget):
 
        BASE_URL = "https://xxxxxxxxxx.yyyyyyyy.net/api/getOnBoarding"
        openmapapi_cache = "no-cache"
        openmapapi_con = "keep-alive"
        type = "application/json"
 
        querystring = { "sourceLeg":  self.source_input.value, "destinationLeg":  self.destination_input.value,
                        "boardingClass":  self.boardingclass_input.value, "preferredSeatNo":  self.preferredSeatNo_input.value,
                        "travelPassport":  self.passPort_input.value , "bookingNo":  self.bookingNo_input.value,
                        "travelerEmail":  self.email_input.value, "travelerMobile": self.mobile_input.value,
                        "mealBreakFast":  self.mealBreakfast_input.value , "mealLunch":  self.mealLunch_input.value,
                        "mealDinner":  self.mealDinner_input.value, "localAddress":  self.localAddress_input.value }
 
        payload = json.dumps(querystring)
 
        print('Input Payload: ')
        print(payload)
 
        headers = {
            'content-type': type,
            'Cache-Control': openmapapi_cache,
            'Connection': openmapapi_con
        }
 
        response = requests.request("POST", BASE_URL, headers=headers, data=payload)
        ResJson = response.text
 
        #jdata = json.dumps(ResJson)
        resp = json.loads(ResJson)
 
        print('Response JSON:')
        print(resp)
 
        details = resp["description"].strip()
        status = str(resp["status"]).strip()
        sourceAirport = str(resp["sourceLeg"]).strip()
        destinationAirport = str(resp["destinationLeg"]).strip()
        boardingClass = str(resp["boardingClass"]).strip()
        confirmedSeat = str(resp["confirmedSeatNo"]).strip()
 
        try:
            self.boardingStatus_box_input.value = f'Please find the update on your itenary -> Source - {sourceAirport} to Destination - {destinationAirport} - ' \
                                                  f'Boarding Class - {boardingClass} - Confirmed Seat - {confirmedSeat} and ' \
                                                  f'the summary is as follows  - {details} - Status - {status}'
        except ValueError:
            self.boardingStatus_box_input.value = "Some technical issue occured. We are working on it."
 
def main():
    return online_checkin()
