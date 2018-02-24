import discord
import asyncio

import nltk
from nltk.stem.wordnet import WordNetLemmatizer

client = discord.Client()

verbs = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
good_verbs = ['VB', 'VBP', 'VBZ']

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_message(message):
    if str(message.author) != 'paraparrot#8776' and str(message.author) != 'Richard#9404':
        print(message.author)
        # check if message contains a verb
        spacey_message = ' '+message.content+' '
        original_verb = ''
        target_verb = ''

        word_pos = nltk.pos_tag(nltk.word_tokenize(message.content))


        for word, pos in word_pos:
            if pos not in verbs:
                continue

            original_verb = word

            if pos not in good_verbs:
                print('This isnt in present tense, so i have to convert it to...')
                try:
                    target_verb = WordNetLemmatizer().lemmatize(original_verb, 'v')
                except Exception as e:
                    continue
            else:
                print('This is a good verb.')
                target_verb = original_verb

            print(target_verb)
            break

        if target_verb != '':
            #await client.send_message(message.channel, 'the good verb is ' + target_verb)
            print('The index of the verb is ' + str(message.content.index(original_verb)))
            verb_index = spacey_message.index(' '+original_verb+' ')
            # the rest of the sentence is index + len(original_verb)
            rest_of_message = spacey_message[verb_index + len(original_verb)+1:]
            print('The rest of the message is: ' + rest_of_message)


            await client.send_message(message.channel, 'only losers ' + target_verb + rest_of_message)
        print(word_pos)
        #await client.send_message(message.channel, word_pos)
        # if it does then pull a verb and noun
        # send new message 'only normies verb noun'


with open('token.txt', 'r') as token_file:
    token = token_file.read().split('\n')[0]

client.run(token)
