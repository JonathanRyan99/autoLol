#accept button
import pyautogui


def press_AcceptButton():
	try:
		pyautogui.click('interface/accept.PNG')
		print("accept pressed")
	except:
		print("AcceptButton not found")
		return False
	return True

press_AcceptButton()