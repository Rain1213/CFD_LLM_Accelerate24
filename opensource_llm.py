from transformers import pipeline

# load an open source LLM
generator = pipeline("text-generation", model="gpt2")

# give prompt
str_prompt = "What is a transformer model? Explain like I am five."

output = generator(str_prompt, max_length = 1000, num_return_sequences = 1)

# print
print(output[0]["generated_text"])

