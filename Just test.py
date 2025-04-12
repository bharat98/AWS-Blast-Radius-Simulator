'''File = open("policy_1.json","rt")
print(File.read())'''

import json
import re

def load_aws_actions_db():
    path="aws_actions.json"
    with open(path, "r") as f:
        return json.load(f)

def expand_actions(actions, aws_actions_db):
    """Expand wildcard actions into individual permissions"""
    expanded = []

    for action in actions:
        if action == "*":
            # Expand to all actions from all services
            for service_actions in aws_actions_db.values():
                expanded.extend(service_actions)

        elif "*" in action:
            service_prefix = action.split(":")[0]
            if service_prefix not in aws_actions_db:
                continue

            pattern = "^" + action.replace("*", ".*") + "$"
            regex = re.compile(pattern)

            matches = [a for a in aws_actions_db[service_prefix] if regex.match(a)]
            expanded.extend(matches)

        else:
            # No wildcard, keep as-is
            expanded.append(action)

    return sorted(set(expanded))


aws_db = load_aws_actions_db()
raw_actions = ["s3:*", "iam:PassRole", "lambda:UpdateFunctionCode"]
expanded = expand_actions(raw_actions, aws_db)

for action in expanded:
    print(action)