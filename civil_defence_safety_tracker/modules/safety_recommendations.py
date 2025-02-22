def get_recommendations(risk_type):
    """
    Retrieves safety recommendations based on the given risk type.

    Args:
        risk_type (str): The type of risk (e.g., "Fire", "Flood", "Earthquake").

    Returns:
        list: A list of recommended safety measures for the specified risk type.
        If the risk type is not found, returns a default message.

    Example:
        get_recommendations("Fire")
       #output: ["Install fire alarms", "Have an emergency exit plan", "Keep fire extinguishers nearby"]
     """
   



    recommendations = {
        "Fire": ["Install fire alarms", "Have an emergency exit plan", "Keep fire extinguishers nearby"],
        "Flood": ["Avoid low areas", "Have emergency supplies", "Stay informed about weather alerts"],
        "Earthquake": ["Secure heavy furniture", "Have an evacuation plan", "Keep an emergency kit"]
    }
    return recommendations.get(risk_type, ["No specific recommendations available."])
