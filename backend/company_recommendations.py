# company_recommendations.py

COMPANY_DATABASE = {
    "AI_ML": [
        {
            "name": "Google India", 
            "link": "https://careers.google.com/jobs/results/?location=India",
            "package": "₹30-60 LPA",
            "roles": ["AI/ML Engineer", "Research Scientist", "ML Engineer"],
            "description": "Leading tech giant with cutting-edge AI research and development. Known for Google Brain, DeepMind, and TensorFlow.",
            "rating": "4.5/5",
            "locations": ["Bangalore", "Hyderabad", "Gurgaon"]
        },
        {
            "name": "Microsoft India", 
            "link": "https://careers.microsoft.com/v2/global/en/locations/india.html",
            "package": "₹25-55 LPA",
            "roles": ["Applied Scientist", "ML Engineer", "AI Researcher"],
            "description": "Global technology leader with strong AI focus through Azure AI, Cognitive Services, and research division.",
            "rating": "4.4/5",
            "locations": ["Hyderabad", "Bangalore", "Noida"]
        },
        {
            "name": "Amazon India", 
            "link": "https://www.amazon.jobs/en/locations/india",
            "package": "₹24-50 LPA",
            "roles": ["ML Engineer", "Data Scientist", "Applied Scientist"],
            "description": "E-commerce giant leveraging AI for recommendation systems, supply chain optimization, and Alexa.",
            "rating": "4.3/5",
            "locations": ["Bangalore", "Hyderabad", "Chennai"]
        },
        {
            "name": "Flipkart", 
            "link": "https://www.flipkartcareers.com/",
            "package": "₹20-40 LPA",
            "roles": ["ML Engineer", "Data Scientist", "AI Engineer"],
            "description": "India's leading e-commerce platform with advanced AI/ML applications in personalization and logistics.",
            "rating": "4.2/5",
            "locations": ["Bangalore"]
        },
        {
            "name": "Fractal Analytics", 
            "link": "https://fractal.ai/careers/",
            "package": "₹18-35 LPA",
            "roles": ["Data Scientist", "ML Engineer", "AI Consultant"],
            "description": "Leading AI and analytics company serving Fortune 500 clients globally.",
            "rating": "4.1/5",
            "locations": ["Mumbai", "Bangalore", "Gurgaon"]
        }
    ],
    "MERN_FULLSTACK": [
        {
            "name": "Paytm", 
            "link": "https://www.paytm.com/careers",
            "package": "₹18-35 LPA",
            "roles": ["Full Stack Developer", "Software Engineer", "Frontend Lead"],
            "description": "India's largest digital payments platform with massive scale and modern tech stack.",
            "rating": "4.0/5",
            "locations": ["Noida", "Bangalore"]
        },
        {
            "name": "PhonePe", 
            "link": "https://www.phonepe.com/careers/",
            "package": "₹20-40 LPA",
            "roles": ["Full Stack Engineer", "Software Development Engineer"],
            "description": "Leading fintech company with high-growth engineering culture and modern MERN stack.",
            "rating": "4.3/5",
            "locations": ["Bangalore"]
        },
        {
            "name": "Groww", 
            "link": "https://groww.in/careers",
            "package": "₹18-38 LPA",
            "roles": ["Full Stack Developer", "Software Engineer"],
            "description": "Fast-growing investment platform with modern tech stack and great work culture.",
            "rating": "4.4/5",
            "locations": ["Bangalore"]
        },
        {
            "name": "Meesho", 
            "link": "https://www.meesho.com/careers",
            "package": "₹22-45 LPA",
            "roles": ["Software Engineer", "Full Stack Developer"],
            "description": "Social commerce unicorn with rapid growth and challenging engineering problems.",
            "rating": "4.2/5",
            "locations": ["Bangalore"]
        },
        {
            "name": "Swiggy", 
            "link": "https://www.swiggy.com/careers",
            "package": "₹20-42 LPA",
            "roles": ["Full Stack Engineer", "Software Development Engineer"],
            "description": "Food delivery giant with complex distributed systems and high-scale applications.",
            "rating": "4.1/5",
            "locations": ["Bangalore", "Gurgaon"]
        }
    ],
    "SOFTWARE_DEVELOPMENT": [
        {
            "name": "TCS", 
            "link": "https://www.tcs.com/careers",
            "package": "₹7-15 LPA",
            "roles": ["System Engineer", "Software Developer", "IT Analyst"],
            "description": "India's largest IT services company with massive global presence.",
            "rating": "3.8/5",
            "locations": ["Multiple locations across India"]
        },
        {
            "name": "Infosys", 
            "link": "https://www.infosys.com/careers/",
            "package": "₹8-18 LPA",
            "roles": ["Software Engineer", "Senior Software Engineer", "Technology Analyst"],
            "description": "Global leader in consulting and IT services with strong training programs.",
            "rating": "3.9/5",
            "locations": ["Multiple locations across India"]
        },
        {
            "name": "Accenture India", 
            "link": "https://www.accenture.com/in-en/careers",
            "package": "₹10-25 LPA",
            "roles": ["Software Engineer", "Application Developer", "Full Stack Developer"],
            "description": "Global professional services company with strong digital transformation focus.",
            "rating": "4.0/5",
            "locations": ["Bangalore", "Hyderabad", "Mumbai", "Pune"]
        },
        {
            "name": "Adobe India", 
            "link": "https://careers.adobe.com/",
            "package": "₹25-50 LPA",
            "roles": ["Software Engineer", "Computer Scientist", "SDE"],
            "description": "Creative software leader with excellent engineering culture and work-life balance.",
            "rating": "4.5/5",
            "locations": ["Noida", "Bangalore"]
        }
    ],
    "DATA_SCIENCE": [
        {
            "name": "Fractal Analytics", 
            "link": "https://fractal.ai/careers/",
            "package": "₹18-35 LPA",
            "roles": ["Data Scientist", "Analytics Consultant", "ML Engineer"],
            "description": "Leading AI and analytics firm serving Fortune 500 clients globally.",
            "rating": "4.2/5",
            "locations": ["Mumbai", "Bangalore", "Gurgaon"]
        },
        {
            "name": "Mu Sigma", 
            "link": "https://www.mu-sigma.com/careers",
            "package": "₹15-30 LPA",
            "roles": ["Decision Scientist", "Data Scientist", "Analytics Consultant"],
            "description": "World's largest pure-play data analytics and decision science company.",
            "rating": "3.9/5",
            "locations": ["Bangalore"]
        },
        {
            "name": "Tiger Analytics", 
            "link": "https://www.tigeranalytics.com/careers/",
            "package": "₹16-32 LPA",
            "roles": ["Data Scientist", "Analytics Consultant", "ML Engineer"],
            "description": "Fast-growing AI and analytics consulting firm with global clients.",
            "rating": "4.1/5",
            "locations": ["Chennai", "Bangalore", "Hyderabad"]
        }
    ],
    "DEVOPS_CLOUD": [
        {
            "name": "AWS India", 
            "link": "https://aws.amazon.com/careers/",
            "package": "₹25-55 LPA",
            "roles": ["Cloud Architect", "DevOps Engineer", "Solutions Architect"],
            "description": "Leading cloud provider with cutting-edge infrastructure and services.",
            "rating": "4.3/5",
            "locations": ["Bangalore", "Hyderabad", "Pune"]
        },
        {
            "name": "Google Cloud India", 
            "link": "https://careers.google.com/jobs/results/?category=Cloud",
            "package": "₹30-60 LPA",
            "roles": ["Cloud Engineer", "Site Reliability Engineer", "DevOps Engineer"],
            "description": "Google's cloud platform with innovative technologies and global scale.",
            "rating": "4.4/5",
            "locations": ["Bangalore", "Hyderabad"]
        }
    ],
    "CYBER_SECURITY": [
        {
            "name": "Palo Alto Networks India", 
            "link": "https://jobs.paloaltonetworks.com/en/india",
            "package": "₹20-45 LPA",
            "roles": ["Security Engineer", "Threat Researcher", "Security Analyst"],
            "description": "Global cybersecurity leader with cutting-edge security products.",
            "rating": "4.2/5",
            "locations": ["Bangalore", "Pune"]
        },
        {
            "name": "EY India", 
            "link": "https://careers.ey.com/",
            "package": "₹12-25 LPA",
            "roles": ["Security Consultant", "Cybersecurity Analyst", "GRC Specialist"],
            "description": "Big 4 firm with strong cybersecurity consulting practice.",
            "rating": "4.0/5",
            "locations": ["Multiple locations"]
        }
    ],
    "MOBILE_APP_DEVELOPMENT": [
        {
            "name": "PhonePe", 
            "link": "https://www.phonepe.com/careers/",
            "package": "₹20-40 LPA",
            "roles": ["Android Developer", "iOS Developer", "Mobile Lead"],
            "description": "Leading fintech app with millions of daily active users.",
            "rating": "4.3/5",
            "locations": ["Bangalore"]
        },
        {
            "name": "Swiggy", 
            "link": "https://www.swiggy.com/careers",
            "package": "₹20-42 LPA",
            "roles": ["Mobile Engineer", "Android/iOS Developer"],
            "description": "Food delivery app with complex mobile experiences and high scale.",
            "rating": "4.1/5",
            "locations": ["Bangalore"]
        }
    ],
    "BLOCKCHAIN": [
        {
            "name": "Polygon Labs", 
            "link": "https://polygon.technology/careers",
            "package": "₹25-55 LPA",
            "roles": ["Blockchain Engineer", "Smart Contract Developer", "Protocol Engineer"],
            "description": "Leading Ethereum scaling solution with strong developer ecosystem.",
            "rating": "4.4/5",
            "locations": ["Remote", "Bangalore"]
        },
        {
            "name": "CoinDCX", 
            "link": "https://coindcx.com/careers",
            "package": "₹20-45 LPA",
            "roles": ["Blockchain Developer", "Backend Engineer", "Security Engineer"],
            "description": "India's largest cryptocurrency exchange with rapid growth.",
            "rating": "4.1/5",
            "locations": ["Mumbai", "Bangalore"]
        }
    ],
    "UI_UX_DESIGN": [
        {
            "name": "Google India", 
            "link": "https://careers.google.com/jobs/results/?category=User+Experience",
            "package": "₹25-50 LPA",
            "roles": ["UX Designer", "Product Designer", "Interaction Designer"],
            "description": "World-class design teams working on globally impactful products.",
            "rating": "4.5/5",
            "locations": ["Bangalore", "Hyderabad"]
        },
        {
            "name": "Adobe India", 
            "link": "https://careers.adobe.com/",
            "package": "₹22-48 LPA",
            "roles": ["UX Designer", "Product Designer", "Design Technologist"],
            "description": "Design software leader with strong emphasis on user experience.",
            "rating": "4.4/5",
            "locations": ["Noida", "Bangalore"]
        }
    ]
}

def get_companies_by_skills(skills, job_category=""):
    """
    Recommend companies based on skills and job category with detailed information.
    """
    recommendations = {}
    
    # Skill to category mapping with confidence scores
    skill_category_map = {
        "Machine Learning": ("AI_ML", 1.0),
        "AI": ("AI_ML", 1.0),
        "Deep Learning": ("AI_ML", 1.0),
        "NLP": ("AI_ML", 0.9),
        "TensorFlow": ("AI_ML", 1.0),
        "PyTorch": ("AI_ML", 1.0),
        "React": ("MERN_FULLSTACK", 1.0),
        "Node.js": ("MERN_FULLSTACK", 1.0),
        "MongoDB": ("MERN_FULLSTACK", 1.0),
        "Full Stack": ("MERN_FULLSTACK", 1.0),
        "JavaScript": ("MERN_FULLSTACK", 0.8),
        "Python": ("SOFTWARE_DEVELOPMENT", 0.7),
        "Java": ("SOFTWARE_DEVELOPMENT", 0.8),
        "Data Science": ("DATA_SCIENCE", 1.0),
        "AWS": ("DEVOPS_CLOUD", 1.0),
        "Docker": ("DEVOPS_CLOUD", 0.9),
        "Kubernetes": ("DEVOPS_CLOUD", 1.0),
        "Security": ("CYBER_SECURITY", 1.0),
        "Android": ("MOBILE_APP_DEVELOPMENT", 1.0),
        "iOS": ("MOBILE_APP_DEVELOPMENT", 1.0),
        "Blockchain": ("BLOCKCHAIN", 1.0),
        "UI Design": ("UI_UX_DESIGN", 1.0),
        "UX Design": ("UI_UX_DESIGN", 1.0),
        "Figma": ("UI_UX_DESIGN", 0.9)
    }
    
    # Convert skills to strings for matching
    skills_str = [str(skill).lower() for skill in skills]
    
    # Determine which categories to recommend based on skills
    categories_to_recommend = {}
    
    for skill in skills_str:
        for key, (category, confidence) in skill_category_map.items():
            if key.lower() in skill:
                if category not in categories_to_recommend:
                    categories_to_recommend[category] = []
                categories_to_recommend[category].append(confidence)
    
    # Sort categories by average confidence
    categories_to_recommend = dict(sorted(
        categories_to_recommend.items(),
        key=lambda x: sum(x[1]) / len(x[1]),
        reverse=True
    ))
    
    # If no categories matched, recommend based on job category or default
    if not categories_to_recommend:
        if job_category and job_category in COMPANY_DATABASE:
            categories_to_recommend = {job_category: [1.0]}
        else:
            # Return top categories with high-demand roles
            categories_to_recommend = {
                "SOFTWARE_DEVELOPMENT": [0.8],
                "DATA_SCIENCE": [0.7],
                "MERN_FULLSTACK": [0.7]
            }
    
    # Build recommendations with detailed company info
    for category in categories_to_recommend.keys():
        if category in COMPANY_DATABASE:
            # Get top 4 companies per category
            recommendations[category] = COMPANY_DATABASE[category][:4]
    
    return recommendations