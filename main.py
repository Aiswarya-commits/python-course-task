# main.py
from employee import Employee

if __name__ == "__main__":
    emp = Employee("Alice Johnson", 75000)
    print(f"Employee Name: {emp.get_name()}")
    print(f"Employee Salary: ${emp.get_salary()}")
