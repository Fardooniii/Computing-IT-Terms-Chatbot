import json  # to load the definitions from a JSON file
import difflib  # Help find accuraate words cuz I can't spell

# Open the JSON file where all the definitions are stored
with open('definitions.json', 'r', encoding='utf-8') as file:
    definitions = json.load(file)

print("Welcome! Ask me about computing terms. Type 'exit' to quit.")

# Theres a infinite loop until i say exit then the loop breaaaks
while True:
    user_input = input("Enter a term: ").lower().strip()  # Gets the input and makes it lowercase and remove any spaces

    if user_input == 'exit':
        print("Goodbye!")
        break  # stops the loop if the user wants to exit

    # This loop goes through each word
    for word in user_input.split():
        # Try to find a close match for the word in the definitions list
        match = difflib.get_close_matches(word, definitions.keys(), n=1, cutoff=0.75)
        
        if match:
            # If a match is found then print the word and its meaning
            print(f"{match[0].capitalize()}: {definitions[match[0]]}")
            break  # don't keep checking once a match is found

    else:
        # If no match is found at all then show this
        print("Sorry, I don't have a definition for that.")



