class BFMatcher(object):
    def __init__(self, pattern, string):
        self._pattern = pattern.upper()
        self._string = string.upper()
    #An implementation of the brute force algorithm
    def bfSearch(self):
        found_index_list = []
        found = False
        p_len, s_len, pos = len(self._pattern), len(self._string), 0
        while pos <= s_len - p_len:
            s_ptr = pos
            p_ptr = 0
            while p_ptr < len(self._pattern):
                if(self._string[s_ptr] == self._pattern[p_ptr]):
                    s_ptr += 1
                    p_ptr += 1
                else:
                    break
                if p_ptr == len(self._pattern):
                    found = True
                    found_index_list.append((pos+1))
            pos += 1
        return found_index_list

