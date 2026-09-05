## 1. What is langchain & its component & why use?

- LangChain acts as a framework around the LLM, helping us connect the model with external data, tools, and application logic.
- LangChain is an open-source framework for building applications powered by Large Language Models (LLMs) such as GPT, Claude, Gemini, etc.
- The main idea is that instead of calling an LLM directly with a prompt, LangChain provides building blocks to create a complete application around the LLM
- for example, connecting it to documents, databases, APIs, tools, memory, and agents.

Main components:

LLM/Chat Models – interact with models like GPT, Claude, Gemini.

Prompts – create reusable instructions for the LLM.

Chains – connect multiple steps/workflows together.

Retrievers – fetch relevant information from a knowledge base.

Vector Stores – store and search document embeddings.

Tools – allow the LLM to call APIs, databases, calculators, etc.

Agents – let the LLM decide which tools/actions to use.

Why use LangChain?
We use LangChain to simplify the development of LLM applications, especially RAG and AI agents, by providing reusable components for prompts, retrieval, 
tools, and workflows.

## 2. prompting techniques:

When the task is straightforward - like translating a sentence - the model already knows how to do it. No examples needed. That's zero-shot.

But what if we want the output in a very specific format? Something the model can't guess on its own. We give one example to show the format - and the model follows it. That's one-shot.

Now think about this - we want the model to classify bug priority as P0 or P2. This is our own custom system. The model has no idea what counts as P0 in our team. So we give it a few examples to learn the pattern. That's few-shot prompting.

Chain-of-Thought (CoT) Prompting: is a technique where we ask the model to write out its reasoning steps before giving the final answer.
In simple words, instead of asking for the answer directly, we ask the model to "think out loud" first.
A thought is one small reasoning step. A chain is many small steps linked together, one after another. 
So a Chain-of-Thought is a series of small reasoning steps that lead us to the final answer.

## What is RAG & RaG pipeline?
RAG (Retrieval-Augmented Generation) is a technique where we retrieve relevant information from our own knowledge base and provide it to the LLM as 
context before generating the answer.

It helps the LLM answer using company-specific or up-to-date information instead of relying only on its training data.

# Rag Pipeline:

1. Data ingestion:
   
   Documents → Chunking → Embeddings → Vector Database

3. User query:
   
   User Question →   Query Embedding   →  Vector Database Search  → Relevant Chunks →  Prompt + Context →  LLM →  Answer  

Why use RAG?
- To answer questions using private/company data
- Reduce hallucinations by providing relevant context
- Update knowledge without retraining the LLM

## How do you develop an architecture for a GenAI project?

“First, I understand the business requirement and decide whether we need a simple LLM application, RAG, or an agent-based system. 
Then I select the model, design the data pipeline, define retrieval and prompt strategy, and finally design deployment, security, monitoring, and evaluation.”

Key things I consider
- Use case: What problem are we solving?
  
- LLM: Which model gives the required quality, latency, and cost?
  
- Data: Do we need RAG and a vector database?
  
- Prompt: How should the model be instructed?
  
- Tools/Agents: Does the model need to interact with APIs or databases?
  
- Security: Authentication, authorization, PII protection, prompt-injection protection.
  
- Evaluation: How do we measure accuracy, hallucination, and response quality?
  
- Deployment: AWS/cloud architecture, CI/CD, scaling, and availability.
  
- Monitoring: Latency, token usage, cost, errors, and model quality.

## evaluation of RAG using Graph dztabase etc
using tools such as RAGAS, LangSmith, DeepEval, or custom evaluation—and a graph database is usually not the evaluation tool itself.

Tools:

- RAGAS is commonly used specifically for RAG evaluation.
- LangSmith is useful for tracing, debugging, monitoring, and evaluating LLM/RAG pipelines.
- DeepEval provides automated evaluation metrics and testing for LLM applications.

Test Questions + Ground Truth
          ↓
          
       RAG Pipeline
          ↓
          
      Generated Answer
          ↓
          
     Evaluation Tool
          ↓
          
   Metrics / Score / Report

Important RAG metrics:

Faithfulness – Is the answer supported by the retrieved context?

Answer Relevance – Does the answer actually address the question?

Context Relevance – Did we retrieve relevant chunks?

Context Recall – Did we retrieve the important information needed to answer?

Correctness – Does the final answer match the expected answer?

Where does a Graph Database fit?

A graph database such as Neo4j can be used as the knowledge/retrieval layer, especially when relationships between entities are important.

For example:

Documents
   ↓
   
Entities + Relationships
   ↓
   
Graph Database
   ↓
   
Retrieve related information
   ↓
   
  LLM
   ↓
   
 Answer

## What us RAg What is inference engineering And how you deploy a model in production Using devops mlops

Inference engineering is the process of making model inference fast, reliable, scalable, and cost-efficient in production.

It includes:

- Model serving and APIs
- Latency optimization
- Batching and caching
- GPU/CPU optimization
- Quantization/model optimization
- Autoscaling
- Monitoring latency, errors, and cost
- Handling high concurrent traffic
For GenAI, it can also include prompt management, token optimization, guardrails, and model routing.

# How do you deploy a model to production using DevOps/MLOps?
I first develop and validate the model, then containerize it using Docker and store the image in a container registry. Using CI/CD, code changes automatically 
trigger testing, security checks, image building, and deployment. In production, I deploy the model using Kubernetes or a cloud service, configure autoscaling 
and load balancing, and monitor model performance, latency, errors, resource utilization, and cost. For MLOps, I also track model versions, datasets, experiments,
and model performance, and have a rollback strategy if the new model performs poorly.

DevOps = deploy and operate the application

MLOps = manage the ML/model lifecycle

## What is vector embedding and how u achieve it?
Vector embedding is a numerical representation of data that captures its semantic meaning. We generate embeddings using an embedding model, 
store them in a vector database, and use similarity search to retrieve semantically relevant information. This is commonly used in RAG systems.

Some commonly used embedding models are:

- OpenAI: text-embedding-3-small, text-embedding-3-large
- Google: text-embedding-005
- Cohere: embed-v4.0


 RAG , retrieval and a project that I have worked on  
 What is PCA 

## various methods used in Machine Learning and why their target usage for different scenarios

Method	Examples	When to use
Supervised Learning:	Linear Regression, Logistic Regression, Decision Trees, Random Forest, XGBoost,	When you have labeled data and want to predict an outcome

Unsupervised Learning:	K-Means, DBSCAN, PCA,	When you don't have labels and want to find patterns/groups

Semi-Supervised Learning:	Label propagation, pseudo-labeling,	When you have a small amount of labeled data + lots of unlabeled data

Reinforcement Learning:	Q-Learning, DQN, PPO	When an agent learns through actions, rewards, and feedback

Deep Learning:	CNN, RNN, Transformers	For complex/high-dimensional data such as images, speech, and text

Ensemble Learning:	Random Forest, XGBoost, LightGBM

## What is support vector in SVM? 
In SVM, support vectors are the training data points closest to the decision boundary. 
They are important because they determine the optimal hyperplane and maximum margin between the classes. 
If we remove or change these points, the decision boundary can change.

## Explain CNN & RNN?

# CNN: (Convolutional Neural Network)
CNN is a deep learning neural network designed primarily for processing grid-like data such as images. 
It automatically learns spatial features from the input, starting from simple features like edges and progressing to complex features like shapes and objects.

Main Components
1. Input Layer: Takes the image as a numerical matrix.
2. Convolution Layer: This is the most important CNN component.
A small filter/kernel slides over the image and performs mathematical operations to detect features.

Early layers may learn: Edges, Lines, Corners
Deeper layers learn: Shapes, Textures, Objects

3. ReLU Activation: introduces non-linearity - negative values become zero. This allows the network to learn complex patterns.

4. Pooling Layer: Pooling reduces the spatial size of feature maps while retaining important information.

Common types:

Max Pooling → takes the maximum value
Average Pooling → takes the average value

Benefits: Reduces computation, Reduces memory, Helps reduce overfitting, 

5. Flatten Layer: After convolution and pooling, the feature maps are converted into a one-dimensional vector.

6. Fully Connected / Dense Layer: The extracted features are passed to dense layers to make the final prediction.

7. Output Layer: For classification, the output could be probabilities.

# RNN — Recurrent Neural Network

RNN is a neural network designed for sequential or time-dependent data. 
It processes data one time step at a time and maintains a hidden state that carries information from previous time steps.
This makes RNNs useful when the order of the data matters.
 
Examples: Time-series forecasting, Speech processing, Sequence classification


## What is 300B Parameter in LLM ? 
300B parameters means the LLM contains approximately 300 billion learnable weights and biases. 
These parameters are adjusted during training to learn patterns and relationships in the data. 
A larger parameter count generally gives the model more capacity, but it also increases memory, computation, and inference cost.

## What are the types of libraries worked on NLP ?
NLTK – Tokenization, stemming, lemmatization, POS tagging, and other traditional NLP tasks.

spaCy – Fast NLP pipelines, NER, POS tagging, dependency parsing, etc.

Hugging Face Transformers – Pretrained Transformer models such as BERT, T5, and GPT-style models.

Gensim – Word embeddings and topic modeling; commonly used for Word2Vec and similar techniques.

Stanford NLP / CoreNLP – Traditional NLP processing and linguistic analysis.

scikit-learn – TF-IDF, Bag-of-Words, text classification, clustering, and traditional ML for NLP.

PyTorch / TensorFlow – Deep-learning frameworks used to build and train custom NLP models.

## What is the difference between deep learning, Machine Learning, Agentic AI & Gen AI?

Machine Learning (ML):

ML enables machines to learn patterns from data and make predictions or decisions without being explicitly programmed for every rule.

Deep Learning (DL):

Deep Learning is a subset of ML that uses multi-layer neural networks to learn complex patterns from large amounts of data.

Example: Image recognition, speech recognition, NLP.
CNNs, RNNs, LSTMs, and Transformers are examples of deep-learning architectures.

Generative AI (GenAI):

Generative AI refers to AI systems that can generate new content such as text, images, audio, video, or code based on learned patterns.

Agentic AI: 

Agentic AI refers to AI systems that can autonomously plan and execute multiple steps to achieve a goal, often using tools, APIs, databases, or other systems.

## What is stemming and Lemmatization ? and which would you prefer?

Stemming: 

Stemming reduces a word to its root form by removing prefixes or suffixes, usually without understanding the word's meaning.

Examples:

playing   → play

studies   → studi

connected → connect

It's fast, but the result may not be a valid word.

Lemmatization:

Lemmatization converts a word to its correct dictionary/base form (lemma) by considering the word's meaning and grammatical context.

Examples:

playing → play

studies → study

better  → good

It's generally more accurate but computationally more expensive than stemming.

Which would I prefer?
“I would prefer lemmatization when accuracy and meaningful language representation are important because it produces valid base words. 
I would use stemming when I need a faster and simpler preprocessing approach and exact linguistic accuracy is not critical.”

## Lets say that a persons chooses stemming over lemmatization what might be the reason ?

If someone chooses stemming over lemmatization, the main reason is usually speed and simplicity.
Possible reasons: 

Faster: Stemming uses simple rules, so it's computationally cheaper.

Less resource-intensive: Useful when processing millions of documents.

Good enough for search: For keyword matching or information retrieval, an exact dictionary word may not be necessary.

Simple implementation: Doesn't require linguistic analysis or context.

Real-time requirements: If preprocessing must be extremely fast, stemming can be preferable.

## Why do you use LLM model if you can fetch the required documents from vector database in RAG Approach ?

The vector database is responsible for retrieval, not reasoning or generation. In RAG, we use the vector database to retrieve relevant context, 
and then pass that context to the LLM. The LLM understands the question, uses the retrieved context, and generates the final grounded response.

Easy way to remember:

Vector DB = Find the information

LLM = Understand and communicate the information

# What is TF-IDF vectorizer explain?

TF-IDF (Term Frequency–Inverse Document Frequency) is a technique used in NLP to convert text into numerical vectors based on how important a word is within 
a document and across a collection of documents.

How it works
1. TF — Term Frequency

Measures how often a word appears in a document.

If "machine" appears many times in a document, its TF is higher.

2. IDF — Inverse Document Frequency

Measures how rare or unique the word is across all documents.

Common words like "the" get low importance, while rarer words get higher importance.

Example
Suppose we have:

Doc 1: "I like machine learning"

Doc 2: "I like deep learning"

Words like "learning" appear in both documents → lower IDF.

"machine" appears only in Doc 1 → higher IDF.

So TF-IDF gives more weight to words that are frequent in a particular document but uncommon across documents.


## Difference between logistic regression and linear regression and the examples

Linear Regression:

Linear regression predicts a continuous numerical value based on one or more input features.

Logistic Regression:

Logistic regression is primarily used for binary classification. It predicts the probability of an observation belonging to a class using the sigmoid function.

If probability > 0.5, we might classify it as Yes, otherwise No. The threshold can be changed depending on the business requirement.

## The accuracy metrics used for logistic regression and linear regression?

Logistic Regression — Classification
Common metrics:

Accuracy – percentage of correct predictions.

Precision – of predicted positives, how many are actually positive.

Recall – of actual positives, how many did we correctly identify.

F1 Score – balance between precision and recall.

ROC-AUC – measures how well the model separates the classes.

Log Loss – evaluates the quality of predicted probabilities.

Linear Regression — Regression

Common metrics:

MAE (Mean Absolute Error) – average absolute difference between actual and predicted values.

MSE (Mean Squared Error) – average squared error; penalizes large errors more.

RMSE (Root Mean Squared Error) – square root of MSE, in the same units as the target.

R² (R-squared) – indicates how much variance in the target is explained by the model.

MAPE – average percentage error, useful when target values are suitable for percentage-based comparison


## What is NER and how to custom train a NER model

NER (Named Entity Recognition) is an NLP technique used to identify and classify important entities in text into predefined categories.

Example:

"Apple hired John in Hyderabad."

Apple    → ORGANIZATION

John     → PERSON

Hyderabad → LOCATION

Common entities include PERSON, ORGANIZATION, LOCATION, DATE, MONEY, PRODUCT, etc.

## Difference between KNN and k means

KNN (K-Nearest Neighbors) is a supervised machine learning algorithm used for classification and regression, where it predicts a new data point based on 
the closest K labeled data points. On the other hand, K-Means is an unsupervised learning algorithm used for clustering, where it divides data into K groups 
or clusters based on similarity. 

In KNN, K represents the number of nearest neighbors, while in K-Means, K represents the number of clusters. For example, 
KNN can be used to predict whether a customer will churn, while K-Means can be used to segment customers into different groups without predefined labels.

## Tensorflow and keras models

TensorFlow is an open-source machine learning and deep learning framework developed by Google, used to build, train, evaluate, and deploy neural network models. 
Keras is a high-level deep learning API that provides a simpler way to build and train models, and it can run on top of TensorFlow.

import tensorflow as tf
from tensorflow import keras

You can use them for:

CNN → image classification, object detection, computer vision.

RNN/LSTM/GRU → time-series and sequential data.

NLP → text classification, sentiment analysis, sequence models

Deep learning regression/classification → when the problem is complex and traditional ML isn't sufficient.

## What is RAG and what does it entail?

RAG (Retrieval-Augmented Generation) is a technique that combines information retrieval with an LLM. 
Instead of asking the LLM to answer only from its trained knowledge, RAG first retrieves relevant information from an external knowledge base, 
such as company documents or a vector database, and then provides that information as context to the LLM to generate a grounded answer.

A typical RAG pipeline entails document ingestion, chunking, embedding generation, storing embeddings in a vector database, retrieving relevant chunks 
for a user query, adding those chunks to the prompt, and finally sending the prompt to the LLM to generate the answer.

# Can you explain in detail what rag design is?

                RAG Architecture

1. Data Ingestion                  2. Query / Retrieval
    ↓                               ↓
            
Documents                          User Question
   ↓
                                  ↓
Document Loader                  Query Embedding
   ↓
                                   ↓
Chunking                         Vector / Hybrid Search
   ↓
                                    ↓
Embedding Model                  Reranking
   ↓
                                     ↓
Vector Database  ←──────────── Relevant Chunks
                                        ↓
   
                                  Prompt + Context
                                        ↓
                                       LLM
                                        ↓
                                     Answer


## Can you explain the standard Object-Oriented Programming (OOP) concepts

Object-Oriented Programming (OOP) is a programming approach where we organize code around objects and classes, combining data and the functions that 
operate on that data.

The four main OOP concepts are:

Class: A blueprint or template used to create objects. It defines variables and methods.
Object: A real-world instance of a class that holds specific data and uses memory

1. Encapsulation
Encapsulation means bundling data and methods together inside a class and controlling access to the data.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

Here, __balance is protected from direct access, and we modify it through methods.

2. Inheritance
Inheritance allows one class to reuse and extend the properties and methods of another class.

allows a class (child class) to acquire properties and methods of another class (parent class). It supports hierarchical classification and promotes code reuse.

class Animal:

    def speak(self):
        print("Animal speaks")

class Dog(Animal):

    pass

Dog inherits from Animal.

3. Polymorphism
Polymorphism means the same interface or method can behave differently depending on the object.

means "same operation, different behavior." It allows functions or methods with the same name to work differently depending on the type of object they are acting upon.

class Dog:

    def speak(self):
        print("Bark")

class Cat:

    def speak(self):
        print("Meow")

Both have speak(), but the behavior is different. Polymorphism allows the same method to have different implementations.”

4. Abstraction
Abstraction means hiding implementation details and exposing only the essential functionality.
Abstraction hides the internal implementation details while exposing only the necessary functionality. It helps focus on "what to do" rather than "how to do it."

model.predict(data)
you don't need to know all the internal mathematical operations used to generate the prediction.

Easy way to remember
E-I-P-A

Encapsulation → Protect data

Inheritance → Reuse code

Polymorphism → Same interface, different behavior

Abstraction → Hide complexity

## Compare symmetric and asymmetric cryptography.
Symmetric encryption uses a single shared secret key for both encryption and decryption. 
It is fast and is typically used for encrypting large amounts of data. 
Asymmetric encryption uses a public-private key pair and is slower, but it solves the key-distribution problem and is commonly used for secure key exchange, 
authentication, and digital signatures. In real systems, both are often used together—for example, asymmetric cryptography establishes a secure session key, 
and symmetric encryption then encrypts the actual data.

## Multithreading & multiprocessing: 
Multithreading runs multiple threads within a single process and is mainly useful for I/O-bound tasks such as API calls and database operations. 
Multiprocessing runs multiple independent processes with separate memory and is better for CPU-bound tasks. In Python, multiprocessing is particularly useful 
for CPU-intensive parallel work because of the GIL.

## what is LLM quantization?

LLM quantization is a technique used to reduce the size and memory requirements of a large language model by representing its weights with fewer bits. For example, instead of using 16-bit precision, we can use 8-bit or 4-bit precision. This makes the model smaller, faster, and easier to run on limited hardware

## Why do we need quantization?”, say:

“Large language models require a lot of GPU memory. Quantization reduces the memory required, so we can run the model on cheaper or smaller GPUs, and sometimes get faster inference.”

#example:

“For example, a 7-billion-parameter model in FP16 may need around 14 GB just for the weights. With 4-bit quantization, it can come down to roughly 3.5 GB, although there is some additional memory overhead.”





What is confusion matrix, and what is true pos and false pos means

Difference between list and tuple

Difference between iloc and loc

How to read an excel file with sheet name 2 in pandas

# Can you describe Ridge regression and how it differs from standard linear regression?

# Explain supervised and unsupervised learning algorithms of your choice
Supervised learning — Random Forest
Unsupervised learning — K‑means clustering

## Explain file handling in Python.

## What are the different types of prompts?

## Describe scenarios you have encountered in project management and how you handled them.





































