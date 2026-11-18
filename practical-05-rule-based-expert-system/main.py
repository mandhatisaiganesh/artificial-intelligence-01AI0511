"""
Practical 5: AI Smart Loan Eligibility Advisor - Rule-Based Expert System
Course: 01AI0511 - Artificial Intelligence | Marwadi University
"""

def analyze_loan(data):
    """
    Evaluates loan eligibility rules L1-L6.
    Base score: 40.0, clamped between 5 and 97.
    """
    income = float(data.get("income", 65000))
    credit = float(data.get("credit_score", 760))
    employment = str(data.get("employment", "Permanent")).strip()
    existing_loan = str(data.get("existing_loan", "No")).strip().lower()
    experience = float(data.get("experience", 5))
    loan_amount = float(data.get("loan_amount", 800000))
    repayment = str(data.get("repayment", "Good")).strip()

    if income <= 0:
        raise ValueError("Monthly income must be greater than zero.")
    if not (300 <= credit <= 900):
        raise ValueError("Credit score must be between 300 and 900.")

    score = 40.0
    factors_pos, factors_neg, fired = [], [], []

    # Rule L1: Credit score
    if credit >= 750:
        score += 22
        factors_pos.append("Good credit score")
        fired.append({"rule": "L1", "condition": "credit_score >= 750", "effect": "+22"})
    elif credit >= 650:
        score += 10
        factors_pos.append("Acceptable credit score")
        fired.append({"rule": "L1", "condition": "credit_score >= 650", "effect": "+10"})
    else:
        score -= 20
        factors_neg.append("Low credit score")
        fired.append({"rule": "L1", "condition": "credit_score < 650", "effect": "-20"})

    # Rule L2: Employment stability
    if employment.lower() in ["permanent", "salaried"]:
        score += 15
        factors_pos.append("Stable employment")
        fired.append({"rule": "L2", "condition": "employment in [Permanent, Salaried]", "effect": "+15"})
    else:
        factors_neg.append("Non-permanent employment")

    # Rule L3: Existing loan
    if existing_loan == "no":
        score += 10
        factors_pos.append("No existing loan")
        fired.append({"rule": "L3", "condition": "existing_loan == No", "effect": "+10"})
    else:
        score -= 10
        factors_neg.append("Existing loan debt burden")
        fired.append({"rule": "L3", "condition": "existing_loan == Yes", "effect": "-10"})

    # Rule L4: EMI / income proxy (assuming 5-year repayment proxy)
    monthly_emi_proxy = (loan_amount * 1.08) / 60.0
    emi_ratio = (monthly_emi_proxy / income) * 100.0
    if emi_ratio <= 35.0:
        score += 15
        factors_pos.append("Sufficient income for requested loan (EMI <= 35%)")
        fired.append({"rule": "L4", "condition": "EMI/income <= 35%", "effect": "+15"})
    else:
        score -= 15
        factors_neg.append(f"High EMI to income ratio ({emi_ratio:.1f}%)")
        fired.append({"rule": "L4", "condition": "EMI/income > 35%", "effect": "-15"})

    # Rule L5: Work experience
    if experience >= 3.0:
        score += 8
        factors_pos.append(f"Adequate work experience ({int(experience)} years)")
        fired.append({"rule": "L5", "condition": "experience >= 3 years", "effect": "+8"})
    else:
        factors_neg.append("Less than 3 years work experience")

    # Rule L6: Repayment history
    if repayment.lower() in ["good", "excellent"]:
        score += 8
        factors_pos.append("Positive repayment history")
        fired.append({"rule": "L6", "condition": "repayment in [Good, Excellent]", "effect": "+8"})
    else:
        score -= 8
        factors_neg.append("Poor repayment history")
        fired.append({"rule": "L6", "condition": "repayment poor", "effect": "-8"})

    raw_score = score
    clamped_score = max(5.0, min(97.0, score))

    if clamped_score >= 75.0:
        eligibility = "HIGH"
    elif clamped_score >= 50.0:
        eligibility = "MEDIUM"
    else:
        eligibility = "LOW"

    return {
        "eligibility": eligibility,
        "clamped_score": clamped_score,
        "raw_score": raw_score,
        "rules_fired": fired,
        "positive_factors": factors_pos,
        "risk_factors": factors_neg,
        "emi_ratio": emi_ratio
    }


def launch_gradio():
    import gradio as gr

    def predict_ui(income, credit, emp, existing, exp, loan_amt, repay):
        data = {
            "income": income,
            "credit_score": credit,
            "employment": emp,
            "existing_loan": existing,
            "experience": exp,
            "loan_amount": loan_amt,
            "repayment": repay
        }
        res = analyze_loan(data)
        fired_txt = "\n".join([f"- **{r['rule']}** ({r['condition']}): `{r['effect']}`" for r in res["rules_fired"]])
        pos_txt = "\n".join([f"- {f}" for f in res["positive_factors"]])
        neg_txt = "\n".join([f"- {f}" for f in res["risk_factors"]]) if res["risk_factors"] else "- None"
        report = f"""### Assessment Result: **{res['eligibility']}**
**Rule Score:** {res['clamped_score']:.1f}/100 (Raw: {res['raw_score']:.1f}) | **Rules Fired:** {len(res['rules_fired'])}

#### Positive Factors:
{pos_txt}

#### Risk Factors:
{neg_txt}

#### Fired Rules:
{fired_txt}
"""
        return report

    demo = gr.Interface(
        fn=predict_ui,
        inputs=[
            gr.Number(value=65000, label="Monthly Income (INR)"),
            gr.Slider(300, 900, value=760, step=1, label="Credit Score"),
            gr.Radio(["Permanent", "Contract", "Self-Employed"], value="Permanent", label="Employment"),
            gr.Radio(["No", "Yes"], value="No", label="Existing Loan"),
            gr.Number(value=5, label="Experience (Years)"),
            gr.Number(value=800000, label="Requested Loan Amount (INR)"),
            gr.Radio(["Good", "Average", "Poor"], value="Good", label="Repayment History")
        ],
        outputs=gr.Markdown(),
        title="AI Smart Loan Eligibility Advisor",
        description="Expert system using production rules L1-L6 with explainable scoring."
    )
    demo.launch()


if __name__ == "__main__":
    test_cases = [
        {"name": "Strong Applicant", "income": 65000, "credit_score": 760, "employment": "Permanent", "existing_loan": "No", "experience": 5, "loan_amount": 800000, "repayment": "Good"},
        {"name": "Borderline Applicant", "income": 35000, "credit_score": 670, "employment": "Permanent", "existing_loan": "Yes", "experience": 2, "loan_amount": 500000, "repayment": "Good"},
        {"name": "Higher-Risk Applicant", "income": 20000, "credit_score": 580, "employment": "Contract", "existing_loan": "Yes", "experience": 1, "loan_amount": 700000, "repayment": "Poor"}
    ]

    print("=" * 65)
    print(" AI SMART LOAN ELIGIBILITY ADVISOR - EXPERT SYSTEM")
    print("=" * 65)

    for case in test_cases:
        res = analyze_loan(case)
        print(f"\nCase: {case['name']}")
        print(f"  Assessment  : {res['eligibility']}")
        print(f"  Rule Score  : {res['clamped_score']:.1f} / 100 (raw {res['raw_score']:.1f})")
        print(f"  Rules Fired : {len(res['rules_fired'])} rules")
        print(f"  Positive    : {', '.join(res['positive_factors'])}")
        if res['risk_factors']:
            print(f"  Risks       : {', '.join(res['risk_factors'])}")

    print("\n" + "=" * 65)
