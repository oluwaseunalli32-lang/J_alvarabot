GRAMMAR_QUESTIONS = [
    {
        "question": "Which sentence is grammatically correct?",
        "options": [
            "She don't like apples.",
            "She doesn't like apples.",
            "She doesn't likes apples.",
            "She don't likes apples."
        ],
        "correct": 1
    },
    {
        "question": "Choose the correct form: I ______ to the store yesterday.",
        "options": ["go", "went", "gone", "going"],
        "correct": 1
    },
    {
        "question": "Which is the correct plural of 'child'?",
        "options": ["childs", "children", "childrens", "childes"],
        "correct": 1
    },
    {
        "question": "Choose the correct sentence:",
        "options": [
            "He has went to school.",
            "He has gone to school.",
            "He have gone to school.",
            "He gone to school."
        ],
        "correct": 1
    },
    {
        "question": "Which word is an adverb?",
        "options": ["quick", "quickly", "quickness", "quicken"],
        "correct": 1
    },
    {
        "question": "Choose the correct passive form: 'The cat chased the mouse.'",
        "options": [
            "The mouse was chased by the cat.",
            "The mouse is chased by the cat.",
            "The mouse chased by the cat.",
            "The mouse has chased by the cat."
        ],
        "correct": 0
    },
    {
        "question": "What is the past tense of 'teach'?",
        "options": ["teached", "taught", "tought", "teached"],
        "correct": 1
    },
    {
        "question": "Which sentence uses the subjunctive mood?",
        "options": [
            "If I was you, I would go.",
            "If I were you, I would go.",
            "If I am you, I would go.",
            "If I be you, I would go."
        ],
        "correct": 1
    },
    {
        "question": "Choose the correct article: He is ______ honest man.",
        "options": ["a", "an", "the", "none"],
        "correct": 1
    },
    {
        "question": "Which is a conjunction?",
        "options": ["and", "run", "quickly", "under"],
        "correct": 0
    }
]

def get_random_grammar_question():
    import random
    return random.choice(GRAMMAR_QUESTIONS)
