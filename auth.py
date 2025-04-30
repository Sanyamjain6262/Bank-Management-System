def login():
    print("🔐 BANK LOGIN")
    attempts = 3
    while attempts > 0:
        username = input("Username: ")
        password = input("Password: ")
        if username == "admin" and password == "bank123":
            return True
        attempts -= 1
        print(f"❌ Invalid credentials. {attempts} attempts left")
    return False
