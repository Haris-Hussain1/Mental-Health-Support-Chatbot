from flask import Flask, render_template, request, jsonify
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

app = Flask(__name__)

# model from local path
model_path = r"model\task_5_model"

try:
    tokenizer = AutoTokenizer.from_pretrained(model_path)
except Exception as e:
    print(f"Failed to load local tokenizer: {e}")
    print("Falling back to distilgpt2 tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained("distilgpt2")

# Load model from local directory with local_files_only=True
try:
    model = AutoModelForCausalLM.from_pretrained(model_path, local_files_only=True)
except Exception as e:
    print(f"Failed to load local model: {e}")
    raise

# Set model to evaluation mode
model.eval()

# Set pad token if not set
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400
    
    # Tokenize input
    inputs = tokenizer(user_message, return_tensors='pt', padding=True, truncation=True)
    
    # Generate response with torch.no_grad() for efficiency
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=100,
            do_sample=True,
            temperature=0.7,
            pad_token_id=tokenizer.eos_token_id
        )
    
    # Decode the generated response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Remove the input message from the response if it's included
    if response.startswith(user_message):
        response = response[len(user_message):].strip()
    
    # Remove "Bot:" prefix if present (case-insensitive)
    if response.lower().startswith("bot:"):
        response = response[4:].strip()
    
    # Remove any remaining "Bot:" text in the middle of response
    response = response.replace("Bot:", "").strip()
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
