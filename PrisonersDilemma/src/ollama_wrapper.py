import ollama
import uuid

class OllamaWrapper:
    def __init__(self):
        """Initializes the OllamaWrapper object. Uses the 'mistral' model."""
        self.model = "mistral"
        self.custom = False
        
    def chat_response(self, message: str):
        """Returns the response from Ollama given a message.
        
        Args:
            message (str): The message to send to Ollama.
        Returns:
            str: The response content.
        """
        response = ollama.chat(
            model=self.model,
            messages=[
            {
                'role': 'user', 
                'content': f'{message}'
            }],
        )
        
        return response['message']['content']
    
    def set_system_prompt(self, system_prompt: str):
        """Sets the system prompt for the Ollama model.
        
        Args:
            system_prompt (str): The system prompt to set.
        Returns:
            None
        """
        if self.custom:
            ollama.delete(self.model)
            
        self.model = 'mistral-' + str(uuid.uuid4())
        
        model_file = f'''
FROM mistral
SYSTEM {system_prompt}
'''
        
        ollama.create(model=self.model, modelfile=model_file)
        
        self.custom = True
    
    def __del__(self):
        if self.custom:
            ollama.delete(self.model)