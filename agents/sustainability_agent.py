def calculate_score(profile):

    score = 50

    if profile.get("farming_type") == "organic":
        score += 20

    if profile.get("crop_type") in ["millets", "pulses"]:
        score += 10

    if profile.get("income_level") == "low":
        score += 5

    return min(score, 100)
