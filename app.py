import streamlit as st
from streamlit.components.v1 import html
from nlp_utils import parse_command
from data import categories, suggestions, products



st.title("🎤 Voice NLP Shopping Assistant")


if "shopping_list" not in st.session_state:
    st.session_state.shopping_list = []



voice_html = """
<button onclick="startRecognition()">🎤 Speak</button>

<p id="output"></p>

<script>
function startRecognition() {
    var recognition = new webkitSpeechRecognition();
    recognition.lang = "en-US";
    recognition.start();

    recognition.onresult = function(event) {
        var text = event.results[0][0].transcript;
        document.getElementById("output").innerText = text;

        window.parent.postMessage({
            type: "streamlit:setComponentValue",
            value: text
        }, "*");
    };
}
</script>
"""

html(voice_html, height=120)



spoken_text = st.text_input(
    " Speak or type your command (Use mic button or Win+H)",
    placeholder="Add milk, remove apple, find organic apple"
)



if spoken_text:

    st.markdown(f"###  You said: {spoken_text}")

    intent, item, quantity = parse_command(spoken_text)

    st.write("Intent:", intent)
    st.write("Item:", item)
    st.write("Quantity:", quantity)

     
    if intent == "add" and item:
        for _ in range(quantity):
            st.session_state.shopping_list.append(item)


    elif intent == "remove" and item:
        if item in st.session_state.shopping_list:
            st.session_state.shopping_list.remove(item)

    
    elif intent == "search" and item:

        results = [p for p in products if item in p["name"]]

        st.markdown("###  Search Results")

        if results:
            for r in results:
                st.markdown(f"- {r['name']} (₹{r['price']})")
        else:
            st.write("No matching product found.")

    
    if item in suggestions:
        st.markdown(
            "<h2> You should buy these too ---></h2>",
            unsafe_allow_html=True
        )

        for s in suggestions[item]:
            st.markdown(f"- {s}")

    
    if item in categories:
        st.markdown(f"**Category:** {categories[item]}")



st.markdown("# 🧾 Shopping List")
st.markdown("### **Your shopping list --->**")

if st.session_state.shopping_list:
    for list_item in st.session_state.shopping_list:
        st.markdown(f"- {list_item}")
else:
    st.write("No items added yet.")





