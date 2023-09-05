class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def search_by_age(self, target_age):
        matching_employees = [emp for emp in self.employees if emp.age == target_age]
        return matching_employees

    def search_by_name(self, target_name):
        matching_employees = [emp for emp in self.employees if emp.name.lower() == target_name.lower()]
        return matching_employees

    def search_by_salary(self, operator, target_salary):
        if operator == ">":
            matching_employees = [emp for emp in self.employees if emp.salary > target_salary]
        elif operator == "<":
            matching_employees = [emp for emp in self.employees if emp.salary < target_salary]
        elif operator == ">=":
            matching_employees = [emp for emp in self.employees if emp.salary >= target_salary]
        elif operator == "<=":
            matching_employees = [emp for emp in self.employees if emp.salary <= target_salary]
        else:
            matching_employees = []
        return matching_employees

def main():
    db = EmployeeDatabase()

    # Add employees to the database
    db.add_employee(Employee("161E90", "Raman", 41, 56000))
    db.add_employee(Employee("161F91", "Himadri", 38, 67500))
    db.add_employee(Employee("161F99", "Jaya", 51, 82100))
    db.add_employee(Employee("171E20", "Tejas", 30, 55000))
    db.add_employee(Employee("171G30", "Ajay", 45, 44000))

    print("Search options:")
    print("1. Age")
    print("2. Name")
    print("3. Salary (>, <, <=, >=)")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        target_age = int(input("Enter the age to search: "))
        result = db.search_by_age(target_age)
    elif choice == 2:
        target_name = input("Enter the name to search: ")
        result = db.search_by_name(target_name)
    elif choice == 3:
        operator = input("Enter the operator (> < >= <=): ")
        target_salary = int(input("Enter the salary to search: "))
        result = db.search_by_salary(operator, target_salary)
    else:
        print("Invalid choice")
        return

    if not result:
        print("No matching records found.")
    else:
        print("Matching records:")
        for emp in result:
            print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")

if __name__ == "__main__":
    main()
