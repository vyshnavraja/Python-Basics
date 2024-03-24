lst=[1,2,6,3,5,4,4]
target =8
for i in range(0,len(lst)):
 for j in range(i+1,(lst)):
  if(lst[i]+lst[j]==target):
   print('{},{}]'.format(lst[i],lst[j]))



   # Create dictionaries with employee ID and name, and employee ID and salary
employee_names = {101: 'John', 102: 'Alice', 103: 'Bob', 104: 'Eve', 105: 'Charlie'}
employee_salaries = {101: 75000, 102: 68000, 103: 55000, 104: 48000, 105: 60000}

# Initialize an empty dictionary to store employee designations
employee_designations = {}

# Iterate through the employee IDs
for emp_id in employee_names:
    salary = employee_salaries.get(emp_id, 0)  # Get the salary for the current employee ID
    
    # Determine the designation based on the salary range
    if 70000 <= salary <= 80000:
        designation = 'Project Manager'
    elif 60000 <= salary < 70000:
        designation = 'Team Leader'
    elif 50000 <= salary < 60000:
        designation = 'Software Developer'
    elif 40000 <= salary < 50000:
        designation = 'Software Trainee'
    else:
        designation = 'Unknown'  # Handle cases where salary is outside the specified ranges
    
    # Add the employee ID and designation to the result dictionary
    employee_designations[emp_id] = designation

# Display the result dictionary
print(employee_designations)
