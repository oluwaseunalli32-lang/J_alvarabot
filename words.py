import random

WORDS = [
    {
        "word": "ephemeral",
        "definition": "Lasting for a very short time.",
        "example": "The beauty of cherry blossoms is ephemeral.",
        "synonyms": ["temporary", "transient", "fleeting"]
    },
    {
        "word": "ubiquitous",
        "definition": "Present, appearing, or found everywhere.",
        "example": "Smartphones have become ubiquitous in modern life.",
        "synonyms": ["omnipresent", "universal", "pervasive"]
    },
    {
        "word": "meticulous",
        "definition": "Showing great attention to detail; very careful and precise.",
        "example": "She was meticulous in her research, checking every source.",
        "synonyms": ["thorough", "diligent", "painstaking"]
    },
    {
        "word": "altruistic",
        "definition": "Showing a selfless concern for the well-being of others.",
        "example": "His altruistic deeds earned him the community's admiration.",
        "synonyms": ["selfless", "benevolent", "charitable"]
    },
    {
        "word": "benevolent",
        "definition": "Well-meaning and kindly.",
        "example": "The benevolent teacher always helped struggling students.",
        "synonyms": ["kind", "generous", "compassionate"]
    },
    {
        "word": "cacophony",
        "definition": "A harsh, discordant mixture of sounds.",
        "example": "The cacophony of street traffic made it hard to concentrate.",
        "synonyms": ["din", "racket", "noise"]
    },
    {
        "word": "diligent",
        "definition": "Having or showing care and conscientiousness in one's work or duties.",
        "example": "She was a diligent student who studied every evening.",
        "synonyms": ["industrious", "assiduous", "persevering"]
    },
    {
        "word": "eloquent",
        "definition": "Fluent or persuasive in speaking or writing.",
        "example": "The president gave an eloquent speech that moved the audience.",
        "synonyms": ["articulate", "expressive", "fluent"]
    },
    {
        "word": "frugal",
        "definition": "Sparing or economical with regard to money or food.",
        "example": "He led a frugal lifestyle, saving money for travel.",
        "synonyms": ["thrifty", "economical", "prudent"]
    },
    {
        "word": "gregarious",
        "definition": "Fond of company; sociable.",
        "example": "Her gregarious nature made her popular at parties.",
        "synonyms": ["sociable", "outgoing", "convivial"]
    },
    {
        "word": "haphazard",
        "definition": "Lacking any obvious principle of organization.",
        "example": "The books were piled in a haphazard manner on the shelf.",
        "synonyms": ["random", "disorganized", "chaotic"]
    },
    {
        "word": "intrepid",
        "definition": "Fearless; adventurous.",
        "example": "The intrepid explorer ventured into the deep jungle.",
        "synonyms": ["brave", "courageous", "daring"]
    },
    {
        "word": "jubilant",
        "definition": "Feeling or expressing great happiness and triumph.",
        "example": "The team was jubilant after winning the championship.",
        "synonyms": ["joyful", "elated", "ecstatic"]
    },
    {
        "word": "kaleidoscopic",
        "definition": "Having complex patterns of colors; changing frequently.",
        "example": "The festival was a kaleidoscopic display of lights and music.",
        "synonyms": ["colorful", "variegated", "multifaceted"]
    },
    {
        "word": "labyrinthine",
        "definition": "Complicated; confusing; like a maze.",
        "example": "The old building had a labyrinthine corridor system.",
        "synonyms": ["maze-like", "complex", "convoluted"]
    },
    {
        "word": "mellifluous",
        "definition": "Sweet or musical; pleasant to hear.",
        "example": "Her mellifluous voice captivated the audience.",
        "synonyms": ["melodious", "harmonious", "dulcet"]
    },
    {
        "word": "nefarious",
        "definition": "Wicked or criminal.",
        "example": "The villain devised a nefarious plan to take over the city.",
        "synonyms": ["evil", "villainous", "heinous"]
    },
    {
        "word": "obstinate",
        "definition": "Stubbornly refusing to change one's opinion or course of action.",
        "example": "He was obstinate and wouldn't listen to any advice.",
        "synonyms": ["stubborn", "headstrong", "unyielding"]
    },
    {
        "word": "pragmatic",
        "definition": "Dealing with things sensibly and realistically.",
        "example": "We need a pragmatic approach to solve the problem.",
        "synonyms": ["practical", "realistic", "sensible"]
    },
    {
        "word": "quintessential",
        "definition": "Representing the most perfect example of a quality or class.",
        "example": "He is the quintessential gentleman.",
        "synonyms": ["perfect", "ideal", "exemplary"]
    }
]

def get_random_word():
    return random.choice(WORDS)

def find_word(word):
    """Return word entry if exists, else None."""
    word_lower = word.lower().strip()
    for entry in WORDS:
        if entry["word"].lower() == word_lower:
            return entry
    return None

def get_random_quiz_options(correct_word_entry, num_options=4):
    """Return a list of dicts for quiz options (one correct, others random)."""
    correct = correct_word_entry["definition"]
    # Get random other definitions
    other_words = [w for w in WORDS if w["word"] != correct_word_entry["word"]]
    random.shuffle(other_words)
    options = [correct_word_entry] + other_words[:num_options-1]
    random.shuffle(options)
    return options
