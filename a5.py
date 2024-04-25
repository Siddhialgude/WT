import random

# Dictionary of responses for different admission inquiries
responses = {
    "hi": ["Hello! Welcome to our school's admission inquiry bot. How can I assist you today?",
           "Hi there! I'm here to help you with any questions you have about admissions."],
    "admission process": ["Our admission process typically involves filling out an online application form, submitting required documents, and attending an interview.",
                          "To start the admission process, you'll need to complete an application form and submit necessary documents. Would you like more details?"],
    "documents required": ["The documents required for admission usually include academic transcripts, birth certificate, ID proof, and any other relevant certificates.",
                           "You'll need to submit your academic transcripts, birth certificate, and other necessary documents for the admission process."],
    "fees": ["The admission fees vary depending on the grade level and program. You can find detailed information about fees on our school's website or by contacting the admissions office directly.",
             "For information regarding admission fees, I recommend checking our school's website or reaching out to the admissions office for assistance."],
    "application deadline": ["The application deadline for the upcoming academic year is usually in [Month]. It's important to submit your application before the deadline to ensure consideration.",
                             "Our application deadline for the upcoming academic year is typically in [Month]. Make sure to submit your application on time to avoid any delays."],
    "bye": ["Thank you for your interest in our school's admission process. If you have any more questions, feel free to ask. Goodbye!",
            "Goodbye! If you need further assistance regarding admissions, don't hesitate to reach out."],
    "default": ["I'm sorry, I didn't understand that. Could you please rephrase your question?",
                "I'm here to help with admission inquiries. Feel free to ask me anything related to admissions."]
}

# Function to generate chatbot response based on user input
def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert user input to lowercase for easier comparison
    for key in responses:
        if user_input in key:
            return random.choice(responses[key])  # Randomly select a response for the matched key
    return random.choice(responses["default"])  # If no specific response is found, return a default response

# Main function to run the chatbot
def main():
    print("Welcome to the School Admission Inquiry Chatbot!")
    print("Feel free to ask any questions about our school's admission process. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")  # Prompt user for input
        if user_input.lower() == 'bye':
            print(chatbot_response(user_input))  # Print farewell message from the chatbot
            break  # Exit the loop if user types 'bye'
        else:
            print("Bot:", chatbot_response(user_input))  # Print chatbot response to user input

# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    main()  # Run the chatbot


 