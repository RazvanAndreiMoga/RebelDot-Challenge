from rapidfuzz import process, fuzz

def find_best_local_match(user_question, faq_list):
    """
    Returns the best matching FAQ object from faq_list based on string similarity.
    If no match is above threshold, returns None.
    """
    questions = [faq.question for faq in faq_list]
    best_match, score, idx = process.extractOne(
        user_question, questions, scorer=fuzz.token_sort_ratio
    )
    if score >= 60:  # similarity threshold
        return faq_list[idx]
    return None
