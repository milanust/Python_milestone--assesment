# Employee File Management System

class Employee:

    def __init__(self, employee_id, name, role, salary):
        self.employee_id = employee_id
        self.name = name
        self.role = role
        self.salary = float(salary)

    def display_details(self):
        print(
            f"{self.employee_id} - {self.name} - {self.role} - ₹{self.salary:.0f}"
        )


def add_employee():
    employees = [
        "101,Rahul,Python Developer,50000\n",
        "102,Anjali,Tester,45000\n",
        "103,John,Developer,60000\n",
        "104,Priya,Tester,48000\n",
        "105,Milan,Automation Engineer,70000\n"
    ]

    with open("employees.txt", "w") as file:
        file.writelines(employees)


def read_employees():
    employee_list = []

    try:
        with open("employees.txt", "r") as file:

            for line in file:
                data = line.strip().split(",")

                emp = Employee(
                    data[0],
                    data[1],
                    data[2],
                    data[3]
                )

                employee_list.append(emp)

    except FileNotFoundError:
        print("employees.txt file not found.")

    return employee_list


def find_highest_salary(employees):
    return max(employees, key=lambda emp: emp.salary)


def find_employees_by_role(employees):

    role_count = {}

    for emp in employees:

        if emp.role in role_count:
            role_count[emp.role] += 1
        else:
            role_count[emp.role] = 1

    return role_count


add_employee()

employees = read_employees()

print("\n===== EMPLOYEE DETAILS =====")

for emp in employees:
    emp.display_details()

print("\n===== EMPLOYEES WITH SALARY > 50000 =====")

high_salary_employees = [
    emp for emp in employees if emp.salary > 50000
]

for emp in high_salary_employees:
    print(f"{emp.name} - ₹{emp.salary:.0f}")

highest_paid = find_highest_salary(employees)

print("\n===== HIGHEST PAID EMPLOYEE =====")
print(f"{highest_paid.name} - ₹{highest_paid.salary:.0f}")

print("\n===== EMPLOYEE COUNT BY ROLE =====")

role_counts = find_employees_by_role(employees)

for role, count in role_counts.items():
    print(f"{role}: {count}")