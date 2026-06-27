from agents.healthcare_agent import HealthcareAgent

# Create one shared healthcareAgent for every instance 
agent = HealthcareAgent()

def get_agent():
    return agent