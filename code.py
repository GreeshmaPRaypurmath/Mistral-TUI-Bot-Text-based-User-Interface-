from ollama import Client

client = Client(host='http://localhost:11434') 

messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

print("Local ChatBot is ready! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    messages.append({"role": "user", "content": user_input})

    prompt = ""
    for msg in messages:
        prefix = "User:" if msg["role"] == "user" else "Assistant:"
        prompt += f"{prefix} {msg['content']}\n"
    prompt += "Assistant:"

    response = client.generate(model='mistral', prompt=prompt)
    reply = response['response'].strip()
    print(f"ChatBot: {reply}\n")

    messages.append({"role": "assistant", "content": reply})
