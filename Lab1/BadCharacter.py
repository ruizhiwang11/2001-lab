from typing import List, Dict


class BadCharacter(object):
    def __init__(self, pattern: str, search_text: str):
        self._pattern = pattern.upper()
        self._search_text = search_text.upper()

    def preprocess(self) -> Dict:
        """Bad Character preprocessing"""

        # need a dictionary with pattern as key and last occurrence as value
        pattern_chars_dict = {}
        for i in range(len(self._pattern)):
            actual_char = self._pattern[i]
            maxshift = max(1,len(self._pattern) - i -1)
            pattern_chars_dict[actual_char] = maxshift
        print(pattern_chars_dict)
        return pattern_chars_dict

    def search(self) -> List[int]:
        """main search func"""

        # getting variables ready
        s, p = self._search_text, self._pattern
        p_len, s_len, s_pos = len(p), len(s), 0
        found_index_list = []
        pattern_chars_dict = self.preprocess()
        while s_pos <= s_len - p_len:
            bad_character_pos = 0
            # checking mismatch position
            for i in range(p_len - 1, -1, -1):
                if(p[i] != s[i+s_pos]):
                    if s[i+s_pos] in pattern_chars_dict:
                        bad_character_pos = pattern_chars_dict[s[i+s_pos]]
                        break
                    else:
                        bad_character_pos = p_len
                        break
            if bad_character_pos == 0:
                # append position index to result list since no mismtach found
                found_index_list.append(s_pos + 1)
            if bad_character_pos == 0:
                s_pos +=1
            else:
                s_pos += bad_character_pos
            #print(s_pos)
            # else:
            #     s_pos += (
            #         # the last occurrence position of character in pattern
            #         # that matches the bad charater in search text
            #         i - pattern_chars_dict[s[s_pos + i]]
            #         # this if statement is checking if there exist a bad
            #         # character match in the pattern that is at the left
            #         # of bad character position if no, we set the value to
            #         # be (i + 1) to fail the condition on purpose
            #         if pattern_chars_dict.get(s[s_pos + i], i + 1) < i
            #         # so if above condition check fails, shift the pattern
            #         # pass the bad character
            #         else i + 1
            #     )
        return found_index_list
