# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# def semantic_score(resume_text, job_desc):
#     vectorizer = CountVectorizer()
#     vectors = vectorizer.fit_transform([resume_text, job_desc])
#     score = cosine_similarity(vectors)[0][1]
#     return round(score * 100, 2)
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def semantic_score(resume_text, job_desc):
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform([resume_text, job_desc])
    score = cosine_similarity(vectors)[0][1]
    return round(score * 100, 2)
