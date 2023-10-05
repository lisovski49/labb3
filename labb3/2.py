with open('employees.rtf', 'r') as f:
    high_salary_employees = []
    total_salary = 0
    num_employees = 0
    for line in f:
        name, salary = line.split()
        salary = float(salary)
        total_salary += salary
        num_employees += 1
        if salary > 10000:
            high_salary_employees.append(name)

    print("Сотрудники с окладом более 10 тысяч:", ', '.join(high_salary_employees))
    avg_salary = total_salary / num_employees
    print("Средняя величина дохода сотрудников:", avg_salary)