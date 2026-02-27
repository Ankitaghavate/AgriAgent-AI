def check_subsidy(profile):
    if profile["farm_size"] <= 2:
        return "Eligible for Small Farmer Subsidy Scheme"
    return "Eligible for General Agriculture Subsidy"
