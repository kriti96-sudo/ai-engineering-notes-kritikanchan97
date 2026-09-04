## Write a python function to parse a large JSON log file and extract only entries where "status" == "error". Optimize for memory efficiency.
import json

def error_logs(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                log = json.loads(line)
                if log.get("status") == "error":
                    yield log
            except json.JSONDecodeError:
                continue
# usage:

for error in error_logs("large.log"):
    print(error)

              
## Given a list of sentences, write Python code to tokenize and count word frequencies, ignoring stopwords.

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download("punkt")
nltk.download("stopwords")

def word_frequencies(sentences):
    stop_words = set(stopwords.words("english"))
    words = []

    for sentence in sentences:
        tokens = word_tokenize(sentence.lower())
        words += [w for w in tokens if w.isalpha() and w not in stop_words]

     return Counter(words)

## Example:

sentences = [
    "This is a simple sentence.",
    "This sentence is very simple."
]

print(word_frequencies(sentences))


## Implement gradient descent from scratch to minimize a quadratic function

def gradient_descent(x, lr=0.1, iterations=20):
    for _ in range(iterations):
        gradient = 2 * x
        x -= lr * gradient
    return x

x = gradient_descent(10)
print("Minimum at:", x)
print("Function value:", x**2)


## Write a function to compute TF-IDF vectors for a set of documents without using scikit-learn.

""" TL;DR — What TF‑IDF does (simple): 
it scores how important a word is to a document in a collection by combining term frequency (TF) — how often the word appears in that document — 
with inverse document frequency (IDF) — how rare the word is across all documents. Common words get low scores; distinctive words get high scores.
"""
import math
from collections import Counter

def tfidf(documents):
    docs = [doc.lower().split() for doc in documents]
    n = len(docs)

    vocab = sorted(set(word for doc in docs for word in doc))
    vectors = []

    for doc in docs:
        counts = Counter(doc)
        vector = []

        for word in vocab:
            tf = counts[word] / len(doc)
            df = sum(word in d for d in docs)
            idf = math.log(n / (1 + df)) + 1
            vector.append(tf * idf)

        vectors.append(vector)

    return vocab, vectors

# Example:
    
docs = [
    "cat sat mat",
    "dog sat mat",
    "cat dog"
]

vocab, vectors = tfidf(docs)

print(vocab)
print(vectors)

## Build a simple feedforward neural network in NumPy to classify points in 2D space.

import numpy as np

# XOR-like 2D data
X = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[0], [1], [1], [0]])

np.random.seed(0)
W1 = np.random.randn(2, 4)
b1 = np.zeros((1, 4))
W2 = np.random.randn(4, 1)
b2 = np.zeros((1, 1))

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

for _ in range(10000):
    # Forward pass
    h = sigmoid(X @ W1 + b1)
    out = sigmoid(h @ W2 + b2)

    # Backpropagation
    error = out - y
    dW2 = h.T @ error
    db2 = error.sum(axis=0, keepdims=True)

    dh = error @ W2.T * h * (1 - h)
    dW1 = X.T @ dh
    db1 = dh.sum(axis=0, keepdims=True)

    # Update weights
    W2 -= 0.5 * dW2
    b2 -= 0.5 * db2
    W1 -= 0.5 * dW1
    b1 -= 0.5 * db1

# Predictions
pred = (out > 0.5).astype(int)
print(pred)


## Write Python code to implement cosine similarity between two embedding vectors.

import math

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two vectors a and b (lists or tuples).
    Returns a float in [-1, 1]. Handles zero vectors safely by returning 0.0.
    """
    # dot product
    dot = sum(x*y for x, y in zip(a, b))
    # norms
    norm_a = math.sqrt(sum(x*x for x in a))
    norm_b = math.sqrt(sum(y*y for y in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)

# Example
v1 = [1, 2, 3]
v2 = [4, 5, 6]
print(cosine_similarity(v1, v2))  # ~0.974631846


## Implement a mini transformer attention mechanism (scaled dot-product attention) using NumPy.

import numpy as np

def attention(Q, K, V):
    d = Q.shape[-1]

    # Scaled dot-product scores
    scores = Q @ K.T / np.sqrt(d)

    # Softmax
    exp = np.exp(scores - np.max(scores, axis=-1, keepdims=True))
    weights = exp / exp.sum(axis=-1, keepdims=True)

    # Weighted values
    return weights @ V, weights


# Example: 3 tokens, embedding size = 4
Q = np.random.randn(3, 4)
K = np.random.randn(3, 4)
V = np.random.randn(3, 4)

output, attention_weights = attention(Q, K, V)

print("Attention weights:\n", attention_weights)
print("Output:\n", output)

## core calculation is:
scores = QKᵀ / √d
weights = softmax(scores)
output = weightsV


## Implement a caching mechanism for API calls using decorators.
import functools
import requests

def cache(func):
    saved = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))

        if key not in saved:
            saved[key] = func(*args, **kwargs)

        return saved[key]

    return wrapper


@cache
def get_data(url):
    return requests.get(url).json()


print(get_data("https://api.example.com/data"))


##  Write a function that returns the number of tokens for a text given a tokenize(text) callable; avoid double tokenization.
## Assesses: API use, caching, simple optimization.

def token_count(text, tokenize):
    tokens = tokenize(text)
    return len(tokens)

# Example: 

def tokenize(text):
    return text.split()

print(token_count("Hello world from Python", tokenize))
# This calls tokenize(text) only once, avoiding double tokenization.

## Mini RAG retrieval step — Given doc embeddings and a query, return documents whose cosine similarity exceeds a threshold, sorted by score.

import numpy as np

def retrieve(docs, embeddings, query, threshold=0.7):
    query = np.array(query)
    scores = [
        np.dot(e, query) / (np.linalg.norm(e) * np.linalg.norm(query))
        for e in embeddings
    ]

    return sorted(
        [(doc, score) for doc, score in zip(docs, scores) if score >= threshold],
        key=lambda x: x[1],
        reverse=True
    )

# Example:
docs = ["Python", "RAG", "Cooking"]
embeddings = [
    [1, 0, 0],
    [0.9, 0.1, 0],
    [0, 0, 1]
]
query = [1, 0, 0]

print(retrieve(docs, embeddings, query, 0.8))


## write a python function to create chunks pf large document by using RAG

def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0

    while start < len(text):
        chunks.append(text[start:start + chunk_size])
        start += chunk_size - overlap

    return chunks


## write a python function for tokenization, embedding, attention mechanism (give attention score to each embedding vector) & then store to vector data base.

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def create_vector_db(text):
    # 1. Chunk document
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.create_documents([text])

    # 2. Create embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # 3. Store embeddings in vector DB
    db = FAISS.from_documents(chunks, embeddings)

    return db

## use:

text = open("document.txt", encoding="utf-8").read()

db = create_vector_db(text)

results = db.similarity_search("What is RAG?", k=3)

for r in results:
    print(r.page_content)


## write a python function to find indian mobile number & email id from user prompt.

import re

def extract(prompt):
    mobile = re.findall(r'(?<!\d)(?:\+91[- ]?)?[6-9]\d{9}(?!\d)', prompt)
    email = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', prompt)
    return {"mobile": mobile, "email": email}

print(extract("Call me at +91 9876543210 or test@gmail.com"))


'''
1.  List — Remove duplicates
Question: Remove duplicates from a list while preserving order.
'''
def remove_duplicates(nums):
    return list(dict.fromkeys(nums))

print(remove_duplicates([1, 2, 2, 3, 1, 4]))
# [1, 2, 3, 4]

'''List — Find second largest'''

def second_largest(nums):
    unique = list(set(nums))
    unique.sort()
    return unique[-2]

print(second_largest([10, 5, 8, 10, 3]))
# 8


'''
3. List — Find missing number
Question: Given [1,2,3,5], find the missing number.
'''

def missing_number(nums):
    n = len(nums) + 1
    return n * (n + 1) // 2 - sum(nums)

print(missing_number([1, 2, 3, 5]))
# 4

'''
5. List — Two Sum ⭐
Question: Find two numbers whose sum equals the target.
'''

def two_sum(nums, target):
    seen = {}

    for i, x in enumerate(nums):
        if target - x in seen:
            return seen[target - x], i
        seen[x] = i

print(two_sum([2, 7, 11, 15], 9))
# (0, 1)

'''
String Questions
6. Reverse a string ⭐
'''

def reverse_string(s):
    return s[::-1]

print(reverse_string("python"))
# nohtyp

'''
7. Check palindrome ⭐
'''
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))
# True

'''8. Count character frequency ⭐'''

from collections import Counter

def char_frequency(s):
    return Counter(s)

print(char_frequency("banana"))
# {'a': 3, 'n': 2, 'b': 1}

'''9. Find first non-repeating character'''
def first_unique(s):
    count = {}

    for c in s:
        count[c] = count.get(c, 0) + 1

    for c in s:
        if count[c] == 1:
            return c

print(first_unique("aabbcde"))
# c

'''10. Check anagram ⭐'''
def is_anagram(a, b):
    return sorted(a) == sorted(b)

print(is_anagram("listen", "silent"))
# True


'''11. Reverse words in a sentence'''

def reverse_words(s):
    return " ".join(s.split()[::-1])

print(reverse_words("I love Python"))
# Python love I

'''
List of Tuples
12. Sort list of tuples by second element ⭐
'''

data = [("A", 3), ("B", 1), ("C", 2)]

result = sorted(data, key=lambda x: x[1])

print(result)
# [('B', 1), ('C', 2), ('A', 3)]


'''13. Find tuple with maximum value'''

data = [("A", 10), ("B", 30), ("C", 20)]

print(max(data, key=lambda x: x[1]))
# ('B', 30)


''' 14. Convert list of tuples into dictionary'''

data = [("a", 1), ("b", 2), ("c", 3)]

result = dict(data)

print(result)
# {'a': 1, 'b': 2, 'c': 3}


'''
Dictionary Questions
15. Count word frequency ⭐
'''

def word_count(text):
    result = {}

    for word in text.split():
        result[word] = result.get(word, 0) + 1

    return result

print(word_count("python is easy python is powerful"))


'''16. Find key with maximum value ⭐'''

data = {"a": 10, "b": 30, "c": 20}

print(max(data, key=data.get))
# b


'''17. Merge two dictionaries'''
a = {"x": 1, "y": 2}
b = {"z": 3, "w": 4}

result = {**a, **b}

print(result)

'''18. Invert a dictionary'''

data = {"a": 1, "b": 2, "c": 3}

result = {v: k for k, v in data.items()}

print(result)
# {1: 'a', 2: 'b', 3: 'c'}


'''
Nested List Questions
19. Flatten a nested list ⭐
'''

Input:
[[1, 2], [3, 4], [5, 6]]

Output:
[1, 2, 3, 4, 5, 6]


def flatten(data):
    return [x for sublist in data for x in sublist]

'''22. Matrix transpose ⭐'''

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

result = [list(x) for x in zip(*matrix)]

print(result)
# [[1, 4], [2, 5], [3, 6]]
















































































