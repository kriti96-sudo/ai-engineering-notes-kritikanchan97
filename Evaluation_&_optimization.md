## What are Agent Skills?

- An Agent Skill is a folder of instructions, and optionally scripts and reference files, that an AI agent loads by itself only when the task actually needs it.
- Agent Skills were introduced by Anthropic in October 2025, and the format is open, so anyone can write one and anyone can use one.
- In simple words, a Skill is a set of written instructions that teaches an agent how to do one particular job well. We write it once, and the agent picks it up on its own whenever that job comes up.

# Example: 
Consider a new employee joining our team. They are already smart and already know their profession. But they do not know our office. So, we do not retrain them from zero. We hand them our team handbook. Inside that handbook, there are separate chapters. One chapter for filing an expense. One chapter for releasing software. One chapter for writing a report.

The new employee does not read the whole handbook every morning. They open one chapter, only when they face that particular job.

# The description is the trigger?

Now, the most important question is: how does the agent know when to use our Skill?

The answer is the description.

The agent reads the name and the description of every available Skill. Then, when we ask for something, it compares our request against those descriptions and decides which Skill fits.

So, the description is not decoration. It is the trigger. A vague description means the Skill sits unused. A clear description means the Skill fires at the right moment.

## What is AI Agent Evaluation?

AI Agent Evaluation is the process of measuring how well an AI Agent performs on the tasks we expect it to do.

In simple words, we give the agent some tasks, watch what it does from start to finish, and check if it finished the task correctly, used the right tools, took the right steps, and did it all without wasting time or money.

Let's say we have built an AI Agent that helps users book flights. Now, the question is: how do we know if our agent is actually good? Did it pick the right flight? Did it use the booking tool correctly? Did it ask the user for missing information? Did it finish the task in a reasonable number of steps? To answer all these questions, we need AI Agent Evaluation.

Here are the main reasons we need AI Agent Evaluation:

To check if the agent finishes the task correctly.
To make sure the agent uses the right tool at the right time.
To track how many steps and how much money the agent uses for each task.
To find weak spots where the agent fails so that we can fix them.
To compare different versions of the agent after prompt changes or model changes.
To make sure the agent is safe and does not take harmful actions.

## Types of AI Agent Evaluation
There are four main types of AI Agent Evaluation. We will learn about each of them in detail.

Outcome Evaluation - We check only the final result of the task.
Trajectory Evaluation - We check every step the agent took to reach the result.
Tool Use Evaluation - We check how the agent used the tools.
Planning Evaluation - We check the quality of the agent's plan.

## Methods to Evaluate AI Agents

Automated Evaluation

We write code that runs the agent on a set of test tasks and checks the output and the trajectory against expected values. This is the fastest and cheapest method.

LLM as a Judge:

Automated checks fail when there is no single correct answer. So, here comes the LLM as a Judge to the rescue. We use a strong LLM to judge the agent's output and trajectory. We give the judge the user's request, the agent's full trajectory, and the final answer. We ask the judge to rate it on a scale of 1 to 5 on different aspects like correctness, helpfulness, and efficiency.

For the sake of understanding, let's see an example judge prompt.


You are an expert evaluator. Read the user request, the agent trajectory, and the final answer.
Rate the agent on a scale of 1 to 5 on the following aspects:
- Did it finish the task?
- Did it use the right tools?
- Did it take an efficient path?
- Was the final answer correct?

Give a short reason for each rating.

User request: {request}
Agent trajectory: {trajectory}
Final answer: {answer}

Advantage: Scales well, works for open-ended tasks.
Disadvantage: The judge can have its own biases, so we must validate it against human ratings.

Human Evaluation

Real humans look at the agent's trajectory and the final answer, and rate them. This is the gold standard for complex tasks where automated metrics and LLM judges can miss subtle problems.

Advantage: Highest quality of judgement.

Disadvantage: Slow, expensive, hard to scale.

In a real product, we usually combine all three methods. We use automated evaluation for fast feedback, LLM as a Judge for daily monitoring, and human evaluation for the final check before shipping.

## Frameworks and Tools for AI Agent Evaluation:

To run all these methods at scale, we use evaluation frameworks. They give us a structured way to define test tasks, run the agent, capture the full trajectory, score each run, and view the results on a dashboard.

There are popular frameworks that we can use for AI Agent Evaluation:

LangSmith - Built for tracing and evaluating LangChain and LangGraph agents, with strong support for trajectory inspection.
DeepEval - Open-source library with many ready-made metrics for agents, tool use, and RAG.

## Challenges in AI Agent Evaluation:

AI Agent Evaluation is hard. Here are the main challenges:

1. Many correct paths - For most tasks, there is no single correct trajectory. The agent can finish the task in many different ways, all of which are good. This makes trajectory comparison tricky.
2. Non-determinism - The same agent can give different answers for the same input, because LLMs are not deterministic. So, we must run each test many times to get a stable score.
3. Long trajectories - Real-world agent tasks can have 20, 50, or even 100 steps. Reviewing such long trajectories by hand is very tiring.
4. Environment changes - Agents often interact with real systems like search engines or databases. The results can change every day, which makes evaluation harder to reproduce.
5. Cascading failures - A small mistake in Step 2 can cause a big failure in Step 10. We must trace failures back to their root cause.
6. Safety risks - Agents take real actions. A bad action can cost real money or send a wrong email to a real user. We must catch these before they happen.
7. Cost of evaluation - Running an agent through many test tasks is expensive, because each task uses many LLM calls and many tool calls.

## What is AI Orchestration?

AI Orchestration is the process of coordinating multiple AI components, such as LLMs, tools, data sources, and agents, to work together to finish a complex task.

In simple words, a single LLM call is not enough for most real-world tasks. We often need many LLM calls, many tool calls, and many steps that depend on each other. AI Orchestration is the layer that decides which component runs, in what order, with what input, and what to do with the output.

Think of it like a conductor in an orchestra. There are many musicians, each playing a different instrument. The conductor decides who plays when, who plays louder, and who stops. Without the conductor, the music will be a mess. In the same way, without AI Orchestration, our AI system will be a mess. So, here comes AI Orchestration to the rescue.

## Why do we need AI Orchestration?

A single LLM call can answer simple questions. But, real products are not that simple. In a real product, we have many models, many tools, many data sources, and many steps. We need a way to connect all of these in a clean and reliable way.

Here are the main reasons we need AI Orchestration:

- To break a complex task into many small steps that are easy to manage.
- To pick the right model or tool for each step. A small model for easy steps, a big model for hard steps.
- To pass the output of one step as the input of the next step in a clean way.
- To run independent steps in parallel and save time.
- To handle errors and retries when a step fails.
- To add guardrails, logging, and monitoring at every step.
- To control cost and latency by avoiding unnecessary model calls.
- To make the whole system easy to test, debug, and improve.

Without AI Orchestration, we end up with messy code that nobody can maintain. With AI Orchestration, our AI system becomes clean, reliable, and ready for production.

## AI Orchestration vs AI Agents

In AI Orchestration, the developer defines the steps and the flow. The system follows a fixed plan that the developer wrote. The LLM does the work inside the steps, but it does not decide the flow.

In AI Agents, the LLM itself decides what to do next. The agent picks the tools, picks the order, and decides when to stop. The flow is dynamic and depends on the LLM's choices at runtime.

## Components of AI Orchestration
Before we learn how AI Orchestration works, we must know the main components that we orchestrate.

LLMs - The language models that do the thinking, writing, and decision-making.
Prompts - The instructions we give to the LLMs at each step.
Tools - Functions that the system can call, like a search API, a database query, or a calculator.
Memory - The place where we store past messages, results, and state across steps.
Data Sources - Vector databases, knowledge bases, files, and APIs that give us information.
Guardrails - Safety checks that block bad inputs and bad outputs.
Routers - Logic that picks which step or which model to use next.
Workflows - The graph of steps that defines how everything connects together.
These are the building blocks. AI Orchestration is the art of putting them together in the right way.

## How AI Orchestration works
Now, let's understand how AI Orchestration actually works at a high level. The steps are:

Step 1: The user sends a request to the system.
Step 2: The orchestrator reads the request and picks the first step in the workflow.
Step 3: The first step runs. It can call an LLM, a tool, or a data source.
Step 4: The orchestrator stores the output of the first step in the shared memory.
Step 5: The orchestrator picks the next step based on the workflow definition and the current state.
Step 6: The next step runs and produces its output.
Step 7: The orchestrator keeps running steps until the workflow reaches its end.
Step 8: The orchestrator sends the final output back to the user.
At every step, the orchestrator can also log the input and output, check guardrails, retry on failure, and route to a different path based on the result. This is the power of AI Orchestration. It gives us full control over a complex AI system.

## Patterns of AI Orchestration
There are five main patterns that we use again and again in AI Orchestration. Do not worry, we will learn about each of them in detail.

Sequential Pattern - Steps run one after another.
Parallel Pattern - Many steps run at the same time.
Conditional Pattern - The next step depends on the output of the previous step.
Loop Pattern - A step or a group of steps runs again and again until a condition is met.
Orchestrator-Worker Pattern - A main orchestrator splits work and gives it to many workers.

## Fine-Tuning and Model Adaptation

Fine-tuning is the process of taking a model that is already trained and training it a little more on our own specific data so that it becomes good at our specific task.

Fine-tuning means making small and careful adjustments to a model that already exists.

Consider a person who already knows how to cook many dishes. They have years of general cooking experience. Now, we want them to become an expert in only Italian food. We do not teach them cooking from zero. We only train them on Italian recipes for some time. Very soon, they become great at Italian food, while keeping most of the old cooking skills.

This is exactly what Fine-tuning does. We take a model that already knows a lot, and we teach it our special skill on top of that.

   +---------------------+        +------------------+
   |   Base model        |        |   Our own        |
   | (already trained on |  +     |   examples       |
   |  huge general data) |        | (our task data)  |
   +---------------------+        +------------------+
              |                            |
              +-------------+--------------+
                            |
                            v
                   +------------------+
                   |   Fine-tuning    |
                   +------------------+
                            |
                            v
                   +------------------+
                   |  Fine-tuned model|
                   | (expert at our   |
                   |   task)          |
                   +------------------+

Here, we can see that we start with a base model that already knows a lot, add our own examples on top, and after Fine-tuning we get a new model that is an expert at our specific task.

- The model we start with is called the base model or the pre-trained model. It is the cook who already knows general cooking.
- Inside a model, there are millions or even billions of small numbers. These numbers are called weights.
- A weight is just a number inside the model that decides how much importance to give to something.
- In simple words, weights are the "knowledge" of the model. When a model learns, it is simply adjusting these numbers again and again until it gets things right.

So, Fine-tuning means slightly adjusting these numbers by showing our own examples to the model.

## Why do we need Fine-tuning?

Let's understand the problem first, and then Fine-tuning will make complete sense.

Training a large model from zero is very costly. It needs a huge amount of data. It needs very powerful and expensive computers. It can take weeks or even months. Most people and most companies cannot afford this.

So, here comes Fine-tuning to the rescue.

Instead of building a model from zero, we take a model that big companies have already trained on massive data. This base model already understands language, grammar, facts, and general reasoning.

But, here is the catch. This general model does not know our specific needs.

Let's say we run a medical company. The general model can talk about many topics, but it does not answer in the exact medical style and accuracy we want. We do not want to spend millions to build a new model. We only want to adjust the existing one.

This way we can use Fine-tuning to solve the interesting problem of making a general model behave the way we want, without huge cost.

## How does Fine-tuning work step by step?

Step 1: Pick a base model.

First, we choose a pre-trained model. This is the model that already learned from huge general data. It already has good values for its weights.

Step 2: Prepare our own dataset.

Then, we collect examples that match our task. Each example usually has an input and the correct output.

Suppose we want our model to reply like a polite customer support agent. Our dataset will have customer questions as input and ideal polite answers as output.

The quality of this data is very important. Good examples lead to a good model. Bad examples lead to a bad model.

Step 3: Show the examples to the model.

After that, we feed our examples to the model one by one. For each input, the model makes a prediction.

Step 4: Measure the mistake.

The model's prediction is compared with the correct answer. How far apart the two are is called the loss.

In simple words, loss is a number that tells us how wrong the model is. It is always zero or more, because it measures the size of the mistake and not its direction. A big loss means a big mistake. A small loss means the model is close to correct. A loss of zero means the answer is exactly right.

Step 5: Adjust the weights.

Now comes the heart of Fine-tuning. The model slightly changes its weights to reduce the loss. This adjustment is done using a method called backpropagation with gradient descent.

Step 6: Repeat many times.

Finally, Steps 3 to 5 are repeated again and again over all our examples. Each full pass over the data is called an epoch. After enough epochs, the loss becomes small. The model now answers the way we want.

+---------+   +------------+   +-----------+   +-------------+
| Input   |   |   Model    |   |  Compare  |   |   Adjust    |
| (our    |-->| predicts   |-->| with the  |-->| the weights |
| example)|   | an output  |   |  answer   |   | (less loss) |
+---------+   +------------+   +-----------+   +-------------+
                    ^                                 |
                    |   the updated weights go back   |
                    +---------------------------------+


## LLM Evaluation

LLM Evaluation is the process of measuring how well a Large Language Model performs on the tasks we expect it to do.

In simple words, we give the model some inputs, look at the outputs, and check if the outputs are correct, helpful, safe, and useful. This is how we decide whether a model is good enough for our use case.

## Why do we need LLM Evaluation?

Here are the main reasons we need LLM Evaluation:

To compare different models and pick the best one for our use case.
To compare different versions of the same model after fine-tuning or prompt changes.
To find weak spots where the model fails so that we can fix them.
To make sure the model is safe and does not produce harmful content.
To track quality over time, so that we know if the model is getting better or worse.
To build trust with our users, our team, and our stakeholders.

## Types of LLM Evaluation

There are four main types of LLM Evaluation. We will learn about each of them in detail.

Automatic Metrics - We use formulas to score the model output against a reference answer.
Benchmarks - We test the model on standard datasets that everyone uses.
Human Evaluation - We ask humans to read the outputs and rate them.
LLM as a Judge - We use another LLM to score the outputs.

## 1. Automatic Metrics

Automatic Metrics are simple formulas that compare the model output with a reference answer and give us a score.

The best way to learn this is by taking an example. Suppose we ask the model to translate a sentence from English to French. We already have the correct French translation written by a human. The model gives its own French translation. Now, we want to know how close the model's translation is to the human translation. This is where automatic metrics come into the picture.

Here are the common ones:

# BLEU:

BLEU is used mostly for translation tasks. It is a precision-based metric. It asks: what fraction of small word groups (called n-grams) in the model output also appear in the reference answer? A higher BLEU score means the model output is closer to the reference. For example, if the reference is "The cat sat on the mat" and the model says "The cat sat on the mat", BLEU is very high. 

# ROUGE

ROUGE is used mostly for summarization tasks. It asks: what fraction of n-grams in the reference summary are covered by the model summary? Just like BLEU, a higher score is better.

# BERTScore:

BERTScore uses contextual embeddings to compare the meaning of the model output with the reference. So, even if the words are different, if the meaning is close, the score is high.

# METEOR: 
METEOR is another metric that improves on BLEU by handling synonyms, stemming, and word order. It sits between pure surface matching and full semantic matching.

# Perplexity
Perplexity measures how well the model predicts the next token. A lower perplexity means the model assigns a higher probability to the actual next token in the test data. This metric is mostly used during model training to track if the model is learning.

# Exact Match
Exact Match is the simplest one. The score is 1 if the model output is exactly the same as the reference answer, and 0 otherwise. This is useful for tasks like math problems or short factual questions.

## Note: In modern LLM evaluation, reference-based metrics like BLEU and ROUGE are mostly used in research papers and translation pipelines. For production LLM applications, we usually rely on LLM as a Judge or task-specific evaluation

## What is RLHF

RLHF (Reinforcement Learning from Human Feedback) is a training technique where we teach a Large Language Model (LLM) to produce responses that humans prefer, by collecting human preferences and converting them into a reward signal that guides further training.

In simple words, we let the model generate responses, we ask humans which response is better, and we update the model so that its future responses look more like the preferred ones.

RLHF = Reinforcement Learning + Human Feedback

Let's decode each part.

Reinforcement Learning (RL) is a way of training a model where it learns by trial and error. The model takes an action, receives a reward, and adjusts its behavior to earn more reward over time. We have a detailed blog on Reinforcement Learning that goes deeper into this.

Human Feedback means the reward does not come from a fixed automatic metric. It comes from real humans who compare model outputs and pick the better one.





































































































































































































































