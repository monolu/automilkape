from textgenrnn import textgenrnn
t = textgenrnn()
t.train_from_file('ApeMiIk_tweets.txt', num_epochs=150)
