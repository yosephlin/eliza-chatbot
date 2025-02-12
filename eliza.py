"""
Course: CMSC437

Program: Eliza - Psychotherapist Chatbot

Description:
This program simulates a rogerian psychotherapist named Eliza. It creates conversation with the user
by recognizing keywords and transforming specific statements into questions.
It also handles unclear inputs with a fallback response and uses the user's name.

Instructions:
1. Run the program: `python eliza.py`
2. Enter responses when prompted.
3. The program ends when user types 'exit', 'quit', or 'bye'.

Example:
-> [eliza] Hi, I'm a psychotherapist. What is your name?
=> [user] My name is Bridget.
-> [eliza] Hi Bridget. How can I help you today?
=> [Bridget] I want to rule the world.
-> [eliza] Bridget, why do you want to rule the world?
=> [Bridget] I don't know, I think I crave power.
-> [eliza] Why don't you tell me more about your cravings?

Algorithm:
1. Greet user and ask for their name.
2. Engage in conversation, spotting key words with regular expressions.
3. Transform specific user statements into questions.
4. Handle unknown inputs with a fallback response.
5. Continue until the user types 'exit', 'quit', or 'bye'.
"""

import re

#Checks for particular keywords and generate questions.
def check_keywords(statement: str, name: str) -> str:
    keywords = {
        "mother": f"Tell me more about your mother, {name}.",
        "mom": f"Tell me more about your mother, {name}.",
        "father": f"Tell me more about your father, {name}.",
        "dad": f"Tell me more about your father, {name}.",
        "love": f"{name}, love is a complex emotion. Can you elaborate?",
        "hate": "Hate is a strong word. What makes you feel this way?",
        "sad": "What comes to mind when you think of the word 'sadness'?",
        "angry": "What do you think might be at the root of this?",
        "happy": "Can you tell me more about what this feeling means to you?",
        "crave": "Why don't you tell me more about your cravings?",
        "stress": "Can you describe what it feels like when you are feeling particularly stressed?"
    }
    for word, response in keywords.items():
        if re.search(rf"{word}", statement, re.IGNORECASE):
            return response
    return None

#fallback response to handle unrecognized inputs.
def fallback_response() -> str:
    return "I didn't quite understand that. Can you rephrase it?"

#transforms certain user statements into questions
def statement_to_question(statement: str, name: str) -> str:
    patterns = [
        (r"I want to (.+)", "Why do you want to \a?"),
        (r"I feel (.+)", "Why do you feel \a?"),
        (r"I am (.+)", "How long have you been \a?"),
        (r"I think (.+)", "Why do you think \a?"),
        (r"I have (.+)", f"{name}, why do you have \a?"),
        (r"I dislike (.+)", "Why do you dislike \a?"),
        (r"I crave (.+)", f"{name}, Why do you crave \a?"),
        (r"I desire (.+)", "Why do you desire \a?"),
    ]
    for pattern, response in patterns:
        match = re.match(pattern, statement, re.IGNORECASE)
        if match:
            return response.replace("\a", match.group(1))
    return None

def eliza(): #Main process: chatbot gives an introduction and asks for name, handles input, and checks for keywords.
    print("-> [eliza] Hi, I'm a psychotherapist. What is your name?")
    name = input("=> [user] ").strip()
    name = re.sub(r"^(my name is|I'm) ", "", name, flags=re.IGNORECASE).strip()
    
    print(f"-> [eliza] Hi {name}. How can I help you today?")
    
    while True:
        user_input = input(f"=> [{name}] ").strip()
        if user_input.lower() in {"exit", "quit", "bye"}:
            print(f"-> [eliza] Goodbye, {name}!")
            break
        
        response = statement_to_question(user_input, name) or check_keywords(user_input, name) or fallback_response()
        print(f"-> [eliza] {response}")

if __name__ == "__main__":
    eliza()
