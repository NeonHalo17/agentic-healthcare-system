from agents.healthcare_agent import (HealthcareAgent)

agent = HealthcareAgent()

queries = [

    # "Book a nephrologist appointment for Rajesh Sharma",

    "What is David Thompson's medication?",

    # "Update Rajesh Sharma record with fatigue and nausea",

    # "Show Rajesh Sharma's medical history"
]

for query in queries:

    plan = agent.run(query, "David Thompson")

    print("\nQUERY:")
    print(query)

    print("\nPLAN:")
    print(plan)

