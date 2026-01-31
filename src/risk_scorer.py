def calculate_risk(missing_ppe, unsafe_count):
    score = 0
    if not missing_ppe.get('helmet', True):
        score += 50
    if not missing_ppe.get('vest', True):
        score += 50
    score += unsafe_count * 10
    return min(score, 100)