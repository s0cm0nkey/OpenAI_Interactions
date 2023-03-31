import openai 

openai.api_key = "API_KEY_HERE" 

inp = input('Paste Command Line Text\n') 

prompt = "Explain the following command string or code:" + inp 

response = openai.Completion.create(model="text-davinci-003", 

prompt=prompt, temperature=0.7, max_tokens=3000) 

print("Command Explanation") 

print(response['choices'][0]['text']) 
