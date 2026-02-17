# Voice_command_shopping_assistant
Voice Command Shopping Assistant is an NLP-based application that allows users to manage shopping lists using natural language commands. It identifies intent, extracts items, provides smart suggestions, auto-categorizes products, and updates lists in real time using a Streamlit interface.

# 🎤 Voice NLP Shopping Assistant
A browser-based Voice Command Shopping Assistant built using NLP and Streamlit. This application allows users to manage their shopping list using natural language voice or text commands. The system interprets user intent, extracts items and quantities, provides smart suggestions, and auto-categorizes products.

---
##  Features
- Voice-based commands using browser microphone  
- Natural Language Processing (spaCy NLP)  
- Add items using conversational commands  
- Remove items from shopping list  
- Search products using keywords  
- Quantity detection (example: "add 2 apples")  
- Smart product suggestions  
- Automatic product categorization  
- Real-time interactive UI with Streamlit  

---

## Example Commands
- add milk  
- add 2 apples  
- remove bread  
- find organic apple  

---
## How It Works

The application uses NLP techniques to process natural language input. User commands are analyzed using spaCy to identify intent (add, remove, search), extract item names, and detect quantities using regex. Based on the parsed result, the application updates the shopping list dynamically.

Suggestions and product categories are stored in predefined datasets to simulate intelligent recommendations. The interface is built using Streamlit to provide a simple browser-based experience with real-time updates.

---
## Technologies Used

- Python
- Streamlit
- spaCy (NLP)
- Web Speech API (browser mic)
- Regular Expressions (regex)

---

## Project Structure
voice_shopping_assistant/
-app.py # Main Streamlit application
-nlp_utils.py # NLP parsing logic
-data.py # categories, suggestions, products
-README.md

---

##  Installation
1. Clone repository:
git clone <your_repo_link>

2. Install dependencies:
pip install streamlit spacy
python -m spacy download en_core_web_sm

3. Run application:

streamlit run app.py

---
##  Approach
The system applies rule-based NLP using spaCy to interpret user intent and extract entities from natural language commands. Streamlit session state maintains the shopping list during interaction. Browser-based voice input improves usability by enabling hands-free command execution.

---
## Future Improvements

- Machine learning-based intent classification
- Voice auto-fill input integration
- Product recommendation engine









