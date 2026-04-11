import os
import logging
from openai import AzureOpenAI

# Logging setup taaki pipeline logs mein dikhe ki AI kya kar raha hai
logger = logging.getLogger(__name__)

class AIEngine:
    def _init_(self):
        # Environment variables se data uthayein
        endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        api_key = os.getenv("AZURE_OPENAI_KEY")
        self.deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

        self.client = AzureOpenAI(
            azure_endpoint=endpoint,
            api_key=api_key,
            api_version="2024-02-15-preview"
        )
        
        if not endpoint or not api_key or not self.deployment_name:
            logger.error("Azure OpenAI Credentials missing in Environment Variables!")
            raise ValueError("Missing Azure OpenAI configuration.")
        # Deployment name jo aapne Azure portal mein rakha hai
        

    def analyze_code(self, file_path, content):

        logger.info(f"AI Engine: Analyzing {file_path}...")
        
        # Professional Prompt Engineering
        system_prompt = (
            f"You are a Senior Software Engineer. Review the code in '{file_path}'.\n"
            f"Focus on:\n"
            f"1. Security vulnerabilities (OWASP).\n"
            f"2. Potential bugs or edge cases.\n"
            f"3. Code quality and SOLID principles.\n\n"
            f"Code Content:\n{content}\n\n"
            f"Provide a concise, professional summary with actionable feedback."
        )
        # User Message: Actual kaam aur data bhejta hai
        user_prompt = f"Review the following file: {file_path}\n\nContent:\n{content}"
        try:
            response = self.client.chat.completions.create(
                model=self.deployment_name,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.2 # Temperature kam rakha hai taaki response consistent rahe
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Error during AI Analysis for {file_path}: {str(e)}")
            return f"⚠️ Could not analyze this file due to an error: {str(e)}"