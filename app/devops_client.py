import os
import base64
import requests
class AzureDevOpsClient:
    def __init__(self):
        self.pat=os.getenv("AZURE_DEVOPS_PAT") #personal access token
        self.org_url=os.getenv("SYSTEM_COLLECTIONURI")
        self.project=os.getenv("SYSTEM_TEAMPROJECT")
        self.repo_id=os.getenv("BUILD_REPOSITORY_ID")
        self.pr_id=os.getenv("SYSTEM_PULLREQUEST_PULLREQUESTID")

    def get_auth_header(self):
        auth_str=f":{self.pat}"
        encoded=base64.b64encode(auth_str.encode()).decode()
        return{"Authorization":f"Basic {encoded}","Content-Type":"application/json"}
    

    def fetch_pr_files(self):
        url = f"{self.org_url}{self.project}/_apis/git/repositories/{self.repo_id}/pullRequests/{self.pr_id}/changes?api-version=7.1-preview.1"
        response = requests.get(url, headers=self.get_auth_header())
        response.raise_for_status()
        return [c['item']['path'] for c in response.json()['changes'] if 'item' in c]

    def get_file_content(self, path):
        url = f"{self.org_url}{self.project}/_apis/git/repositories/{self.repo_id}/items?path={path}&api-version=7.1-preview.1"
        res = requests.get(url, headers=self.get_auth_headers())
        return res.text if res.status_code == 200 else None

    def post_comment(self, message):
        url = f"{self.org_url}{self.project}/_apis/git/repositories/{self.repo_id}/pullRequests/{self.pr_id}/threads?api-version=7.1-preview.1"
        body = {"comments": [{"content": message, "parentCommentId": 0, "commentType": 1}], "status": 1}
        requests.post(url, json=body, headers=self.get_auth_headers())