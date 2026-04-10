<div align="center">

# 🤖 AI PR Code Reviewer

### 🔍 Automated Pull Request Analysis using AI + Docker + Azure DevOps

</div>

---

## 🚀 Overview

This project automatically analyzes Azure DevOps Pull Requests using an **AI-powered containerized system**.

When a PR is created or updated:

- A CI/CD pipeline is triggered
- An AI Docker container is pulled from Azure Container Registry (ACR)
- The container fetches PR changes
- AI analyzes code for:
  - 🔐 Security issues  
  - 🐛 Bugs  
  - ✨ Code quality improvements  
- Results are posted back as PR comments

---

## ⚙️ Architecture
