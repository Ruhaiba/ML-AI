import re
import long_responses as long

def message_probability(user_mess, recog_words, single=False, required_words=[]):
    mess_certain=0
    has_req_words=True

    #How many words present in predefined message
    for word in user_mess:
        if word in recog_words:
            mess_certain+=1

    #Percentage of recognized words 
    percentage=float(mess_certain)/float(len(recog_words))

    #Checks to make sure required words are in string
    for word in required_words:
        if word not in user_mess:
            has_req_words=False
            break

    if has_req_words or single:
        return int(percentage*100)
    else:
        return 0
    
def check_all_mess(mess):
    highest_prob_list={}
    def response(bot_resp, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_resp]=message_probability(mess, list_of_words, single_response, required_words)
    #Response -----------------------------------------------------------------------------------------
    response("Hello!", ["hi", "hey", "sup", "hello", "heya", "hai"], single_response=True)
    response("I'm doing great! How about you?", ["how","are","you","doing"], single_response=["how"])
    response("No problem! Thanks for visiting!", ["thank","you","for","helping","me!"], single_response=["thank", "you"])

    best_match=max(highest_prob_list, key=highest_prob_list.get)
    print(highest_prob_list)
    return best_match

def get_response(user_inp):
    split_mess=re.split(r'\s+|[!-.?,:;]\s*', user_inp.lower())
    response=check_all_mess(split_mess)
    return response

#Response System
while True:
    print("Bot: " + get_response(input("You: ")))