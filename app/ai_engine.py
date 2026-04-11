import os
import logging
from openai import AzureOpenAI

# Logging setup taaki pipeline logs mein dikhe ki AI kya kar raha hai
logger = logging.getLogger(__name__)

class AIEngine:
    def _init_(self):
        self.client = AzureOpenAI(
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_KEY"),
            api_version="2024-02-15-preview",
            deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
        )
        if not self.client.azure_endpoint or not self.client.api_key:
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
        try:
            response = self.client.chat.completions.create(
                model=self.client.deployment_name
                messages=[
                        {"role": "system", "content": "You are a professional code reviewer who provides technical, concise, and helpful feedback."},
                        {"role": "user", "content": prompt}
                    ],
                temperature=0.2 # Temperature kam rakha hai taaki response consistent rahe
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Error during AI Analysis for {file_path}: {str(e)}")
            return f"⚠️ Could not analyze this file due to an error: {str(e)}"