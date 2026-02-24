# Password Strength Checker
# Created by Kojo

import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Minimum 8 characters required.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    return score, feedback


while True:
    user_password = input("\nEnter a password to test (or type 'exit'): ")

    if user_password.lower() == "exit":
        break

    score, feedback = check_password_strength(user_password)

    if score == 5:
        print("✅ Strong Password")
    elif score >= 3:
        print("⚠ Moderate Password")
    else:
        print("❌ Weak Password")

    for item in feedback:
        print("-", item)
