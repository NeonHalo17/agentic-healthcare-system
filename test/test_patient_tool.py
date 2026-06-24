from tools.patient_tool import PatientTool

# Initialize object of patient tool
tool = PatientTool()

# Call methods to check if it working or not
print(tool.get_patient("P001"))

print(tool.get_history("P001"))

print(tool.get_patient_by_name("Neha Kapoor"))

print(tool.update_notes("P005", "Scheduled for cardiology review."))