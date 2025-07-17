def control_dam(release_predicted):
    if release_predicted > 1200:
        return "Open gates to 80%"
    elif release_predicted > 1000:
        return "Open gates to 50%"
    else:
        return "Keep gates at 30%"