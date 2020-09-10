from typing import List


class BadCharacter(object):
    def __init__(self, pattern: str, search_text: str):
        self._pattern = pattern.upper()
        self._search_text = search_text.upper()

    def preprocess(self, process_text: str) -> int:
        """preprocessor for determining next move"""

        # getting variables ready
        s = process_text
        p = self._pattern
        p_len = len(p)
        bad_character_pos = p_len

        # find bad character position
        for i in range(p_len - 1, -1, -1):
            if s[i] != p[i]:
                bad_character_pos = i
                break

        # if no last occurence of bad character found in text
        # should slide the pattern  pass the bad character
        preprocess_result = bad_character_pos + 1

        for j in range(bad_character_pos - 1, -1, -1):
            # if exist any character same as bad character
            # return number of pos need to move to align them
            if p[j] == s[bad_character_pos]:
                preprocess_result = bad_character_pos - j

        # default is the
        return preprocess_result

    def search(self) -> List[int]:
        """main search func"""

        # getting variables ready
        s = self._search_text
        p = self._pattern
        p_len, s_len, s_pos = len(p), len(s), 0
        found_index_list = []

        while s_pos <= s_len - p_len:
            # find number of mtached characters for substring
            # with any arbitrary starting position
            num_match = sum(1 for i in range(p_len - 1, -1, -1) if s[s_pos + i] == p[i])

            if num_match == p_len:
                # append position index to result list
                found_index_list.append(s_pos)
                s_pos += 1
            else:
                # apply bad character preprocessing
                s_pos += self.preprocess(s[s_pos : s_pos + p_len + 1])
        return found_index_list
