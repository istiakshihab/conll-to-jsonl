import json, getopt, sys

argumentList = sys.argv[1:]
if(len(argumentList)!=2):
    print("Write the name of the input and output file.")

with open(argumentList[0]) as file:
    sentence_list = []
    sentence = []
    for line in file:
        if(line == '\n'):
            sentence_list.append(sentence)
            sentence = []
        elif(line.startswith("# id ")):
            continue
        else:
            sentence.append(line)

with open(argumentList[1], 'a') as output:
    for sentence in sentence_list:
        token_list = []
        label_list = []
        for word in sentence:
            token,_,_,label = word.strip().split(" ")
            token_list.append(token)
            label_list.append(label)
        jsonl = json.dumps({"tokens":token_list, "tags":label_list}, ensure_ascii=False)
        output.write(jsonl+"\n")    
