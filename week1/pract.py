
users = {
    "alice": {"email": "alice@example.com"},
    "bob": {"email": "jesus.l.garcia@gmail.com"},
    "jesus": {"something": "hear me"}
}
username = "jesus"
email = users.get(username, {}).get("something", "No email found")

print(email)  # Output: jesus.l.garcia@gmail.com
