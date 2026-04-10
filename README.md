<div align="center">

# 🤖 AI PR Code Reviewer

### 🔍 Automated Pull Request Analysis using AI + Docker + Azure DevOps

</div>

---

## 🚀 Overview

This project automatically analyzes Azure DevOps Pull Requests using an **AI-powered containerized system**.

When a PR is created or updated:

- A CI/CD pipeline is triggered
- An AI Docker image is pulled from Azure Container Registry (ACR)
- Image is executed as a running container
- The container fetches PR changes
- Code is sent to AI engine for analysis 
- AI analyzes code for:
  - 🔐 Security issues  
  - 🐛 Bugs  
  - ✨ Code quality improvements  
- Results are posted back as PR comments

---
