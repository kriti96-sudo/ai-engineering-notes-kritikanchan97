## Self-introduction:

Hi, my name is Kriti Kanchan, and I have around 4 years of professional experience in the IT and data domain.

Currently, I’m working at HCL Technologies as a Senior Software Engineer for the USAA Bank client. I started my journey at HCL working on a Data Engineering project,
where I worked with technologies like Snowflake, dbt, Oracle, SQL Server, Python, AWS S3, and Linux. I was involved in data pipelines, data validation and profiling, 
API data extraction, data modeling, CI/CD activities, and production support.

After that, I moved to the Enterprise team under the SDM-Discovery / Protect team, where I currently focus on automation and Agentic AI solutions using MCP configuration
with GitLab, use GitHub Copilot to create agents. Currently, I’m also researching the implementation of RAG technology using AWS Bedrock services for AI-powered 
solutions.

Previously, I worked at Learnbay as a Data Analyst on a one-year contractual role. I worked on data analysis and machine learning projects, where I developed a 
machine learning-based trend analysis system to identify business trends and support forecasting. I also worked on NLP-based sentiment analysis to extract insights 
from customer feedback. In addition, I monitored business and product KPIs, prepared daily performance reports, performed data analysis based on business requirements, and presented insights and project demos to stakeholders.

Before Learnbay, I worked at Cordlife India as a part of data quality team, where I collaborated with cross-functional teams,  monitored data accuracy using CRM and 
Nagios, created Power BI dashboards, and handled customer escalations by identifying root causes and providing solutions.

Overall, my experience combines Data Engineering, Data Analytics, and AI/ML, with a strong focus on automation and emerging AI technologies.


## project explanation: Learnbay

"My role was not just limited to analyzing data. I first understood the business requirement, identified the relevant data sources and KPIs, 
performed data cleaning and exploratory analysis, and then developed the required analytical or machine learning solution. For the trend analysis project, 
I worked on identifying patterns in historical business data and supporting forecasting. For sentiment analysis, I worked with customer feedback and used NLP 
techniques to derive meaningful insights. I also prepared daily KPI reports and presented my findings and project demos to stakeholders."

## project explanation: Cordlife:

- At Cordlife India, I was of data quality team, where I primarily worked with medical insurance-related data.
- My main responsibility was to perform data validation based on predefined business rules, quality guidelines, and process requirements.
- I validated records for completeness, accuracy, consistency, and adherence to the defined guidelines.
- Whenever I identified missing, incorrect, or inconsistent information, I flagged the exceptions, investigated the issue, and coordinated with the relevant teams for resolution.
- After corrections were made, I also performed re-validation to ensure the data met the required standards.
- I was also involved in maintaining audit documentation. I maintained the required validation records, supporting documents,
- and evidence of the checks performed so that the process could be properly tracked and reviewed during audits.
- Along with this, I used CRM systems to track records, monitored data-related activities using Nagios, and created Power BI reports and dashboards for monitoring and reporting.

## "How would you design a RAG solution using AWS Bedrock?"
Know this architecture:

Documents → S3 → chunking → embeddings → vector store → retrieval → Bedrock LLM → response

Explain:

- I would first store the source documents in S3. The documents would be processed and split into appropriate chunks. 
- I would generate embeddings for those chunks and store them in a vector database. When a user asks a question,
- I would convert the query into an embedding, retrieve the most relevant chunks, and provide those chunks as context to the Bedrock foundation model.
- The model would then generate a response grounded in the retrieved information."

Be prepared for follow-ups on:

- Chunk size
- Chunk overlap : Overlap helps prevent important information from being split between two chunks.
- Embeddings
- Vector databases
- Similarity search: Similarity search is a technique used in RAG systems to find the pieces of information that are most relevant to a user's question.

Simple example:

Suppose your knowledge base contains these three chunks:

- Chunk 1: "Employees are entitled to 20 days of annual leave."
- Chunk 2: "Employees can request medical insurance reimbursement."
- Chunk 3: "The company provides laptops to new employees."
- Metadata filtering

User asks:

"How many annual leave days do employees get?"

- The system converts the question into an embedding vector.
- It has already converted each document chunk into vectors.
- imilarity search compares the question vector with the chunk vectors and finds that: Question ↔ Chunk 1 = high similarity
  



- Hallucination
- RAG evaluation
- Access control
- Cost
- Latency

  ## Latency:

  - Latency can come from retrieval, LLM inference, network calls, or application code, so you first identify the bottleneck.
  - A typical RAG request looks like:

User Query → Embedding → Vector Search → Retrieve Chunks → LLM → Response

You can optimize each stage.

- Instead of retrieving 20–30 chunks, start with a smaller Top-K, such as 3–5, and evaluate the quality.
- Reduce unnecessary LLM calls
- LLM → tool → LLM → tool → LLM - you may have significant latency.
- Design the agent so that it makes only the necessary tool calls and avoids unnecessary reasoning loops.

- Reduce prompt size: Don't send the entire conversation or entire documents to the model.

Use:

- Relevant chunks only
- Conversation summarization
- Metadata filtering

## "What if your RAG system gives an incorrect answer?"
Strong answer:

- I would first determine whether the problem is in retrieval or generation.
- If the correct document wasn't retrieved, I would investigate chunking, embeddings, similarity thresholds, metadata filters, and the retrieval strategy. '
- If the correct context was retrieved but the model still generated an incorrect answer, I would investigate the prompt, context formatting, model behavior, and generation parameters.
- I would also add evaluation datasets and metrics to systematically measure retrieval and answer quality."


## How do you reduce hallucination in RAG?"
Mention:

- Better chunking
- Better embeddings
- Top-K tuning
- Similarity threshold
- Strong system prompt
- Tell model to answer only from retrieved context
- Citation/source references
- "I don't know" fallback

## What is Top-K tuning?

"Top-K means how many relevant chunks we want to get from the database for one question."

For example:

"If K is 5, the system will get the top 5 most relevant chunks from the vector database."

## Why do we tune K?

"If K is too low, we may miss important information. If K is too high, we may get unnecessary information, which can increase latency and cost."

## How do we choose K?

"We try different values like 3, 5, or 10 and check which one gives the best answer with good speed and accuracy."

Easy example:

User asks:

"What is the leave policy?"

The database has 1,000 chunks.

- K = 3 → Get top 3 relevant chunks
- K = 5 → Get top 5 relevant chunks
- K = 10 → Get top 10 relevant chunks
- We test these values and choose the one that gives the best answer without adding unnecessary information.

## What is Metadata Filtering?

Metadata filtering means using extra information about a document to find only the relevant data.

In a RAG system, every document/chunk can have metadata such as:

Document name, Department, Date, Document type, Country, Access level, Product name

# Simple example
Suppose your database has company policy documents from different departments:

- Document 1 → HR → Leave Policy
- Document 2 → Finance → Expense Policy
- Document 3 → IT → Security Policy

User asks:

"What is the HR leave policy?"

Instead of searching all documents, we can filter:

department = "HR", Then similarity search happens only on the HR documents.

Metadata filtering can:

- Improve accuracy — search only relevant documents.
- Reduce noise — avoid unrelated chunks.
- Improve speed — search a smaller set of data.
- Improve security — users can access only documents they are allowed to see.
























  












