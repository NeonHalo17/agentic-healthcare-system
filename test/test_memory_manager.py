from memory.memory_manager import MemoryManager

memory = MemoryManager()

memory.save_patient_context(
    "session_1",
    "Rajesh Sharma"
)

print(
    memory.get_patient_context(
        "session_1"
    )
)