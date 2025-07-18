from utils.risk import assess_risk

def test_risk_low():
    assert assess_risk(55, 2000, "Low") == "Low"

def test_risk_medium():
    assert assess_risk(35, 4000, "Medium") == "Medium"

def test_risk_high():
    assert assess_risk(25, 8000, "High") == "High"