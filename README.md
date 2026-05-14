# Mental Health Support Chatbot (Fine-Tuned LLM)

## Project Overview

The Mental Health Support Chatbot is an AI powered conversational agent designed to provide empathetic and supportive responses for users experiencing stress, anxiety, and emotional wellness concerns. This project demonstrates the application of fine-tuned language models for mental health support, creating a safe and accessible platform for emotional support conversations.

## Model Development

### Base Model Used
- **DistilGPT2** (from Hugging Face Transformers)
  - Lightweight and efficient version of GPT-2
  - Ideal for fine tuning on specific tasks
  - Provides strong foundation for conversational AI

### Dataset
- **EmpatheticDialogues** (Facebook AI)
  - Contains human to human emotional conversations
  - Dataset focusing on empathetic responses
  - Includes various emotional scenarios and supportive dialogues
  - Perfect for training mental health support systems

### Data Processing
- **Conversation Formatting**: Converted raw dialogues into structured input response pairs
- **Template Structure**: 
  ```
  User: [emotional expression]
  Bot: [empathetic response]
  ```
- **Cleaning**: Removed irrelevant content and standardized formatting
- **Splitting**: Organized into training and validation sets

### Tokenization
- **AutoTokenizer**: Used Hugging Face's tokenizer for DistilGPT2
- **Text Processing**: Converted human-readable text into numerical tokens
- **Vocabulary Handling**: Managed special tokens and padding
- **Sequence Length**: Optimized for model's input requirements

### Training
- **Framework**: Hugging Face Trainer API
- **Fine-Tuning**: Adapted pre-trained DistilGPT2 on empathetic dialogue data
- **Objective**: Causal Language Modeling (predicting next tokens)
- **Hyperparameters**: 
  - Learning rate: 2e-5
  - Batch size: 8
  - Epochs: 3
  - Warmup steps: 500

### Training Results
- **Loss Reduction**: Decreased from ~1.3 to ~0.87
- **Convergence**: Model showed steady improvement over training epochs
- **Validation Performance**: Maintained consistent performance on held-out data
- **Response Quality**: Learned to generate contextually appropriate, empathetic replies

### Model Behavior
- **Emotional Understanding**: Recognizes emotional cues in user input
- **Empathetic Responses**: Generates supportive and caring replies
- **Context Awareness**: Maintains conversation flow and relevance
- **Safety**: Produces appropriate responses for mental health contexts

## Web Application Development

### Backend Development
- **Flask Framework**: Python-based web server
- **API Endpoint**: `/chat` POST endpoint for message processing
- **Model Integration**: Seamless connection between web interface and AI model
- **Error Handling**: Robust fallback mechanisms for model loading issues
- **Performance**: Optimized inference with `torch.no_grad()`

### Frontend Development
- **HTML Structure**: Semantic markup for chat interface
- **CSS Styling**: Modern dark theme with glassmorphism effects
- **JavaScript Logic**: Real-time message handling and API communication
- **User Experience**: Smooth animations and loading indicators
- **Responsive Design**: Works across desktop and mobile devices

### System Integration
1. **User Input**: Frontend captures user messages
2. **API Request**: Sends data to Flask backend
3. **Model Processing**: Tokenizes input and generates response
4. **Response Delivery**: Returns empathetic reply to frontend
5. **Display Updates**: Shows response in chat interface

## Tech Stack

### Backend Technologies
- **Python 3.11**: Core programming language
- **Flask 3.0.0**: Web framework for API development
- **Hugging Face Transformers 4.35.0**: Model loading and inference
- **PyTorch 2.1.0**: Deep learning framework
- **Safetensors 0.4.1**: Safe model serialization

### Frontend Technologies
- **HTML5**: Semantic markup structure
- **CSS3**: Modern styling with animations
- **JavaScript**: Client-side interactivity
- **Fetch API**: Asynchronous HTTP requests

### Model & Processing
- **DistilGPT2**: Base language model
- **AutoTokenizer**: Text tokenization
- **Fine-tuned Weights**: Custom model parameters

## How to Run the Project

### Prerequisites
- Python 3.11 or higher
- Git (for cloning repository)

### Installation Steps

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the Application**
   ```bash
   python app.py
   ```

3. **Access the Chatbot**
   - Open web browser
   - Navigate to `http://localhost:5000`
   - Start chatting with the AI assistant

### Troubleshooting
- If tokenizer loading fails, the app automatically falls back to distilgpt2
- Ensure all model files are present in `model/task_5_model/` directory
- Check Python version compatibility with requirements

## Features

### Core Functionality
- **Empathetic Responses**: AI generates supportive and caring replies
- **Real-time Chat**: Instant response generation and display
- **Fine-tuned Model**: Specialized for mental health conversations
- **Lightweight Deployment**: Efficient resource usage

### User Experience
- **Modern Interface**: Clean and simple chatbot design
- **Smooth Animations**: Professional message
- **Mobile Responsive**: Works on all device sizes
- **Error Handling**: Graceful fallbacks and user feedback

### Technical Features
- **Local Processing**: No external API dependencies
- **Fast Inference**: Optimized model loading and generation
- **Scalable Architecture**: Easy to extend and modify
- **Privacy-Focused**: All processing happens locally

## Future Improvements

### Technical Enhancements
- **Advanced UI Framework**: Migration to Streamlit or React for better interactivity
- **Emotion Detection**: Integration of sentiment analysis for better response matching
- **Conversation Memory**: Multi turn context awareness and personalization
- **Voice Interface**: Speech to text and text to speech capabilities

### Model Improvements
- **Larger Dataset**: Training on more diverse mental health conversations
- **Advanced Fine-tuning**: Techniques like LoRA for better adaptation
- **Safety Mechanisms**: Enhanced content filtering and responsible AI practices
- **Evaluation Metrics**: Comprehensive assessment of response quality

### Deployment Options
- **Cloud Hosting**: AWS, Google Cloud, or Azure deployment
- **Containerization**: Docker setup for easy deployment
- **API Service**: Convert to microservice architecture
- **Mobile App**: Native iOS and Android applications

## Author

**[Haris Hussain]**
- AI/ML Intern
- Specialization: Natural Language Processing
- Focus: Conversational AI and Mental Health Applications

---

*This project demonstrates the practical application of fine-tuned language models for socially beneficial purposes, prioritizing user privacy and emotional well being.*
