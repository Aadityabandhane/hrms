def custom_authenticate(email, password):
    email = email.strip()  # Remove any accidental spaces
    emp_user = Employe_User.objects.filter(email=email).first()
    print(f"User found: {emp_user}")  # Confirm if user is retrieved

    if not emp_user:
        print("❌ No user found with this email")
        return None  # User doesn't exist

    if not check_password(password, emp_user.password):
        print("❌ Password mismatch")
        return None  # Password incorrect

    return emp_user  # Return authenticated user
  # No matching user found