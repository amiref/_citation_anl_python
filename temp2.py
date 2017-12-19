import pickle

for i in range(1,6):
    handle = open("D:/aebrahimifard/Desktop/Data/SeparatedTopics/" + "topics(" + str(i) + "#20#20).LDA", "rb")
    pickledNodes = handle.read()
    papers = pickle.loads(pickledNodes)
    for item in papers:
        print(papers[item].print_topics(num_topics=1, num_words=20))
        print()
    handle.close()