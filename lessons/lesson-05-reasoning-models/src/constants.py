GEMINI_API_KEY = "AIzaSyCgWYGWiJ07fsIUOIMSdZZjAlUAm2hE4v0"

GEMINI_MODEL_NAME = "gemini-2.0-flash"

SUPPORTED_FORMATS = ["json", "yaml", "markdown", "text", "html"]

DEFAULT_MIN_COUNT = 3

STOPWORDS = [
    "the", "and", "of", "to", "a", "in", "is", "it", "that", "for",
    "on", "with", "as", "was", "at", "be", "this", "have", "from",
    "or", "by", "not", "but", "what", "all", "were", "we", "when",
    "your", "said", "there", "use", "an", "each", "which", "she",
    "do", "how", "their", "if", "will", "up", "other", "about",
    "out", "many", "then", "them", "these", "so", "some", "her",
    "would", "make", "like", "him", "into", "time", "has", "look",
    "two", "more", "write", "go", "see", "number", "no", "way",
    "could", "people", "my", "than", "first", "water", "been",
    "call", "who", "oil", "its", "now", "find", "long", "down",
    "day", "did", "get", "come", "made", "may", "part", "i", "you",
    "he", "they", "are", "can", "had", "one", "our", "just", "me"
]

PUNCTUATION_BLACKLIST = [".", "!", ",", "?", ";", ":", "'", '"', "-", "(", ")", "[", "]", "{", "}", "/", "\\", "|", "@", "#", "$", "%", "^", "&", "*", "+", "=", "~", "`", "<", ">"]