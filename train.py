from textgenrnn import textgenrnn
t = textgenrnn()
t.train_from_file(new_model=False, 'ApeMiIk_tweets.txt', num_epochs=150)