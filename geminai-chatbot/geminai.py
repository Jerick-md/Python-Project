import google.generativeai as genai

genai.configure(api_key="your_Api_key")
model = genai.GenerativeModel('gemini-2.0-flash')
chat = model.start_chat()

while True:
    userinput = input("Start chatting: ")
    if userinput.lower() == 'x':
        break
    respone = chat.send_message(userinput).text
    print("AI Respone: ", respone)