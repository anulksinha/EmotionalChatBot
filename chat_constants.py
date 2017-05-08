import numpy as np

BLANK = np.array( [0]*300 + [1] )
SPLIT_STRING = '+++$+++'
EMOTE_DELIMITER = '@'
BLANK_LINE = " ".join( [ '1', '9', '1', EMOTE_DELIMITER, '' ] )
MIN_SENT_LENGTH = 6
MAX_SENT_LENGTH = 30
EMBED_DIM = len(BLANK)