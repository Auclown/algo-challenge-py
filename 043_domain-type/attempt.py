def domain_type(domains):
    result = []
    domain_types = {"org": "organization", "com": "commercial",
                    "net": "network", "info": "information"}

    for i in range(len(domains)):
        result.append(domains[i].split(".")[-1])

    for j in range(len(result)):
        result[j] = domain_types[result[j]]

    return result


# Test
print(domain_type(["en.wiki.org", "codefights.com", "happy.net", "code.info"]))
# ["organization", "commercial", "network", "information"]
