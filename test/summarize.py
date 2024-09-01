import ollama

f = open("pg1.txt", "r")
text = f.read()

print("Starting summary")
response = ollama.chat(model='phi3', messages=[{'role': 'user', 'content': 'summarize this: ' + text}])
print(response['message']['content'])
f = open("summary.txt", "w")
f.write(response['message']['content'])
f.close