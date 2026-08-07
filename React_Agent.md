## What is a ReAct Agent?

ReAct Agent = Reasoning + Acting + Agent

Reasoning is the thinking part - the LLM figures out what to do next. Acting is the doing part - the LLM picks a tool, and the loop calls it. 
Agent is the wrapper around the LLM that runs this loop, executes the tools, and feeds the results back.

In simple words:

ReAct Agent = LLM + Tools + A loop that lets the LLM think, act, and observe until the task is done.

Think of a ReAct Agent like a new intern on their first day. They do not solve every problem in their head. 
They think about what they need, open a tool, read the result, think again, and repeat. A ReAct Agent works the exact same way - but at the speed of a machine.
