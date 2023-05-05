from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer, PorterStemmer
from data import data

_tokenizer = RegexpTokenizer(r"\w+")
_lemmatizer = WordNetLemmatizer()
_stemmer = PorterStemmer()
_stopwords = stopwords.words("english")
_stopwords.remove("not")

def sequence_to_token(sequence: str, tokenization: str):
    tokens = [item for item in _tokenizer.tokenize(sequence.lower()) if item not in _stopwords]
    match tokenization:
        case "lemmatize":
            tokens = [_lemmatizer.lemmatize(token) for token in tokens]
        case "stem":
            tokens = [_stemmer.stem(token) for token in tokens]
    return tokens

def questions_to_sequece():
    sequence: str = ""
    for querys in data.querys: 
        for question in querys["questions"]:
            sequence += question + " "
    return sequence

def concat_iterables(*iterables):
    for iterable in iterables:
        yield from iterable

def one_hot_encode(ids: list, vocab_size: int):
    encoded = [0] * vocab_size
    if len(ids) <=0 :
        return encoded
    for _id in ids:
        encoded[_id] = 1
    return encoded

def get_stopwords():
    return ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']
