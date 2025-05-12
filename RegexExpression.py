import re

emails = [

 "test@example.com",

 "invalid.email",

 "another_test@domain.co.uk",

 "not_valid@.com",

 "user+123@company.net"]

email_data = {}

def validate_email_format(user_email):
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    result = re.match(pattern, user_email)

    if result:
        return "email match"
    else:
        return "email not match"

for email in emails:
    response = validate_email_format(email)
    email_data[email] = response

print(email_data)
