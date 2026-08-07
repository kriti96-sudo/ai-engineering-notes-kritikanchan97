## What is a ReAct Agent?

ReAct Agent = Reasoning + Acting + Agent

Reasoning is the thinking part - the LLM figures out what to do next. Acting is the doing part - the LLM picks a tool, and the loop calls it. 
Agent is the wrapper around the LLM that runs this loop, executes the tools, and feeds the results back.

In simple words:

ReAct Agent = LLM + Tools + A loop that lets the LLM think, act, and observe until the task is done.

Think of a ReAct Agent like a new intern on their first day. They do not solve every problem in their head. 
They think about what they need, open a tool, read the result, think again, and repeat. A ReAct Agent works the exact same way - but at the speed of a machine.

## ReAct Agent vs AI Agent?

AI Agent is the category - any system where an LLM is wrapped in a loop with tools and memory. It does not say how the loop is structured, how the LLM picks the next action, or whether the reasoning is visible.

ReAct is a pattern for building that loop, where the LLM follows a Thought - Action - Observation cycle. At every step, the LLM first writes its reasoning (the Thought), then picks a tool (the Action), then reads the result (the Observation), then thinks again. The reasoning is explicit, step by step, and visible at every turn. That explicit step-by-step reasoning is Chain-of-Thought (CoT) Prompting surfaced inside the agent loop.

So when we say "ReAct Agent," we mean an AI Agent built with the ReAct pattern. 

## Anatomy of a ReAct Agent

A ReAct Agent has five parts:

1. The LLM. This is the brain. It does the reasoning. It reads the conversation history and decides the next step - either pick a tool for the loop to call, or produce the final answer.

2. The System Prompt. This tells the LLM how to behave. It explains the ReAct pattern, lists the available tools, and sets the rules. Without a good system prompt, the LLM may not think, act, or stop reliably.

3. The Tools. These are the actions the agent can take - search the web, query a database, run a calculator, send an email, read a file, and etc. Each tool has a name, a description, and an input schema.

4. The Memory. This is the running history of the conversation - the user's question, every thought, every action, every observation. The LLM reads this memory at every step to decide what to do next.

5. The Loop Controller. This is the code that runs the loop. It sends the memory to the LLM, executes any tool calls, appends the results back to the memory, and checks if the agent is done. It also handles the stop conditions - like a maximum number of steps.

All five parts work together. Remove any one of them, and it is no longer a ReAct Agent.

## The ReAct Prompt Template

Here is a simple ReAct prompt template:

You are a helpful assistant that solves problems by thinking step by step and recommending tools when needed.

You have access to the following tools:
- search(query): Search the web for information.
- calculator(expression): Evaluate a math expression.

At each step, respond in one of these two formats:

Format 1 - When you need to recommend a tool:
Thought: <your reasoning about what to do next>
Action: <tool_name>(<tool_input>)

Format 2 - When you have the final answer:
Thought: <your final reasoning>
Final Answer: <the answer to the user's question>

Rules:
- Always start with a Thought.
- Recommend one tool per turn, unless multiple independent tools would clearly help in parallel.
- Wait for the Observation before continuing.
- Stop as soon as you have the final answer.

## How a ReAct Agent Thinks and Acts

Step 1: The user sends a question. The Loop Controller adds it to the Memory.
Step 2: The Loop Controller sends the Memory (system prompt + user question + history) to the LLM.
Step 3: The LLM responds with either a Thought + Action, or a Final Answer.
Step 4: If the response is a Final Answer, the Loop Controller returns it to the user. The agent is done.
Step 5: If the response is a Thought + Action, the Loop Controller executes the tool and gets the result. This result is the Observation.
Step 6: The Loop Controller appends the Thought, Action, and Observation to the Memory.
Step 7: Go back to Step 2.
This loop continues until the LLM produces a Final Answer or the maximum step limit is reached.


## Implementing a ReAct Agent

- The initial messages. We seed the memory with the ReAct system prompt and the user's question. The system prompt is what makes the LLM follow the Thought - Action - Observation pattern, so it must be the first message in the memory.
- The while True loop. This is the Loop Controller. It keeps going until either the LLM has the final answer or we hit the step limit.
- The step limit. We bail out after max_steps iterations. This protects us from infinite loops - one of the most common failure modes for ReAct Agents.
- The LLM call. We send the full memory (the conversation history) along with the list of tools. The LLM does the Thought step here - it reasons about the next move and either picks an Action or returns the Final Answer.
- The stop check. If response.is_done is True, the LLM is telling us "I am done, here is the final answer." We return that answer and exit the loop.
- The tool-call branch. If the LLM picked one or more tools, we run each one with call_tool using the arguments the LLM gave, append the observation back to the memory, and the loop continues.
- That is the complete skeleton of a ReAct Agent - a while loop, an LLM call inside it, a check for the final answer, and a tool-call branch that feeds observations back. Everything else we add on top - structured tracing of Thoughts, retries, reflection, parallel tool calls - is polish around this core loop.


## Common Failure Modes and How to Fix Them

ReAct Agents are powerful, but they can fail in specific ways. Let's decode each one.

1. Infinite loops. The agent keeps calling the same tool with the same input and never produces a final answer.

How to fix: Set a hard max_steps limit. Also, detect repeated identical actions and either stop or inject a message telling the agent to try a different approach.

2. Wrong tool selection. The agent calls the wrong tool for the job - like using search for a math problem.

How to fix: Write very clear tool descriptions. The description is what the LLM uses to pick the tool, so every word matters. Say exactly what the tool does and when to use it.

3. Hallucinated tool calls. The agent calls a tool that does not exist or passes invalid arguments.

How to fix: Use an LLM with native tool-use support (like Claude, GPT, or Gemini) so the schema is enforced. Always validate tool inputs before executing, and return a clear error message as the Observation if they are invalid.

4. Context explosion. After many steps, the conversation history becomes too long for the LLM's context window.

How to fix: Summarize older steps, drop stale observations, or use a separate memory store. For long-running agents, we must actively manage the context - this is the discipline of Context Engineering.

5. Premature stopping. The agent gives a final answer before gathering enough information.

How to fix: Add a critic step that reviews the final answer before it is returned, or require the agent to check its answer against a checklist (Did I cover all the parts of the question? Did I cite a source? Did I verify the math?) before emitting the Final Answer. The system prompt should make this verification step explicit, not optional.

6. Getting stuck after a tool error. A tool fails, and the agent does not know how to recover.

How to fix: Catch tool errors, convert them into natural-language Observations (e.g., "Error: the search API timed out. Try again or use a different query."), and let the LLM reason its way out.

Quick Summary

- A ReAct Agent is an AI Agent that loops through Thought, Action, and Observation until the task is done. It is an LLM wrapped in a loop with tools and memory.
- The anatomy has five parts: the LLM, the System Prompt, the Tools, the Memory, and the Loop Controller. Remove any one, and it is no longer a ReAct Agent.
- The system prompt is what makes a plain LLM behave reliably as a ReAct Agent. It explains the pattern, lists the tools, and sets the rules.
- The loop is simple: send memory to LLM -> if tool call, execute and append observation -> if final answer, return.
- Common failure modes include infinite loops, wrong tool selection, hallucinated tool calls, context explosion, premature stopping, and errors after tool failures. Handling these is the real work of building a production agent.
- ReAct or a ReAct-style loop is the most common pattern under the hood of modern AI agents - from coding assistants to customer support bots to research assistants.



















