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
            pattern_chars_dict[self._pattern[i]] = i

        return pattern_chars_dict

    def search(self) -> List[int]:
        """main search func"""

        # getting variables ready
        s, p = self._search_text, self._pattern
        p_len, s_len, s_pos = len(p), len(s), 0
        found_index_list = []
        pattern_chars_dict = self.preprocess()

        while s_pos <= s_len - p_len:
            bad_character_pos = -1
            # checking mismatch position
            for i in range(p_len - 1, -1, -1):
                if s[s_pos + i] != p[i]:
                    bad_character_pos = i
                    break

            if bad_character_pos == -1:
                # append position index to result list since no mismtach found
                s_pos += 1
                found_index_list.append(s_pos)
            else:
                s_pos += (
                    # the last occurrence position of character in pattern
                    # that matches the bad charater in search text
                    i - pattern_chars_dict[s[s_pos + i]]
                    # this if statement is checking if there exist a bad
                    # character match in the pattern that is at the left
                    # of bad character position if no, we set the value to
                    # be (i + 1) to fail the condition on purpose
                    if pattern_chars_dict.get(s[s_pos + i], i + 1) < i
                    # so if above condition check fails, shift the pattern
                    # pass the bad character
                    else i + 1
                )
        return found_index_list
