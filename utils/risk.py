def assess_risk(age: int, income: float, tolerance: str) -> str:
    score = 0
    score += 2 if age < 30 else 1 if age < 50 else 0
    score += 1 if income < 3000 else 2
    score += {"Low": 0, "Medium": 1, "High": 2}.get(tolerance, 0)

    if score <= 2:
        return "Low"
    elif score <= 4:
        return "Medium"
    return "High"

def agent_advice(risk_level: str) -> str:
    messages = {
        "Low": "🟡 You're better suited for safer, more stable assets like bonds and gold.",
        "Medium": "🟠 Balance is key. Diversify across asset classes.",
        "High": "🔴 Consider high-growth assets like crypto and stocks—but cautiously."
    }
    return messages.get(risk_level, "⚠️ Unknown risk level.")
