from langchain_core.runnables import RunnableLambda, RunnableSequence

add_one = RunnableLambda(lambda x: x + 1)
double = RunnableLambda(lambda x: x * 2)
seq = RunnableSequence(add_one, double)  # same as add_one | double
print(seq.invoke(3))  # (3 + 1) * 2 = 8
