import os
import logging
from dotenv import load_dotenv

# 1. Sabse pehle env load karein
load_dotenv()

# 2. Local Imports (Jo environment variables use karte hain)
from devops_client import GitHubClient
from ai_engine import AIEngine

# 3. Logging Setup
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


def run_workflow():
    devops = GitHubClient()
    ai = AIEngine()

    logger.info("Fetching PR changes from GitHub...")
    files = devops.fetch_pr_files()
    logger.info(files)
    if not files:
        logger.info("No modified files found in this PR.")
        return
    full_report = "### 🤖 AI Code Review\n\n"
    review_generated = False
    for file_path in files:
        if file_path.lower().endswith(('.py', '.cs', '.js', '.ts', '.sql')):    
            try:
                content = devops.get_file_content(file_path)
                if content:
                    print(f"Analyzing {file_path}...")
                    feedback = ai.analyze_code(file_path, content)
                    full_report += f"\n*File:* {file_path}\n{feedback}\n---"
                    review_generated = True
                else:
                    logger.warning(f"Skipping {file_path}: No content found.")
            except Exception as e:
                    logger.error(f"Error analyzing {file_path}: {str(e)}")
    if review_generated:
        devops.post_comment(full_report)
        logger.info("Professional review posted to GitHub PR successfully!")
        print("Review posted successfully!")
    else:
        logger.info("No code changes required review.")

if __name__ == "__main__":
    run_workflow()