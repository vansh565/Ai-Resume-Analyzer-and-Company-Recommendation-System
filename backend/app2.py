from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import re

from resume_parser import (
    extract_text,
    lexical_analysis,
    generate_parse_tree,
    generate_ir
)
from semantic_matcher import semantic_score
from gemini_utils import gemini_feedback, extract_ats_score, gemini_chat
from company_recommendations import get_companies_by_skills, COMPANY_DATABASE

app = Flask(__name__)
CORS(app)

FRONTEND_PATH = os.path.join(os.getcwd(), "..", "frontend")


@app.route("/")
def index():
    return send_from_directory(FRONTEND_PATH, "2.html")


@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(FRONTEND_PATH, path)


# ────────────────────────────────────────────────
# CHAT ENDPOINT – conversational mode
# ────────────────────────────────────────────────
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        message = data.get("message")

        if not message:
            return jsonify({"error": "No message provided"}), 400

        message = message.strip()
        if not message:
            return jsonify({"error": "Empty message not allowed"}), 400

        if len(message) > 3000:
            return jsonify({"error": "Message too long (max ~3000 characters)"}), 400

        # Use the chat-specific function
        response_text = gemini_chat(message)

        return jsonify({
            "reply": response_text
        })

    except Exception as e:
        print("CHAT ERROR:", str(e))
        return jsonify({
            "error": "Sorry — something went wrong while processing your message. Please try again."
        }), 500


# ────────────────────────────────────────────────
# COMPANY RECOMMENDATIONS ENDPOINT
# ────────────────────────────────────────────────
@app.route("/recommend-companies", methods=["POST"])
def recommend_companies():
    try:
        data = request.json
        skills = data.get("skills", [])
        job_category = data.get("job_category", "")

        if not skills and not job_category:
            return jsonify({"error": "No skills or job category provided"}), 400

        # Get recommendations based on skills
        recommendations = get_companies_by_skills(skills, job_category)

        return jsonify({
            "recommendations": recommendations,
            "categories": list(COMPANY_DATABASE.keys())
        })

    except Exception as e:
        print("COMPANY RECOMMENDATION ERROR:", str(e))
        return jsonify({"error": str(e)}), 500


# ────────────────────────────────────────────────
# RESUME ANALYSIS ENDPOINT – keeps structured output
# ────────────────────────────────────────────────
@app.route("/analyze", methods=["POST"])
def analyze_resume():
    try:
        resume_file = request.files.get("resume")
        job_desc = request.form.get("job_desc")

        if not resume_file or not job_desc:
            return jsonify({"error": "Missing resume file or job description"}), 400

        resume_path = "temp_uploaded_resume.pdf"
        resume_file.save(resume_path)

        resume_text = extract_text(resume_path)
        tokens = lexical_analysis(resume_text)

        algo_score = semantic_score(resume_text, job_desc)

        # This one should keep the ATS_SCORE / MISSING_SKILLS format
        feedback = gemini_feedback(resume_text, job_desc)
        gemini_score = extract_ats_score(feedback)

        parse_tree = generate_parse_tree(tokens)
        ir_code = generate_ir(tokens)
        
        # Extract skills from the resume for recommendations
        # Simple skill extraction - you might want to enhance this
        skills = extract_skills_from_text(resume_text)
        
        # Get company recommendations based on extracted skills
        company_recommendations = get_companies_by_skills(skills, "")

        # Clean up temporary file
        try:
            os.remove(resume_path)
        except:
            pass

        return jsonify({
            "ATS_Match_Score": gemini_score,
            "Algorithm_Score": algo_score,
            "Total_Tokens": len(tokens),
            "Gemini_Feedback": feedback,
            "Parse_Tree": parse_tree,
            "IR_Code": ir_code,
            "Extracted_Skills": skills,
            "Company_Recommendations": company_recommendations
        })

    except Exception as e:
        print("ANALYZE SERVER ERROR:", str(e))
        return jsonify({"error": str(e)}), 500


def extract_skills_from_text(text):
    """
    Simple skill extraction from resume text.
    You can enhance this with NLP or keyword matching.
    """
    # Common tech skills keywords
    skill_keywords = {
        "AI_ML": ["machine learning", "deep learning", "ai", "artificial intelligence", "tensorflow", "pytorch", "nlp", "computer vision", "neural networks", "llm", "openai", "langchain"],
        "MERN_FULLSTACK": ["react", "node.js", "express", "mongodb", "mern", "javascript", "typescript", "redux", "next.js", "fullstack"],
        "SOFTWARE_DEVELOPMENT": ["java", "python", "c++", "c#", "software development", "spring boot", "django", "flask", "api", "rest", "microservices"],
        "DATA_SCIENCE": ["data science", "analytics", "pandas", "numpy", "scikit-learn", "statistics", "data visualization", "tableau", "power bi", "sql", "big data"],
        "DEVOPS_CLOUD": ["aws", "azure", "gcp", "docker", "kubernetes", "jenkins", "ci/cd", "terraform", "ansible", "devops", "cloud computing"],
        "CYBER_SECURITY": ["security", "cybersecurity", "penetration testing", "ethical hacking", "network security", "cryptography", "firewall", "vulnerability"],
        "MOBILE_APP_DEVELOPMENT": ["android", "ios", "swift", "kotlin", "react native", "flutter", "mobile development", "app development"],
        "BLOCKCHAIN": ["blockchain", "ethereum", "solidity", "smart contracts", "web3", "cryptocurrency", "hyperledger"],
        "UI_UX_DESIGN": ["ui design", "ux design", "figma", "adobe xd", "sketch", "user experience", "user interface", "prototyping", "wireframing"]
    }
    
    text_lower = text.lower()
    detected_skills = []
    
    for category, keywords in skill_keywords.items():
        for keyword in keywords:
            if keyword.lower() in text_lower:
                detected_skills.append(keyword.title())
    
    # Remove duplicates while preserving order
    detected_skills = list(dict.fromkeys(detected_skills))
    
    return detected_skills[:20]  # Return top 20 skills


if __name__ == "__main__":
    # Using host='0.0.0.0' so you can access from phone/laptop on same network
    # port=5000 is default, but you can change it
    app.run(debug=True, host="0.0.0.0", port=5000)