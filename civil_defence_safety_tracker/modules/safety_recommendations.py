def get_recommendations(risk_type):
    recommendations = {
        "Fire": ["Install fire alarms", "Have an emergency exit plan", "Keep fire extinguishers nearby"],
        "Flood": ["Avoid low areas", "Have emergency supplies", "Stay informed about weather alerts"],
        "Earthquake": ["Secure heavy furniture", "Have an evacuation plan", "Keep an emergency kit"]
    }
    return recommendations.get(risk_type, ["No specific recommendations available."])
