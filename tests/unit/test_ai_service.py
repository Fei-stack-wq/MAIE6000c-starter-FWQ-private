from services.ai.app.main import triage_text


def test_triage_access_case():
    result = triage_text(
        "Cannot login",
        "User cannot access the dashboard after a password reset.",
    )
    assert result.label == "access"
    assert result.confidence >= 0.55
    assert "Cannot login" in result.summary


def test_triage_general_case():
    result = triage_text(
        "General question",
        "Need clarification about the process for next week.",
    )
    assert result.label == "general"


def test_triage_timeout_classified_as_incident():
    result = triage_text(
        "Checkout request timeout",
        "The request timed out and could not be completed.",
    )
    assert result.label == "incident"
    assert result.confidence >= 0.55


def test_triage_unavailable_classified_as_incident():
    result = triage_text(
        "Service unavailable",
        "The API is unavailable and requests are failing.",
    )
    assert result.label == "incident"
