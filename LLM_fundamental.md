## What is tokenization in LLMs?

- When we type a sentence like "I love teaching AI", we see words. But a model does not understand words directly. It works with numbers.
- So, the first step is to break the text into small pieces called tokens. Each token is then converted into a number.
- This process of breaking text into tokens is called tokenization.
- Think of it like a chocolate bar. The full bar is the sentence. Each small part you break off is a token. The model processes multiple tokens at a time.

  ## Types of tokenization:

  1. Word-Level Tokenization:
     The simplest idea is to treat each word as one token.
     For the sentence "I love teaching", the tokens would be: "I", "love", "teaching".

  2. Character-Level Tokenization:
     The other extreme is to treat each character as one token.
     For the sentence "I love", the tokens would be: "I", " ", "l", "o", "v", "e".

But the issue with this approach is that the tokens are too small. The model has to process many more tokens for the same text. A 10-word sentence can become 50+ tokens. This makes training very slow and makes it harder for the model to understand meaning - because a single character like "l" carries very little meaning on its own.

We needed a solution that gives us the best of both worlds - not too big, not too small. So, here comes BPE to the rescue.

3. Byte Pair Encoding (BPE):

- BPE (Byte Pair Encoding) is a tokenization algorithm that breaks text into pieces that are somewhere between characters and words.
- It works by repeatedly finding the most common pair of adjacent tokens and merging them into one.
- So, BPE starts with individual characters and keeps merging the most frequent pairs until it builds up a vocabulary of common pieces - called subwords.
- These subwords can be full words (like "the"), parts of words (like "ing", "un", "tion"), or even single characters.

## Note: 
Think of it like learning shorthand. When you first start taking notes, you write every letter. But over time, you notice that some combinations appear very often - like "ing" or "tion". So, you create shortcuts for them. BPE does the same thing automatically.


























