import time
from playsound import playsound

class myAlarm():
	def __init__(self):
		self.hour = input("Please enter a hour: ")
		self.minute = input("Please enter a minute: ")

	def alarm(self):
		while True:
			self.hour_now = time.strftime("%H")
			self.minute_now = time.strftime("%M")
			if self.hour == self.hour_now:
				if self.minute == self.minute_now:
					print("Get up!")
					playsound("C:\\Users\\murat\\Music\\asker.wav")
					time.sleep(2)
					#playsound("C:\\Users\\murat\\Music\\waltz_for_tomorrow.wav")
					break
			time.sleep(30)

my_instance = myAlarm()
my_instance.alarm()