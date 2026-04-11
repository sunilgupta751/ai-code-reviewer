import os
import base64
import requests
import logging

# Logging setup taaki pipeline logs mein dikhe ki AI kya kar raha hai
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

class GitHubClient:
    def __init__(self):
        self.token = os.getenv("GITHUB_TOKEN")
        self.repo = os.getenv("GITHUB_REPOSITORY") # Format: "owner/repo"
        self.pr_id = os.getenv("PR_NUMBER")
        self.base_url = "https://api.github.com"

    def get_auth_header(self):
        return {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github.v3+json",
            "Content-Type": "application/json"
        }

    def fetch_pr_files(self):
        if not self.pr_id:
            logger.error("PR_NUMBER environment variable is missing!")
            return []
        """PR mein change hui files ki list nikalne ke liye"""
        url = f"{self.base_url}/repos/{self.repo}/pulls/{self.pr_id}/files"
        try:
            response = requests.get(url, headers=self.get_auth_header())
            response.raise_for_status()
            # GitHub mein 'filename' key use hoti hai
            return [f['filename'] for f in response.json()]
        except Exception as e:
            logger.error(f"Failed to fetch PR files: {str(e)}")
            return []

    def get_file_content(self, file_path):
        """Specific file ka raw content nikalne ke liye"""
        # Note: Production mein 'ref' (commit SHA) dena best practice hai
        url = f"{self.base_url}/repos/{self.repo}/contents/{file_path}?ref=pull/{self.pr_id}/head"
        try:
            response = requests.get(url, headers=self.get_auth_header())
            if response.status_code == 200:
                # GitHub content base64 mein deta hai, hume use decode karna padega
                import base64
                content_b64 = response.json().get('content', '')
                return base64.b64decode(content_b64).decode('utf-8')
            else:
                return None
        except Exception as e:
            logger.error(f"Error fetching file content: {str(e)}")
            return None

    def post_comment(self, message):
        """PR par feedback comment post karne ke liye"""
        url = f"{self.base_url}/repos/{self.repo}/issues/{self.pr_id}/comments"
        body = {"body": message}
        response = requests.post(url, json=body, headers=self.get_auth_header())
        return response.status_code