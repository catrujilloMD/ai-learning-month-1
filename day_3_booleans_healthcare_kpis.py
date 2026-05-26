# Day 3 - Booleans and Healthcare KPI Logic
# Wednesday, May 20, 2026
# Goal: Practice booleans, comparisons, and simple healthcare KPI checks.

# Basic boolean values

is_patient_active = True
is_patient_discharged = False

print(is_patient_active)
print(is_patient_discharged)

print(type(is_patient_active))
print(type(is_patient_discharged))

# Comparison operators

patients_scheduled = 40
patients_seen = 35

print(patients_seen == patients_scheduled)
print(patients_seen != patients_scheduled)
print(patients_seen < patients_scheduled)
print(patients_seen <= patients_scheduled)

completed_followups = 84
total_followups_due = 100

followup_completion_rate = completed_followups / total_followups_due * 100

print("Follow-up completion rate:", followup_completion_rate)

target_followup_rate = 80

met_followup_target = followup_completion_rate >= target_followup_rate

print("Met follow-up target:", met_followup_target)

scheduled_visits = 50
no_show_visits = 7

no_show_rate = no_show_visits / scheduled_visits * 100

print("No-show rate:", no_show_rate)
acceptable_no_show_rate = 10

no_show_rate_too_high = no_show_rate > acceptable_no_show_rate

print("No-show rate too high:", no_show_rate_too_high)

# Example 3 Pending workload
total_patients = 120
patients_completed = 95

pending_patients = total_patients - patients_completed

print("Pending patients:", pending_patients)

high_workload_threshold = 20

workload_is_high = pending_patients > high_workload_threshold

print("Workload is high:", workload_is_high)

# Block 5 Add basic formating
clinic_name = "Acutis AI Demo Clinic"

completed_followups = 84
total_followups_due = 100
followup_completion_rate = int(completed_followups / total_followups_due * 100)

print("Clinic:", clinic_name)
print("Follow-up completion rate:", followup_completion_rate, "%")

print(f"Clinic: {clinic_name}")
print(f"Follow-up completion rate: {followup_completion_rate}%")
print(f"Follow-up completion rate: {followup_completion_rate:.1f}%")

# Final KPI
clinic_name = "Acutis AI Demo Clinic"

scheduled_visits = 50
no_show_visits = 7
no_show_rate = no_show_visits / scheduled_visits * 100

completed_followups = 84
total_followups_due = 100
followup_completion_rate = completed_followups / total_followups_due * 100

total_patients = 120
patients_completed = 95
pending_patients = total_patients - patients_completed

print(f"Clinic: {clinic_name}")
print(f"No-show rate: {no_show_rate:.1f}%")
print(f"Follow-up completion rate: {followup_completion_rate:.1f}%")
print(f"Pending patients: {pending_patients}")