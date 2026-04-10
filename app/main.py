from dotenv import load_dotenv
# set all env variable in OS
load_dotenv()

from devops_client import AzureDevOpsClient
from ai_engine import AIEngine 

def run_workflow():
    devops = AzureDevOpsClient()
    devops.get_attribute()
    # ai = AIEngine()
    
    # print("Fetching PR changes...")
    # files = devops.fetch_pr_files()
    # full_report = "### 🤖 AI Code Review\n"
    
    # for file_path in files:
    #     if file_path.lower().endswith(('.py', '.cs', '.js')):
    #         content = devops.get_file_content(file_path)
    #         if content:
    #             print(f"Analyzing {file_path}...")
    #             feedback = ai.analyze_code(file_path, content)
    #             full_report += f"\n*File:* {file_path}\n{feedback}\n---"

    # devops.post_comment(full_report)
    # print("Review posted!")



if __name__ == "__main__":
    print('hello')
    run_workflow()