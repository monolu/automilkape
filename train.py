from textgenrnn import textgenrnn
t = textgenrnn('textgenrnn_weights.hdf5')
t.train_from_file('ApeMiIk_tweets.txt', num_epochs=20)