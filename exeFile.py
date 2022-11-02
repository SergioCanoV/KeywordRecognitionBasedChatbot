from main import *

#defining conversation start/end protocols/
print("BOT: My name is Ringo. Let's talk about LOTR: The Fellowship of the Ring.  Also, if you want to exit any time, just type bye!")
flag = True
while (flag==True):
    user_response = input()
    user_response = user_response.lower()
    if(user_response != 'bye'):
        if(user_response =='thanks' or user_response =='thank you'):
            flag=False
            print("BOT: You are welcome")
        else:
            if(greet(user_response)!=None):
                print("BOT: " + greet(user_response))
            else:
                sent_tokens.append(user_response)
                word_tokens=word_tokens+nltk.word_tokenize(user_response)
                final_words = list(set(word_tokens))
                print("BOT: ", end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag = False
        print("BOT: goodbye! take care")
