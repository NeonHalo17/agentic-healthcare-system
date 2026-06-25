import json
import os

# Define Memory Manager to save the contextual knowledge from conversation history 
class MemoryManager:
    # Initilization function
    def __init__(self):
        # Load conversation history
        if os.path.exists("memory.json"):
            with open("memory/memory.json", "r") as f:
                self.memory = json.load(f)
        else:
            self.memory = {}
            
    # Helper function to save memory      
    def _save_memory(self):
        with open("memory/memory.json", "w") as f:
            json.dump(self.memory, f, indent=4)

    # Create new session memory
    def create_session(self,session_id):
        if session_id not in self.memory:
            self.memory[session_id] = {
                "patient_name": None,
                "history": []
            }    
            
    # Save interaction messages
    def save_interaction(self,session_id,query,response):
        # Create session 
        self.create_session(session_id)
        # Save the query and llm response in the memory
        self.memory[session_id]["history"].append(
            {
                "query": query,
                "response": response
            }
        )
        # Save conversation history
        self._save_memory() 
    
    # Retreive conversation
    def get_conversation_history(self,session_id):
        # Create session
        self.create_session(session_id)
        return self.memory[session_id]["history"]

    # Save patient_name if found in session
    def save_patient_context(self,session_id,patient_name):
        # Create session  
        self.create_session(session_id)
        # Save patient_name
        self.memory[session_id]["patient_name"] = patient_name
        # Save conversation history
        self._save_memory()
    
    # Get the saved patient context from memory
    def get_patient_context(self,session_id):
        # Create session 
        self.create_session(session_id)
        # Find particular memory by patient_name and return it
        return self.memory[session_id].get("patient_name")