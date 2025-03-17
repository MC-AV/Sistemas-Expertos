#Cielo Aceves 22110390
# Base de datos inicial de respuestas
chatbot_db = {
    "hola": "¡Hola! ¿Cómo estás?",
    "como estas": "Estoy bien, gracias por preguntar. ¿Y tú?",
    "de que te gustaria hablar": "Podemos hablar de lo que quieras. ¿Tienes algún tema en mente?"
}

def chatbot():
    print("Chatbot: ¡Hola! Soy tu chatbot. Escribe 'salir' para terminar.")
    while True:
        # Entrada del usuario
        user_input = input("Tú: ").lower()
        
        # Condición para salir del chat
        if user_input == "salir":
            print("Chatbot: ¡Hasta luego!")
            break
        
        # Respuesta según la base de datos
        response = chatbot_db.get(user_input)
        
        if response:
            print(f"Chatbot: {response}")
        else:
            # Si no conoce la respuesta, pide al usuario una nueva
            print("Chatbot: No sé cómo responder eso. ¿Qué debería decir?")
            new_response = input("Escribe la respuesta que debería aprender: ")
            chatbot_db[user_input] = new_response
            print("Chatbot: ¡Gracias! He aprendido algo nuevo.")

# Iniciar el chatbot
chatbot()