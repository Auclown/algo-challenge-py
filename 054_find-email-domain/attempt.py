def find_email_domain(email):
    temp = email.split("@")

    return temp[-1]


print(find_email_domain("prettyandsimple@example.com"))
print(find_email_domain("<>[]:,;@\"!#\$%&\*+-/=?^\_{}| ~.a\"@example.org"))
