import openai
class TxtColor:
	GREEN = '\033[92m'
	ENDC = '\033[0m' 
# Set OpenAI API key
openai.api_key = "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"  
# Initialize message list
ChatMessages = []  
while True:
	# Prompt user for input
	user_input = input(": ")
	# Add user input to message list
	# [{"role": "user", "content": "Hello!"}]
	ChatMessages.append({"role": "user", "content": user_input})
	# Check if user wants to quit
	# print (messages)
	if user_input.lower() == 'q':
		break
	# Generate response from OpenAI language model
	response = openai.ChatCompletion.create(
		model="gpt-3.5-turbo",
		messages=ChatMessages )
    # Print the response from the language model
    print(TxtColor.GREEN + response.choices[0].message.content + TxtColor.ENDC)
    #print( response.choices[0].message.content)
    # Add response to message list
    ChatMessages.append({"role": "assistant", "content": response.choices[0].message.content})
    # Print separator line
    print("____________________________________")
