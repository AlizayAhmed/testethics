"""
Privacy-sensitive test data for GitHub analyzer.
All data below is fictional.
"""

user_data = {
    "name": "Sara Mahmood",
    "email": "sara.mahmood92@examplemail.com",
    "phone": "+92 331 555 9821",
    "cnic": "42101-9876543-1",
    "bank_account": "HBL – 1283-903123-01"
}

def show_user_info():
    for key, value in user_data.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    show_user_info()
