# This code prints a right-angled triangle pattern using asterisks.
"""for i in range(1,5):
    for j in range(i):
        print("*", end="")
    print()"""

# """for i in range(1, 6):
#     for j in range(6 - i):
#         print(" ", end="")
#     for k in range(i):
#         print("*", end="")
#     print()"""

"""for i in range(1, 6):
    for space in range(6 - i):
        print(" ", end="")
    for star in range(2 * i - 1):
        print("*", end="")
    print()"""

# """def factorial(n):
#     if n<0 :
#         return "Invalid input"
#     elif n==0 or n==1:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(5))"""

#palindrome checker function
'''def is_palindrome(text):
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    reversed_text = cleaned_text[::-1]

    if cleaned_text == reversed_text:
        return True
    else:
        return False
    
print(f"'Madam' is a palindrome: {is_palindrome('Madam')}")
print(f"'A man a plan a canal Panama' is a palindrome: {is_palindrome('A man a plan a canal Panama')}")
print(f"'Python' is a palindrome: {is_palindrome('Python')}")'''

# '''filename = "my_data.txt"
# with open(filename, 'w') as file:
#     file.write("This is the first line.\n")
#     file.write("This overwrites everything else.\n")
# print(f"Data written to {filename} using 'w' mode.")
# with open(filename, 'a') as file:
#     file.write("This line is appended now.\n")
# print(f"New data appended to {filename} using 'a' mode.")
# filename = "my_data.txt"
# with open(filename, 'r') as file:
#     all_content = file.read()
#     print("\n--- Full Content Read (.read()) ---")
#     print(all_content)
# print("\n--- Reading Line by Line ---")
# line_number = 1
# with open(filename, 'r') as file:
#     for line in file:
#         print(f"Line {line_number}: {line.strip()}")
#         line_number += 1'''


'''def safe_divide(a,b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Invalid input type. Please provide numbers."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
    else:
        return result
print(safe_divide(10, 2))  # Should print 5.0
print(safe_divide(10, 0))  # Should handle division by zero'''

# class student:
#     school_name = "Tech Academy"
    
#     def __init__(self, name, student_id, major):
#         self.name = name
#         self.student_id = student_id
#         self.major = major
#         self.courses = []
        
#     def get_info(self):
#         return(f"Student Name : {self.name}\n"
#                f"Student Id : {self.student_id}\n"
#                f"Major: {self.major}\n"
#                f"Enrolled at: {student.school_name}")
               
#     def enroll(self, course_name):
#         if course_name not in self.courses:
#             self.courses.append(course_name)
#             print(f"{self.name} is now enrolled in {course_name}.")
#         else:
#             print(f"{self.name} is already in {course_name}.")

# # Test the class
# s1 = student("neeti", "50", "Computer Science")
# print(s1.get_info())
# s1.enroll("Math")
# s1.enroll("Math")

# # Create two instances (objects) of the Student class
# student1 = student("Alice Smith", "S1001", "Computer Science")
# student2 = student("Bob Johnson", "S1002", "Data Science")

# # --- Using Methods ---
# # Enroll student1 in courses
# student1.enroll("Python Fundamentals")
# student1.enroll("Calculus I")

# # Enroll student2 in a course
# student2.enroll("Statistics")

# # --- Accessing Attributes and Calling Info Method ---
# print("\n" + "="*30)
# print("ALICE'S DETAILS:")
# print(student1.get_info())

# # Accessing the Class Variable
# print(f"Student 1's School: {student1.school_name}")


