def login():
    print("BANK LOGIN")
    attempts = 3
    
    with open("password_username.txt", "r") as f:
        valid_credentials = {}
        for line in f:
            if ":" in line and not line.startswith("#"):
                username, password = line.strip().split(":")
                valid_credentials[username] = password

    while attempts > 0:
        username = input("Username: ")
        password = input("Password: ")
        
        if username in valid_credentials and valid_credentials[username] == password:
            return True
        attempts -= 1
        print(f"Invalid credentials. {attempts} attempts left")
    
    return False
