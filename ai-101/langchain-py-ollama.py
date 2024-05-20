from langchain.llms import Ollama

input = input("Hi there, tell me about Paris ?")
llm = Ollama(model="llama3")
res = llm.predict(input)
print (res)