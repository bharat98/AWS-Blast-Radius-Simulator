# simulate.py

import argparse
import json
from pathlib import Path
import re

# ======================================== Wildcard Expansion ========================================

def load_aws_actions_db(path="aws_actions.json"):
    """Load AWS actions database from JSON"""
    try:
        with open(path, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"[ERROR] Could not load AWS actions DB: {e}")
        return {}

def expand_actions(actions, aws_actions_db):
    """Expand wildcard actions into individual permissions"""
    expanded = []

    for action in actions:
        if action == "*":
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
            expanded.append(action)

    return sorted(set(expanded))

# ======================================== IAM Policy Logic ========================================

def load_policy(file_path):
    """Load and return IAM policy JSON from file"""
    try:
        with open(file_path, 'r') as f:
            policy = json.load(f)
        return policy
    except Exception as e:
        print(f"[ERROR] Failed to load policy: {e}")
        return None

def extract_permissions(policy, aws_actions_db):
    """Extract and expand all allowed actions from the policy"""
    permissions = []

    statements = policy.get("Statement", [])
    if not isinstance(statements, list):
        statements = [statements]  # Normalize single-object policies

    for stmt in statements:
        if stmt.get("Effect", "").lower() != "allow":
            continue

        actions = stmt.get("Action", [])
        if isinstance(actions, str):
            actions = [actions]

        resources = stmt.get("Resource", "*")
        if isinstance(resources, str):
            resources = [resources]

        expanded = expand_actions(actions, aws_actions_db)

        permissions.append({
            "Sid": stmt.get("Sid", "None"),
            "ExpandedActions": expanded,
            "Resources": resources
        })

    return permissions

# ======================================== Main CLI ========================================

def main():
    parser = argparse.ArgumentParser(description="Simulate IAM policy blast radius.")
    parser.add_argument("policy", type=str, help="Path to IAM policy JSON file")
    parser.add_argument("--actions-db", type=str, default="aws_actions.json", help="Path to AWS actions JSON")
    args = parser.parse_args()

    policy = load_policy(args.policy)
    if policy is None:
        return

    aws_actions_db = load_aws_actions_db(args.actions_db)
    if not aws_actions_db:
        return

    permissions = extract_permissions(policy, aws_actions_db)

    print("\n[+] Parsed and Expanded Permissions:")
    for p in permissions:
        print(f"\n  SID: {p['Sid']}")
        for action in p['ExpandedActions']:
            print(f"    Action: {action}")
        for resource in p['Resources']:
            print(f"    Resource: {resource}")

if __name__ == "__main__":
    main()
