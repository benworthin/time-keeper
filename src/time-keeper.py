import os
import csv
from datetime import datetime

digitalSignature = "Benjamin A. Worthington (010895994)"

today = datetime.today()
now = today.strftime('%m-%d-%y %I:%M %p')

invalidInput = True

while invalidInput:
    action = input("Type either 'clock-in' or 'clock-out': ")
    action = action.upper()

    if action == "CLOCK-IN" or action == "CLOCK-OUT":
        print("Punch Recorded.\n")
        invalidInput = False
    else:
        print("Invalid input, please try again.")

with open('../punch-card.txt', 'a') as punch_card_txt_file:
    punch_card_txt_file.write(f"{action} at {now} by {digitalSignature}\n")