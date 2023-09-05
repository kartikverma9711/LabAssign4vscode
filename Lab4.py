class Employee:
    def _init_(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def _init_(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def search_by_age(self, target_age):
        result = [emp for emp in self.employees if emp.age == target_age]
        return result

    def search_by_name(self, target_name):
        result = [emp for emp in self.employees if emp.name == target_name]
        return result

    def search_by_salary(self, target_salary, operator):
        if operator == ">":
            result = [emp for emp in self.employees if emp.salary > target_salary]
        elif operator == "<":
            result = [emp for emp in self.employees if emp.salary < target_salary]
        elif operator == ">=":
            result = [emp for emp in self.employees if emp.salary >= target_salary]
        elif operator == "<=":
            result = [emp for emp in self.employees if emp.salary <= target_salary]
        else:
            result = []

        return result

if __name__ == "_main_":
    emp_table = EmployeeTable()

    # Adding employee data to the table
    emp_table.add_employee(Employee("161E90", "Raman", 41, 56000))
    emp_table.add_employee(Employee("161F91", "Himadri", 38, 67500))
    emp_table.add_employee(Employee("161F99", "Jaya", 51, 82100))
    emp_table.add_employee(Employee("171E20", "Tejas", 30, 55000))
    emp_table.add_employee(Employee("171G30", "Ajay", 45, 44000))

    while True:
        print("Search Options:")
        print("1. Search by Age")
        print("2. Search by Name")
        print("3. Search by Salary")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            target_age = int(input("Enter the age to search: "))
            result = emp_table.search_by_age(target_age)
        elif choice == "2":
            target_name = input("Enter the name to search: ")
            result = emp_table.search_by_name(target_name)
        elif choice == "3":
            target_salary = float(input("Enter the salary to search: "))
            operator = input("Enter the operator (<, >, <=, >=): ")
            result = emp_table.search_by_salary(target_salary, operator)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please select a valid option.")
            continue

        if not result:
            print("No matching records found.")
        else:
            print("Matching records:")
            for emp in result:
                print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")