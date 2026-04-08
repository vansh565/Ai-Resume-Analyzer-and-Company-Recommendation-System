import re
import google.generativeai as genai

import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get API key from .env
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)


model = genai.GenerativeModel("gemini-3-flash-preview")
generation_config={"temperature": 0.7, "top_p": 0.95}
def gemini_chat(message):
    """
    Conversational mode – no forced ATS structure, natural replies
    """
    prompt = f"""You are a supportive resume & career coach.  
Answer every message in exactly 1–2 short, positive, actionable lines only.

Respond naturally like a helpful human coach. only give answer related to resume not any other thing

User message: {message}

Your reply:"""

    response = model.generate_content(prompt)
    return response.text.strip()
def gemini_feedback(resume_text, job_desc):
    prompt = f"""
You are an ATS Resume Analyzer.

STRICT FORMAT. EACH ITEM ON NEW LINE.

ATS_SCORE: <0-100>
MISSING_SKILLS: skill1, skill2, skill3
SUGGESTIONS:
- suggestion 1
- suggestion 2

Resume:
{resume_text}

Job Description:
{job_desc}
"""

    response = model.generate_content(prompt)
    return response.text
def extract_ats_score(text):
    """
    Strictly extracts ATS score only from ATS_SCORE line
    """
    for line in text.splitlines():
        if line.strip().upper().startswith("ATS_SCORE"):
            nums = re.findall(r'\d{1,3}', line)
            if nums:
                score = int(nums[0])
                return min(max(score, 0), 100)
    return 0

