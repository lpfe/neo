import lmstudio as lms

model = lms.llm()

# for fragment in model.respond_stream("What is the meaning of life?") :
for fragment in model.respond_stream("삶이란 뭐야?") :
    print(fragment.content, end = '', flush = True)

print()