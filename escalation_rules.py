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
    "cloudformation:CreateStack",
    "iam:CreateUser"
}

ESCALATION_CHAINS = [
    {
        "name": "Lambda Injection via PassRole",
        "required": {"iam:PassRole", "lambda:UpdateFunctionCode"}
    },
    {
        "name": "EC2 Backdoor via PassRole",
        "required": {"iam:PassRole", "ec2:RunInstances"}
    },
    {
        "name": "CloudFormation Root Stack",
        "required": {"cloudformation:CreateStack", "iam:PassRole"}
    },
    {
        "name": "Custom Admin User Creation",
        "required": {"iam:CreateUser", "iam:PutUserPolicy"}
    },
    {
        "name": "STS Role Escalation",
        "required": {"sts:AssumeRole"}
    }
]

def detect_escalation(actions):
    """Return simple escalation actions present"""
    return sorted([a for a in actions if a in ESCALATION_ACTIONS])

def detect_escalation_chains(actions):
    """Return escalation chains triggered by this action set"""
    triggered = []
    actions_set = set(actions)

    for chain in ESCALATION_CHAINS:
        if chain["required"].issubset(actions_set):
            triggered.append(chain["name"])

    return triggered
