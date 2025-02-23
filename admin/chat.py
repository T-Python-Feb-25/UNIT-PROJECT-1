'''from transformers import pipeline, GPT2LMHeadModel, GPT2Tokenizer
import torch
import re

# Load a pre-trained model for general question answering
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

# Load the distilGPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("distilgpt2")
model = GPT2LMHeadModel.from_pretrained("distilgpt2")

# Move the model to GPU if available
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

# Set pad_token_id to eos_token_id (common approach for GPT-2)
tokenizer.pad_token = tokenizer.eos_token


context_time_weather = """ .........."""

context



# Combine all contexts into one
combined_context = context_saudi_arabia + " " + context_riyadh + " " + context_time_weather

# Function to extract temperature information in Celsius from context
def extract_temperature_from_context():
    # Look for temperature values in the context
    temp_match = re.findall(r'(\d{2,3})°C', context_time_weather)
    if temp_match:
        # Return the first temperature found in Celsius
        return temp_match[0] + "°C"
    else:
        return "No temperature information found."

# Function to answer questions based on multiple contexts
def answer_question(question):
    result = qa_pipeline({
        'context': combined_context,
        'question': question
    })
    return result['answer']

# Function to generate response using GPT-2
def generate_response(prompt):
    # Tokenize the input text
    inputs = tokenizer.encode(prompt, return_tensors="pt").to(device)
    attention_mask = torch.ones(inputs.shape, dtype=torch.long).to(device)

    # Generate a response (limit response to 100 tokens)
    outputs = model.generate(
        inputs,
        max_length=100,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        pad_token_id=tokenizer.eos_token_id,  # Set pad_token_id
        attention_mask=attention_mask  # Set attention_mask
    )

    # Decode the generated response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# User interaction loop
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        if "weather" in user_input.lower():
            print("AI:", extract_temperature_from_context())  # Extract and display the temperature directly
        else:
            response = generate_response(user_input)
            print("AI:", response)
'''