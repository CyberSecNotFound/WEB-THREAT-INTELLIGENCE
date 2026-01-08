def verdict(score):
    if score < 30:
        return "AMAN", "GREEN"
    elif score < 70:
        return "MENCURIGAKAN", "YELLOW"
    else:
        return "BERBAHAYA", "RED"
