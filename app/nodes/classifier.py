from app.state import LegalState

def classify_case(state: LegalState):

    query = state["user_query"].lower()

    criminal_keywords = [
        "theft", "stole", "steal",
        "robbery", "murder",
        "assault", "attack",
        "fraud", "cheating"
    ]

    family_keywords = [
        "divorce",
        "marriage",
        "custody",
        "alimony"
    ]

    cyber_keywords = [
        "hack",
        "hacked",
        "cyber",
        "upi",
        "otp",
        "phishing",
        "online fraud"
    ]

    if any(word in query for word in criminal_keywords):
        category = "Criminal"

    elif any(word in query for word in family_keywords):
        category = "Family"

    elif any(word in query for word in cyber_keywords):
        category = "Cyber"

    else:
        category = "Civil"

    return {
        "legal_category": category
    }