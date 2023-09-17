input_email = str(input("Enter an email address / website address: "))

def get_domain(input_email):
    domain_name_with_period= input_email.split("@")
    domain_name = domain_name_with_period[1].split(".")[0]
    print(domain_name)


get_domain(input_email)
