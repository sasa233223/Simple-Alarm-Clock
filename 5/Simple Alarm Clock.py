import time
import winsound  # Works on Windows for sound

def alarm_clock():
    alarm_time = input("Set alarm time (HH:MM): ")

    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            print("It's time!")
            winsound.Beep(1000, 1000)  # Beep for 1 second
            break
        time.sleep(30)  # Check time every 30 seconds

alarm_clock()
