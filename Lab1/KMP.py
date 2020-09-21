class KmpMatcher(object):
    def __init__(self, pattern, string):
        self._pattern = pattern.upper()
        self._string = string.upper()
        self._prefix = []
    # Matches the motif pattern against itself.

    def computePrefix(self):
        # Initialize prefix array
        self.__fillPrefixList()
        k = 0
        for pos in range(1, len(self._pattern)):

            # Unique base in pattern
            while(k > 0 and self._pattern[k] != self._pattern[pos]):
                k = self._prefix[k-1]
            #repeat in pattern
            if(self._pattern[k] == self._pattern[pos]):
                k += 1
            self._prefix[pos] = k
    # Initialize the prefix list and set all elements are 0

    def __fillPrefixList(self):
        self._prefix = [0] * (len(self._pattern))

    # An implementation of the Knuth-Morris-Pratt algorithm for linear time string matching
    def kmpSearch(self):
        # Compute prefix array
        self.computePrefix()
        # Number of characters matched
        p_len, s_len, pos = len(self._pattern), len(self._string), 0
        match = 0
        found = False
        found_index_list = []
        while pos < s_len :
            # Next character is not a match
            while(match > 0 and self._pattern[match] != self._string[pos]):
                match = self._prefix[match-1]
            # A character match has been found
            if(self._pattern[match] == self._string[pos]):
                match += 1
            # Pattern found
            if(match == len(self._pattern)):
                found_index_list.append((pos-match+2))
                found = True
                match = self._prefix[match-1]
            pos += 1
        return found_index_list