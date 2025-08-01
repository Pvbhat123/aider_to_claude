"""Constants for transcript analytics, including word blacklist."""

# Common words to exclude from frequency analysis
word_blacklist = {
    # Articles
    "a", "an", "the",
    
    # Pronouns
    "i", "you", "he", "she", "it", "we", "they", "me", "him", "her", "us", "them",
    "my", "your", "his", "her", "its", "our", "their", "mine", "yours", "ours", "theirs",
    "this", "that", "these", "those",
    
    # Prepositions
    "in", "on", "at", "by", "for", "with", "about", "against", "between", "into",
    "through", "during", "before", "after", "above", "below", "to", "from", "of",
    "up", "down", "out", "off", "over", "under", "again", "further",
    
    # Conjunctions
    "and", "or", "but", "if", "because", "as", "until", "while", "since", "unless",
    "although", "though", "whereas", "whether", "either", "neither", "nor", "so",
    
    # Common verbs
    "is", "am", "are", "was", "were", "be", "been", "being", "have", "has", "had",
    "do", "does", "did", "will", "would", "should", "could", "might", "must",
    "shall", "can", "may", "ought", "need", "used",
    
    # Common adverbs
    "then", "now", "here", "there", "when", "where", "why", "how", "all", "both",
    "each", "more", "most", "other", "some", "such", "only", "own", "same", "than",
    "too", "very", "just", "quite", "rather", "really", "still", "even", "also",
    "already", "however", "therefore", "thus", "hence", "moreover", "furthermore",
    
    # Other common words
    "yes", "no", "not", "what", "which", "who", "whom", "whose", "every", "any",
    "few", "more", "many", "much", "several", "one", "two", "three", "first",
    "last", "next", "something", "anything", "nothing", "everything", "someone",
    "anyone", "everyone", "no one", "somebody", "anybody", "everybody", "nobody"
}