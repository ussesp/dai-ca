'''prompt = "Enter a message. Enter quit to stop the program:"
message = ""
while message != "quit":
	message = input(prompt)

while prompt2 = "Enter another message:":
	message2 != "cancel":
	message2 = input(prompt2)
	print (message)
	print (message2)
'''

prompt = "Enter a message. Enter quit to stop the program:"
message = ""
active = True
while active:
	message = input(prompt)
	if message == "quit":
		active = False	
	else:
		prompt2 = "Enter another message:"
		while True:
			message2 = input(prompt2)
			if message2 == "cancel":
				active = False
				break				
			else:
				print (message)
				print (message2)
							