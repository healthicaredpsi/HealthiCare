from chatterbot import ChatBot
from chatterbot.trainers import listTrainer
from chatterbot.trainers import FhatterBotCorpusTrainer

chatbot=ChatBot(
    'help',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///db.sqlite3'
)
#conversation = [
  #  "Hello",
  #  "Hi there!",
  #  "How are you doing?",
  #  "I'm doing great",
   # "That is good to hear",
  #  "Thank you"
#]
training_data_quesans = open('training_data/ques_ans.txt').read().splitlines()

training_data = training_data_quesans

trainer = ListTrainer(chatbot)
trainer.train(training_data)

# Training with English Corpus Data
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    'chatterbot.corpus.english'
)