# escalation_rules.py

ESCALATION_ACTIONS = {
    "iam:PassRole",
    "iam:AttachUserPolicy",
    "iam:PutUserPolicy",
    "iam:PutRolePolicy",
    "sts:AssumeRole",
    "lambda:CreateFunction",
    "lambda:UpdateFunctionCode",
    "ec2:RunInstances",
    "cloudformation:CreateStack"
}

def detect_escalation(actions):
    """Return list of escalation actions present in this policy"""
    return sorted([a for a in actions if a in ESCALATION_ACTIONS])
