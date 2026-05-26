# Day 3 Mini Project - Clinic KPI Checker

clinic_name = "Acutis AI Demo Clinic"

# Follow-up data
completed_followups = 84
total_followups_due = 100
target_followup_rate = 80

followup_completion_rate = completed_followups / total_followups_due * 100
met_followup_target = followup_completion_rate >= target_followup_rate

# No-show data
scheduled_visits = 50
no_show_visits = 7
acceptable_no_show_rate = 10

no_show_rate = no_show_visits / scheduled_visits * 100
no_show_rate_too_high = no_show_rate > acceptable_no_show_rate

# Workload data
total_patients = 120
patients_completed = 95
high_workload_threshold = 20

pending_patients = total_patients - patients_completed
workload_is_high = pending_patients > high_workload_threshold

# Report
print("----- Clinic KPI Report -----")
print(f"Clinic: {clinic_name}")
print(f"Follow-up completion rate: {followup_completion_rate:.1f}%")
print(f"Met follow-up target: {met_followup_target}")
print(f"No-show rate: {no_show_rate:.1f}%")
print(f"No-show rate too high: {no_show_rate_too_high}")
print(f"Pending patients: {pending_patients}")
print(f"Workload is high: {workload_is_high}")
print("-----------------------------")