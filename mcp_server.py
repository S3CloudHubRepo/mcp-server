from student_model import Student
import json

student_db = {
    "101": Student("101", "Amit", "Computer"),
    "102": Student("102", "Priya", "IT"),
    "103": Student("103", "Raj", "Electronics")
}

def handle_request(command, args):
    if command == "GET":
        roll_no = args[0]
        student = student_db.get(roll_no)
        if student:
            return json.dumps(student.to_dict())
        else:
            return json.dumps({"error": "Student not found"})

    elif command == "LIST":
        return json.dumps([student.to_dict() for student in student_db.values()])
    
    elif command == "ADD":
        roll_no, name, dept = args
        student_db[roll_no] = Student(roll_no, name, dept)
        return json.dumps({"status": "Student added"})

    else:
        return json.dumps({"error": "Invalid command"})
if __name__ == "__main__":
    print("Simple MCP Server Running...")
    while True:
        try:
            input_str = input("MCP> ")  # Example: GET 101
            if input_str.lower() in ["exit", "quit"]:
                break

            parts = input_str.strip().split()
            command = parts[0].upper()
            args = parts[1:]

            response = handle_request(command, args)
            print("Response:", response)
        except Exception as e:
            print("Error:", str(e))
