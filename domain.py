def replace_domain(email, old_domain, new_domain):
    if '@' + old_domain in email:
        index = email.index("@"+old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email


email_1 = replace_domain('abhie@gmail.com', 'gmail.com', 'email.com')
print(email_1)