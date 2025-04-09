# AWS-Blast-Radius-Simulator






## 🛠️ AWS Blast Radius Simulator – Development Roadmap

| Phase | Goal | Key Tasks | Deliverables | Time Estimate | Effort Estimate |
|-------|------|-----------|--------------|----------------|-----------------|
| **1. Core Engine (MVP)** | Simulate privilege escalation paths from static IAM policy | - Parse IAM policy JSON<br>- Identify risky IAM actions (e.g., `PassRole`, `AssumeRole`, `UpdateFunctionCode`)<br>- Build access graph using NetworkX<br>- Map service-to-service lateral flow | - Working CLI prototype<br>- Graph object of access paths<br>- Text summary of blast radius | 1.5 – 2 weeks | 20 – 30 hrs |
| **2. Visualization Layer** | Make blast radius tangible via visual graphs | - Integrate Mermaid.js or Graphviz<br>- Map nodes (IAM, services) + privilege levels<br>- Export graph as HTML or Markdown | - Visual attack path output<br>- Color-coded graph diagram<br>- Simple exportable report | 1 week | 10 – 15 hrs |
| **3. Lightweight Web UI** | Build basic front end to improve usability | - Flask app setup<br>- Upload/parse IAM policy<br>- Render graph in browser<br>- Output attack summary and scoring (text + visual) | - Hosted local web demo<br>- Clean UI for policy upload<br>- Real-time graph rendering | 1 – 1.5 weeks | 15 – 20 hrs |
| **4. Risk Scoring Engine** | Prioritize identities based on potential damage | - Build scoring logic (e.g., service sensitivity × access level × escalation potential)<br>- Display score in UI<br>- Update graph with risk-weighted paths | - Risk score for each identity<br>- Weighted visual graph<br>- Downloadable risk report | 1 – 1.5 weeks | 15 – 25 hrs |
| **5. Real IAM Integration** | Enable fetching IAM roles/policies from live AWS | - Use Boto3 to fetch attached/inline policies<br>- Integrate IAM Access Analyzer (if needed)<br>- Parse live data into simulator | - Dynamic IAM entity support<br>- AWS account integration<br>- CLI or UI policy loader from AWS | 2 weeks | 25 – 35 hrs |
| **6. Polish & Launch** | Prep for open-source, visibility, and sharing | - Write clear README & docs<br>- Add sample IAM policies<br>- Record demo / write blog<br>- Launch on GitHub + share on LinkedIn | - Public GitHub repo<br>- Demo content & walkthrough<br>- Community-ready project | 1 week | 10 – 12 hrs |
