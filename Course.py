# Base class
class Course:
    def __init__(self, course_code, course_name, credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours

    def display_details(self):
        return f"Course Code: {self.course_code}, Course Name: {self.course_name}, Credit Hours: {self.credit_hours}"

# Subclass for core courses
class CoreCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, required_for_major):
        super().__init__(course_code, course_name, credit_hours)
        self.required_for_major = required_for_major

    def display_details(self):
        required_status = "Required" if self.required_for_major else "Optional"
        return super().display_details() + f", Required for Major: {required_status}"

# Subclass for elective courses
class ElectiveCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, elective_type):
        super().__init__(course_code, course_name, credit_hours)
        self.elective_type = elective_type

    def display_details(self):
        return super().display_details() + f", Elective Type: {self.elective_type}"

# Example usage
if __name__ == "__main__":
    core_course = CoreCourse("CS101", "Introduction to Computer Science", 3, True)
    elective_course = ElectiveCourse("ART202", "Modern Art History", 2, "liberal arts")

    print(core_course.display_details())
    print(elective_course.display_details())
