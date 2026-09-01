# ai-engineering-notes-kritikanchan97

ai-engineering-interview-questions/amitshekhariitbhu

RAG-Amazon Bedrock.ipynb / Sandesh-hase

# Transformer Architecture

# Why Was the Transformer Needed?

Before the Transformer, models processed words one by one, in order - like reading a sentence from left to right, one word at a time.

This had two big problems:

Problem 1: Forgetting. As sentences got longer, the model would start forgetting earlier words. By the time it reached the 50th word, its memory of the 1st word was very weak.

Problem 2: Slowness. Because words were processed one after another, the 2nd word had to wait for the 1st word to finish, the 3rd word had to wait for the 2nd, and so on. This was very slow.

So, here comes the Transformer to the rescue. It processes all input tokens at the same time and lets every token look at every other token directly.

# The Architecture Has Two Halves
The original Transformer has two main halves:

The Encoder - this half reads and understands the input
The Decoder - this half generates the output
Think of it like a conversation between a reader and a writer. The reader (encoder) reads a document carefully and creates detailed notes. The writer (decoder) uses those notes to write a new document. The reader focuses on understanding. The writer focuses on producing.

# Encoder Block Steps:
1. Input Embedding & Positional Encoding: Converts input tokens into vectors and adds position data.
2. Multi-Head Self-Attention: Lets each token look at all other tokens in the input sequence.
3. Add & Norm: Applies residual connection and layer normalization.
4. Position-wise Feed-Forward Network: Processes each vector through a fully connected network.
5. Add & Norm: Applies a second residual connection and layer normalization

# 1. Input Embedding & Positional Encoding:

The model does not understand words. It only understands numbers. So, the very first step is to convert words into numbers.

This happens in two stages:

Tokenization: The input text is split into small pieces called tokens. A token can be a word, part of a word, or even a single character. For the sake of understanding, let's treat each word as one token.

"I love learning" becomes three tokens: "I", "love", "learning".

Embedding: Each token is then converted into a vector of numbers called an embedding. An embedding is like a digital fingerprint for a word. Words with similar meanings get similar fingerprints.

For example, "happy" and "joyful" would have very similar embeddings because they mean almost the same thing. But "happy" and "car" would have very different embeddings because they are unrelated.

# Positional Encoding:

But, here is the catch. The encoder processes all input tokens at the same time - not one by one. This is great for speed, but it means the model has no idea which word comes first, second, or third.

"I love AI" and "AI love I" would look the same to the model. But they mean very different things.

Positional Encoding solves this. It adds a vector of numbers to each embedding that represents the position of the word. The 1st word gets a different position signal than the 2nd word, and so on.

Think of it like seat numbers in a theater. Even if all the audience members arrive at the same time, their seat numbers tell us exactly where each person is supposed to sit. Positional encoding is the seat number for each word.

After this step, the positional encoding numbers are combined into the embedding itself through addition. So, each token now carries a single vector of numbers that encodes both what the word means and where it sits in the sentence.

# The attention Mechanism:

This is the heart of the Transformer. The attention mechanism is the single most important idea that makes everything work.
Attention allows each word to look at every other word in the sentence and decide how much focus to give to each one.

Let's take the sentence: "The cat sat on the mat because it was tired."

When the model processes the word "it", it needs to figure out what "it" refers to. Is it the cat? Is it the mat? The attention mechanism helps the model focus more on "cat" and less on "mat" because "cat" is more relevant to "it" in this context.

How Attention Works
Each word is converted into three things:

Query (Q) - what this word is looking for
Key (K) - what this word can offer
Value (V) - the actual information this word carries

The process works like this:

First, each word uses its Query to compare with the Keys of all other words using a dot product. This produces attention scores - numbers that tell the model how relevant each pair of words is.
hen, these scores are scaled down (divided by √dₖ) to keep them in a manageable range. After scaling, the scores are normalized using softmax so they become probabilities that add up to 1. Finally, the model collects a weighted mix of the Values based on these probabilities.

The result is that every word now carries information not just about itself, but about the words most relevant to it. The word "it" now carries a strong signal from "cat" because the attention mechanism figured out the connection.

In simple words, attention lets each token borrow useful information from other relevant tokens before moving to the next layer.

# 2. Multi-Head Attention:

The Transformer does not run attention just once. It runs it multiple times in parallel - each time from a different perspective. This is called multi-head attention.

Think of it like a team of editors reviewing an article. One editor checks for grammar, another checks for factual accuracy, and another checks for flow. Each editor looks at the same text but focuses on something different. Together, they provide a complete review.

Each head in multi-head attention focuses on a different type of relationship between words. One head focuses on subject-verb connections. Another head focuses on which adjective describes which noun. The outputs of all heads are combined to give the model a rich understanding of the text.

# 3. Add & Norm: Applies residual connection and layer normalization:

Inside each layer (Multi-Head Self-Attention, Feed-Forward Neural Network), there are two more important pieces that help the Transformer learn effectively.

1. Residual Connection (Skip Connection):

- After each sub-layer (attention or feed-forward network), the original input to that sub-layer is added back to the output.
- Think of it like taking notes in a class. Even after the teacher adds new information, we keep our original notes and combine the new information with them.
- This prevents the model from losing important information as data passes through many layers.

In simple words, the output of each sub-layer is: output = sub-layer(input) + input.


2. Layer Normalization:

- After each residual connection, the numbers are normalized - adjusted so they stay in a stable range.
- This prevents the numbers from becoming too large or too small as they pass through many layers. It keeps the training process stable and smooth.
- These two pieces are present in every single layer of both the encoder and decoder.


# Stacking Multiple Layers

- The Transformer does not use just one such layer. It stacks multiple layers on top of each other, one after another. This is where the real power comes from.
- Each of these layers is also called a Transformer block. So when we say "the model has 96 layers", it means the model has 96 Transformer blocks stacked one    after another. Each block has its own multi-head attention sub-layer and its own feed-forward sub-layer.

## Note: This stacking is different from multi-head attention. Multi-head attention runs many attention heads in parallel inside a single attention sub-layer. Stacking layers, on the other hand, places full Transformer blocks one after another in sequence, so the output of one layer becomes the input of the next layer.


## Feed Forward Network:

- After the attention mechanism processes the words, the output passes through a feed-forward network.
- Think of it as a refinement step. If attention is about understanding relationships between words, the feed-forward network is about deepening the understanding of each word individually.
- It takes the enriched representation from attention and processes it further - sharpening the signal and removing noise. Every word passes through the same feed-forward network independently.

## Decoder Block Steps:
1. Output Embedding & Positional Encoding: Converts target tokens shifted right into vectors.
2. Masked Multi-Head Self-Attention: Prevents tokens from looking at future tokens during training.
3. Add & Norm: Applies residual connection and layer normalization.
4. Encoder-Decoder Cross-Attention: Connects the decoder to the final output of the encoder to focus on relevant input parts.
5. Add & Norm: Applies residual connection and layer normalization.
6. Position-wise Feed-Forward Network: Processes the vectors further.
7. Add & Norm: Final normalization step.
8. Linear & Softmax Layers (After final decoder block): Converts vectors into probabilities for the next output token.


# 2. Mask Attention:

- Masked Multi-Head Self-Attention is the first layer in the Transformer decoder.
- Its job is to help the decoder focus only on the current word and the previous words, not the future words.
- This is called masking.

# Why do we use masking?

When the decoder is generating a sentence, it should not know the future words.

For example, if the sentence is: "I love AI"

Predicting Word	               Words the Decoder Can See                  Words the Decoder Cannot See
I	                             I                                          love, AI
love                           I, love                                    AI
AI	                           I, love, AI                                None

## Why is it called Multi-Head?

- The decoder uses multiple attention heads.
- Each attention head learns different relationships between words.

For example:

- One head may focus on nearby words.
- Another head may focus on important words earlier in the sentence.
- Another head may learn grammar.

The outputs of all heads are combined to get a better understanding of the sentence.


# 4. Encoder-Decoder Cross-Attention:

- Cross Attention is a mechanism where one sequence looks at a different sequence, using its own Queries against the Keys and Values of the other sequence.
- In simple words, Cross Attention = Cross + Attention. The word "Cross" means the information crosses over from one sequence to another.
- The word "Attention" means the model decides how much it should focus on each part of the other sequence.
- So, one sequence asks the questions, and a different sequence provides the answers.

# Why do we need Cross Attention?

Suppose we are a student writing an exam answer. We have our own thoughts in our head (this is one sequence). We also have a reference book open on the table (this is another sequence). While writing each line of our answer, we look at our own thoughts (Query) and check the reference book (Key and Value) to pick up the relevant information.

That is exactly what Cross Attention does in a model. One sequence is reading from another sequence.
So, Cross Attention lets the output sequence read from the input sequence at every step.

## Query, Key, and Value in Cross Attention

For each word the decoder is generating, Cross Attention needs to answer two questions:

- Which tokens of the input sequence are important for me?
- How much should I focus on each of them?
- To answer these questions, we create three vectors:

Query (Q): what the decoder is looking for at the current step.
Key (K): what each input token offers.
Value (V): the actual information each input token carries.

The word "Cross" in Cross Attention comes from one very important fact:

- "Query comes from one sequence, and Key and Value come from a different sequence."

This is what makes it "Cross" Attention. The two sequences are different, but one is attending to the other.

## Note: This is the key difference between Self Attention and Cross Attention. In Self Attention, all three (Q, K, V) come from the same sequence. In Cross Attention, Q comes from one sequence, while K and V come from a different sequence.

## 8. Linear & Softmax Layers (After the Final Decoder Block)

- After the decoder finishes processing, it produces a vector (a list of numbers) for the current position.
- The model cannot directly predict a word from this vector. So it uses two final layers:

1. Linear Layer
2. Softmax Layer

# Step 1: Linear Layer

The Linear Layer converts the decoder's output vector into scores for every word in the vocabulary.

Suppose the vocabulary contains only four words:

I
am
student
teacher

The decoder outputs a vector.

The Linear Layer converts it into scores like this: These are just scores. They are not probabilities yet.

Word	     Score
I	         1.2
am	       2.5
student	   5.8
teacher	   0.9

# Step 2: Softmax Layer: The Softmax Layer converts these scores into probabilities (values between 0 and 1).

Example:

Word	          Probability
I	              0.02 (2%)
am	            0.08 (8%)
student	        0.85 (85%)
teacher	        0.05 (5%)

- The probabilities always add up to 1 (100%).
- The model chooses the word with the highest probability.

# So the next predicted word is: student

# Example: 

Suppose the decoder has generated:

I am a

Now it wants to predict the next word.

- The decoder produces a vector.
- The Linear Layer gives scores for every word.
- The Softmax Layer converts the scores into probabilities.
- The word with the highest probability is selected.

# Final output: I am a student












