import time
import ollama

f = open("page.txt", "r")
text = f.read()

tinyllamaStart = time.time()
print("Starting TinyLlama")
response = ollama.chat(model='tinyllama', messages=[{'role': 'user', 'content': 'summarize this: ' + text}])
print(response['message']['content'])
tinyLlamaEnd = time.time()
tinyLlamaTime = tinyLlamaEnd-tinyllamaStart
print("TinyLlama: " + str(tinyLlamaTime))

phi3Start = time.time()
print("Starting phi3")
response = ollama.chat(model='phi3', messages=[{'role': 'user', 'content': 'summarize this: ' + text}])
print(response['message']['content'])
phi3End = time.time()
phi3Time = phi3End-phi3Start
print("phi3: " + str(phi3Time))

mistralStart = time.time()
print("Starting mistral")
response = ollama.chat(model='mistral', messages=[{'role': 'user', 'content': 'summarize this: ' + text}])
print(response['message']['content'])
mistralEnd = time.time()
mistralTime = mistralEnd-mistralStart
print("mistral: " + str(mistralTime))

orcaStart = time.time()
print("Starting orca")
response = ollama.chat(model='orca-mini', messages=[{'role': 'user', 'content': 'summarize this: ' + text}])
print(response['message']['content'])
orcaEnd = time.time()
orcaTime = orcaEnd-orcaStart
print("orca: " + str(orcaTime))

print("TinyLlama: " + str(tinyLlamaTime))
print("phi3: " + str(phi3Time))
print("mistral: " + str(mistralTime))
print("orca: " + str(orcaTime))