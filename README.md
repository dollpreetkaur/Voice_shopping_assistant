# Voice_command_shopping_assistant
Voice Command Shopping Assistant is an NLP-based application that allows users to manage shopping lists using natural language commands. It identifies intent, extracts items, provides smart suggestions, auto-categorizes products, and updates lists in real time using a Streamlit interface.
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
git clone [<your_repo_link>](https://github.com/dollpreetkaur/Voice_shopping_assistant)

2. Install dependencies:
pip install streamlit spacy
python -m spacy download en_core_web_sm

3. Run application:
streamlit run app.py

## 🚀 Deployment

Users can deploy this application using Streamlit Cloud or Render.

---

### ⭐ Deploy on Streamlit Cloud (Recommended)

1. Fork or clone this repository to your GitHub account.
2. Go to https://share.streamlit.io
3. Click "New App".
4. Select your repository.
5. Choose branch: main
6. Set file path to: app.py
7. Click Deploy.

Make sure requirements.txt is present so dependencies install automatically.

---

###  Deploy on Render
1. Push project to GitHub.
2. Go to https://render.com and create a new Web Service.
3. Connect your GitHub repository.
4. Set Environment to Python.
Build Command:pip install -r requirements.txt
Start Command:streamlit run app.py --server.port=$PORT --server.address=0.0.0.0

5. Click Deploy.

---
##  Approach
The system applies rule-based NLP using spaCy to interpret user intent and extract entities from natural language commands. Streamlit session state maintains the shopping list during interaction. Browser-based voice input improves usability by enabling hands-free command execution.
---
## Future Improvements

- Machine learning-based intent classification
- Voice auto-fill input integration
- Product recommendation engine









