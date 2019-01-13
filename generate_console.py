from textgenrnn import textgenrnn
t = textgenrnn('ApeMiIk_twitter_weights.hdf5')

t.generate(5, temperature=1.0)