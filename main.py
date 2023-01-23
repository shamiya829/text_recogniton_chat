import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # word count
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # probability
    percentage = float(message_certainty) / float(len(recognised_words))

    # check for required word
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # check for required word or if is single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('I was born last weekend.', ['how', 'old', 'you', 'age'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    response('My name is Bobbie Bot!', ['what', 'name', 'your', 'is'], required_words=['name'])
    response('I can\'t do math yet. Can you teach me?', ['multiply','math','add', '+', 'minus', '-','times','divide'], single_response=True)
    response('Pleaaaaaase', ['no', 'can\'t'], single_response=True)
    response('Yayay!', ['yes', 'sure','ofcourse'], single_response=True)
    response('The weather is great!', ['what', 'is','weather'], required_words=['name'])

    # longer
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


while True:
    # print('Bot: ' + get_response(input('You: ')))
