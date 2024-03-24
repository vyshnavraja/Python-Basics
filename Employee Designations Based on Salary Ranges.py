names = {101: 'vyshnav', 102: 'pranoy', 103: 'gautham', 104: 'joshva', 105: 'ajith'}
salaries =  {101: 75000, 102: 68000, 103: 55000, 104: 48000, 105: 60000}

#Empty dictionary
designations = {}

for emp_id in names:
    salary = salaries.get(emp_id, 0)  
    3
    if 70000 <= salary <= 80000:
        designation = 'Project Manager'
    elif 60000 <= salary < 70000:
        designation = 'Team Leader'
    elif 50000 <= salary < 60000:
        designation = 'Software Developer'
    elif 40000 <= salary < 50000:
        designation = 'Software Trainee'
    else:
        designation = 'ERROR' 
    

    designations[emp_id] = designation

print(designations)
