# Build a chatbot that interacts with the Indian Penal Code and answers user queries.

import spacy

nlp = spacy.load("en_core_web_sm")

IPC_SECTIONS = {
    "302": "Section 302 IPC - Punishment for murder, Commits shall be punished with death, or imprisonment for life, and shall also be liable to pay fine.",
    "375": "Section 375 IPC - Rape. This section defines what constitues rape under Indian Law",
    "420": "Section 420 IPC - Cheating and dishonesty inducing delivery of property",
    "376": "Section 376 IPC - Punishment for rape. Rigorous imprisonment of not less than 10 years, which may extend to life imprionment, and a fine",
    "124a": "Section 124A IPC - Section whoever by words or signs, brings or attempts to bring hatred or contempt againt the government shall be punished"
}

# Extract IPC section
def extract_ipc_section(user_input):
    doc = nlp(user_input)

    for token in doc:
        if token.text.lower() in IPC_SECTIONS:
            return token.text.lower()

    return None


# Detect user intent
def detect_intent(user_input):
    text = user_input.lower()

    if "hello" in text or "hi" in text:
        return "greeting"

    if "section" in text or any(sec in text for sec in IPC_SECTIONS):
        return "ipc_query"

    return "general"


print("IPC Chatbot: Hello! Ask me about any section of the Indian Penal Code")
while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("IPC Chatbot. Goodbye!")
        break


    intent = detect_intent(user_input)

    if intent == "ipc_query":
        section = extract_ipc_section(user_input)
        if section:
            print(f"IPC Chatbot: {IPC_SECTIONS[section]}")
        else:
            print("IPC Chatbot. Sorry I couldn't identify the IPC section. Please specify like 'Section 302'")
        
    elif intent == "greeting":
        print("IPC Chatbot: Hello! Ask me about any IPC section")
        
    else:
        print("IPC Chatbot: I can help you with information about the Penal Code. Try asking about a section like 'What is section 420?'")
