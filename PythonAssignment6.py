# Dictionary containing course numbers and room numbers
room_numbers = {
    'CS101': '3004',
    'CS102': '4501',
    'CS103': '6755',
    'NT110': '1244',
    'CM241': '1411'
}

# Dictionary containing course numbers and instructors
instructors = {
    'CS101': 'Haynes',
    'CS102': 'Alvarado',
    'CS103': 'Rich',
    'NT110': 'Burke',
    'CM241': 'Lee'
}

# Dictionary containing course numbers and meeting times
meeting_times = {
    'CS101': '8:00 a.m.',
    'CS102': '9:00 a.m.',
    'CS103': '10:00 a.m.',
    'NT110': '11:00 a.m.',
    'CM241': '1:00 p.m.'
}

# Function to get course details
def get_course_details(course_number):
    if course_number in room_numbers:
        room_number = room_numbers[course_number]
        instructor = instructors[course_number]
        meeting_time = meeting_times[course_number]
        return room_number, instructor, meeting_time
    else:
        return None, None, None

# Main function
def main():
    course_number = input("Enter a course number: ")
    room_number, instructor, meeting_time = get_course_details(course_number)
    if room_number is not None:
        print(f"Room Number: {room_number}")
        print(f"Instructor: {instructor}")
        print(f"Meeting Time: {meeting_time}")
    else:
        print("Course not found.")

if __name__ == "__main__":
    main()