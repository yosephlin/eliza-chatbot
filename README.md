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
