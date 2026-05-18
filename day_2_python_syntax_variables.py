# Day 2 - Python Syntax and Variables
# Goal: Practice variables, strings, numbers, and simple healthcare calculations
first_name = "Camilo"
last_name = "Trujillo"
profession = "MD and Surgical Assistant"
business = "Acutis AI Smart Solutions"
goal = "Become an AI expert"

print(first_name)
print(last_name)
print(profession)
print(business)
print(goal)

full_name = first_name + " " + last_name

print("Full name:", full_name)

age = 38
month_number = 1
weekly_study_hours = 15
weeks_in_month = 4

monthly_study_hours = weekly_study_hours * weeks_in_month

print("Age:", age)
print("Month number:", month_number)
print("Weekly study hours:", weekly_study_hours)
print("Monthly study hours:", monthly_study_hours)

# Healthcare KPI Practice

total_patients = 250
completed_followups = 190
missed_followups = 40
pending_followups = 20

completion_rate = completed_followups / total_patients * 100
missed_rate = missed_followups / total_patients * 100
pending_rate = pending_followups / total_patients * 100

print("Total patients:", total_patients)
print("Completion rate:", completion_rate, "%")
print("Missed follow-up rate:", missed_rate, "%")
print("Pending follow-up rate:", pending_rate, "%")

print("Business interpretation:")
print("This type of calculation can help a clinic identify follow-up gaps.")
print("Acutis AI could turn this into a basic dashboard or automated report.")

# Checking data types

print(type(first_name))
print(type(age))
print(type(completion_rate))

# Independent Challenge

monthly_appointments = 300
completed_appointments = 240
no_show_appointments = 45
canceled_appointments = 15

completion_rate = completed_appointments / monthly_appointments * 100
no_show_rate = no_show_appointments / monthly_appointments * 100
cancellation_rate = canceled_appointments / monthly_appointments * 100

print("Completion Rate:", + completion_rate, "%")
print("No Show Rate:", + no_show_rate, "%" )
print("Cancellation Rate:", cancellation_rate, "%")

# Independent Challenge

clinic_name = "Acutis Mock Clinic"
monthly_appointments = 300
completed_appointments = 240
no_show_appointments = 45
canceled_appointments = 15

completion_rate = completed_appointments / monthly_appointments * 100
no_show_rate = no_show_appointments / monthly_appointments * 100
cancellation_rate = canceled_appointments / monthly_appointments * 100

print("Clinic:", clinic_name)
print("Completion rate:", completion_rate, "%")
print("No-show rate:", no_show_rate, "%")
print("Cancellation rate:", cancellation_rate, "%")