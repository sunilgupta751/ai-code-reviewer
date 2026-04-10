import os
from openai import AzureOpenAI

class AIEngine:
    def _init_(self):
        self.client = AzureOpenAI(
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_KEY"),
            api_version="2024-02-15-preview"
        )

    def analyze_code(self, file_path, content):
        prompt = f"Review this {file_path} for security, bugs, and best practices. Be concise.\n\nCode:\n{content}"
        response = self.client.chat.completions.create(
            model="gpt-4o", # Replace with your deployment name
            messages=[{"role": "system", "content": "You are a Senior Engineer."},
                      {"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content