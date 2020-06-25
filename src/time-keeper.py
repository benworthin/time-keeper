import os
from datetime import datetime

today = datetime.today()
now = today.strftime('%m-%d-%y %I:%M %p')

digital_signature = ""

if not os.path.exists("../config/digital-signature.txt") or os.path.getsize("../config/digital-signature.txt") == 0:
    with open("../config/digital-signature.txt", 'a+') as digital_signature_text_file:
        digital_signature_initializer = input("Please enter a digital signature to use on Punch Card\n(Recommended: "
                                              "Fullname & ID #)\n> ")
        digital_signature_text_file.write(digital_signature_initializer)
        digital_signature_text_file.seek(0)  # Resets pointer at beginning to capture files contents
        digital_signature = digital_signature_text_file.read()
else:
    with open("../config/digital-signature.txt", "r") as digital_signature_text_file:
        digital_signature = digital_signature_text_file.read()

invalid_input = True
while invalid_input:
    action = input("Type either 'clock in' or 'clock out': ")
    action = action.upper()

    if action == "CLOCK IN" or action == "CLOCK OUT":
        print("Punch Recorded.")
        invalid_input = False
    else:
        print("Invalid input, please try again.")

with open('../punch-card.txt', 'a') as punch_card_txt_file:
    punch_card_txt_file.write(f"{action} at {now} by {digital_signature}\n")
