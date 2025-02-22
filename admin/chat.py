from transformers import pipeline, GPT2LMHeadModel, GPT2Tokenizer
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

# Context about Saudi Arabia
context_saudi_arabia = """
Saudi Arabia, officially known as the Kingdom of Saudi Arabia (KSA), is a country located on the Arabian Peninsula. 
It is bordered by Jordan, Iraq, Kuwait, Bahrain, Qatar, the UAE, Oman, and Yemen. Saudi Arabia is known for its vast deserts and rich cultural heritage. 
The country is also home to Islam's two holiest cities, Mecca and Medina.
"""

# Context about Riyadh
context_riyadh = """
Riyadh is the capital city of Saudi Arabia and the largest city in the country. It is located in the central region of the Arabian Peninsula. 
Riyadh is known for its modern architecture, shopping malls, and vibrant cultural life. The city has been undergoing rapid development in recent years, 
with new business districts, residential areas, and international hotels emerging. Riyadh is also home to many government offices and institutions.
"""

# Context about time and weather
context_time_weather = """
Saudi Arabia has a desert climate with hot summers and mild winters. The country experiences high temperatures throughout the year, 
especially in the summer months of June to August. Riyadh, in particular, experiences extremely hot temperatures in summer, often exceeding 40°C (104°F). 
Rainfall is scarce, and the country faces occasional sandstorms. Winters in Riyadh are much milder, with temperatures dropping to around 15°C (59°F) at night.
"""

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
