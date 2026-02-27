def profile_farmer(data):
    return {
        "location": data["location"],
        "farm_size": float(data["farm_size"]),
        "crop": data["crop"],
        "income": data["income"]
    }
