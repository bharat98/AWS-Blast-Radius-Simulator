# 🔥 AWS Blast Radius Simulator (v0.1 – CLI Tool)

The AWS Blast Radius Simulator is a tool that models the potential **impact of a compromised IAM identity** in AWS. By analyzing policy files, it identifies allowed actions, simulates **privilege escalation paths**, and outputs a clear summary of the **blast radius** using known attacker techniques.

This is an early-phase CLI version focused on:
- IAM policy parsing
- Wildcard expansion
- Privilege escalation detection
- Escalation chain recognition

---

## 🚀 Features

- 🧾 Parses AWS IAM policies (JSON format)
- 🔍 Expands wildcards like `s3:*` or `ec2:Describe*` using a curated AWS actions database
- 🛠 Detects risky permissions (`iam:PassRole`, `lambda:UpdateFunctionCode`, etc.)
- 🔗 Identifies complex escalation chains used in real-world attacks
- 📄 Outputs a readable summary of allowed actions and escalation risks

---

## 🧱 Project Structure

```
blast-radius-simulator/
├── simulate.py              # Main CLI script
├── aws_actions.json         # Action database for wildcard expansion
├── escalation_rules.py      # Rules for detecting escalation vectors
├── policy_samples/          # Example IAM policy files
```

---

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/aws-blast-radius-simulator.git
cd aws-blast-radius-simulator
```

2. (Optional) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. Install requirements (currently only standard libraries needed).

---

## 📄 Usage

### Run the simulator with a policy file:

```bash
python simulate.py policy_samples/policy_3.json --actions-db aws_actions.json
```

### Sample Output:
```
[+] Parsed and Expanded Permissions:

  SID: LambdaEscalation
    Action: iam:PassRole
    Action: lambda:UpdateFunctionCode
    Resource: *

    🚨 Privilege Escalation Actions Detected:
      ➤ iam:PassRole
      ➤ lambda:UpdateFunctionCode
    🔗 Escalation Chains Triggered:
      ➤ Lambda Injection via PassRole
```

---

## 🧪 Test Policy Samples

A few sample IAM policies are included in the `policy_samples/` directory:
- `policy_1.json`: Basic S3 read-only (safe)
- `policy_3.json`: Lambda + PassRole (privilege escalation)
- `policy_6.json`: Complex DevOps access with multiple escalation paths

---

## 📚 Coming Soon

- Visual graph of service reachability and escalation paths (Phase 5+)
- Risk scoring model
- Web UI to upload and analyze policies
- Integration with live AWS IAM data via Boto3

---

## 🤝 Contributing / Feedback

This is a work-in-progress project. Feedback, feature suggestions, and PRs are welcome!  
If you'd like to collaborate, feel free to connect or drop an issue.

---

## 📜 License

MIT License



## 🛠️ AWS Blast Radius Simulator – Development Roadmap

| Phase | Goal | Key Tasks | Deliverables | Time Estimate | Effort Estimate |
|-------|------|-----------|--------------|----------------|-----------------|
| **1. Core Engine (MVP)** | Simulate privilege escalation paths from static IAM policy | - Parse IAM policy JSON<br>- Identify risky IAM actions (e.g., `PassRole`, `AssumeRole`, `UpdateFunctionCode`)<br>- Build access graph using NetworkX<br>- Map service-to-service lateral flow | - Working CLI prototype<br>- Graph object of access paths<br>- Text summary of blast radius | 1.5 – 2 weeks | 20 – 30 hrs |
| **2. Visualization Layer** | Make blast radius tangible via visual graphs | - Integrate Mermaid.js or Graphviz<br>- Map nodes (IAM, services) + privilege levels<br>- Export graph as HTML or Markdown | - Visual attack path output<br>- Color-coded graph diagram<br>- Simple exportable report | 1 week | 10 – 15 hrs |
| **3. Lightweight Web UI** | Build basic front end to improve usability | - Flask app setup<br>- Upload/parse IAM policy<br>- Render graph in browser<br>- Output attack summary and scoring (text + visual) | - Hosted local web demo<br>- Clean UI for policy upload<br>- Real-time graph rendering | 1 – 1.5 weeks | 15 – 20 hrs |
| **4. Risk Scoring Engine** | Prioritize identities based on potential damage | - Build scoring logic (e.g., service sensitivity × access level × escalation potential)<br>- Display score in UI<br>- Update graph with risk-weighted paths | - Risk score for each identity<br>- Weighted visual graph<br>- Downloadable risk report | 1 – 1.5 weeks | 15 – 25 hrs |
| **5. Real IAM Integration** | Enable fetching IAM roles/policies from live AWS | - Use Boto3 to fetch attached/inline policies<br>- Integrate IAM Access Analyzer (if needed)<br>- Parse live data into simulator | - Dynamic IAM entity support<br>- AWS account integration<br>- CLI or UI policy loader from AWS | 2 weeks | 25 – 35 hrs |
| **6. Polish & Launch** | Prep for open-source, visibility, and sharing | - Write clear README & docs<br>- Add sample IAM policies<br>- Record demo / write blog<br>- Launch on GitHub + share on LinkedIn | - Public GitHub repo<br>- Demo content & walkthrough<br>- Community-ready project | 1 week | 10 – 12 hrs |
