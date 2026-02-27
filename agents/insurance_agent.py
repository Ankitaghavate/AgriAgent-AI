def check_insurance(profile):
    if profile["crop"].lower() in ["cotton", "rice", "wheat"]:
        return "Eligible for Crop Insurance Scheme"
    return "Insurance eligibility needs manual verification"
