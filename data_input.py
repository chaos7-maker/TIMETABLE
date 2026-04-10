def collect_user_data():
    print("--- System Setup ---")
    num_subs = int(input("How many subjects? "))
    
    subject_teacher = {}
    subject_periods = {}
    
    for _ in range(num_subs):
        sub = input("Subject Name: ")
        teacher = input(f"Teacher for {sub}: ")
        count = int(input(f"Periods per week for {sub}: "))
        
        subject_teacher[sub] = teacher
        subject_periods[sub] = count
        
    classes = input("Enter classes (comma separated, e.g., CSE-A,CSE-B): ").split(',')
    
    return subject_teacher, subject_periods, [c.strip() for c in classes]