import re

def audit_wifi_password(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters.")

    common = ["password", "12345678", "qwerty", "admin", "wifi123"]
    if password.lower() in common:
        feedback.append("This is a very common password.")
        score = max(0, score - 3)

    if score >= 6:
        strength = "Very Strong"
    elif score >= 4:
        strength = "Strong"
    elif score >= 2:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback


if __name__ == "__main__":
    pwd = input("Enter your Wi-Fi password to audit: ")
    strength, tips = audit_wifi_password(pwd)

    print(f"\nStrength: {strength}")

    if tips:
        print("\nSuggestions:")
        for tip in tips:
            print(f"- {tip}")
    else:
        print("Excellent! Your password follows good security practices.")
