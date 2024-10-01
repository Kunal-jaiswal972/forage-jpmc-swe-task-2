import os

def main():
    # Hardcoded sensitive information (Vulnerable)
    api_key = "abc123-def456-ghi789-jkl012"  # Exposed API Key
    db_password = "password123"  # Exposed Database Password

    # Simulate logging sensitive information
    print("Starting application...")
    print(f"API Key: {api_key}")  # Vulnerable: printing sensitive information
    print(f"Database Password: {db_password}")  # Vulnerable: printing sensitive information

    # Simulated application logic
    if os.environ.get('DEBUG', 'False') == 'True':
        print("Debugging mode is on")
        print(f"Debug API Key: {api_key}")  # Exposed in debug mode

    # Normal application flow
    print("Application is running...")

if __name__ == "__main__":
    main()
