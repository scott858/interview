def smallest_window(big_str, sub_str):
    sub_hash = [0] * 256
    for ch in sub_str:
        sub_hash[ord(ch)] += 1

    orig_sub_hash = sub_hash.copy()

    result = -1
    r_ix = len(big_str) - len(sub_str) + 1
    count = len(sub_str)
    next_sub_ix = None
    for start_sub_ix in range(r_ix):
        # iterate to an occurrence of sub-character
        ch = big_str[start_sub_ix]
        if orig_sub_hash[ord(ch)] > 0:
            if next_sub_ix is None:
                # start out iteration at occurrence of first sub-character
                next_sub_ix = start_sub_ix

            while count > 0 and next_sub_ix < len(big_str):
                ch = big_str[next_sub_ix]
                if sub_hash[ord(ch)] > 0:
                    # found a match
                    count -= 1

                # count duplicates anyway
                sub_hash[ord(ch)] -= 1

                next_sub_ix += 1

            if count == 0:
                temp_result = ''.join(big_str[start_sub_ix:next_sub_ix])
                if result == -1 or len(temp_result) < len(result):
                    result = temp_result
                # shifted the start to the right by one so lost the first occurrence
                ch = big_str[start_sub_ix]
                sub_hash[ord(ch)] += 1
                if sub_hash[ord(ch)] > 0:
                    # if what was popped was in the substring add it back to the count
                    count += 1

    return result


if __name__ == '__main__':
    str1 = list('timetopractice')
    str2 = list('toc')

    # str1 = list('zoomlazapzo')
    # str2 = list('oza')

    res = smallest_window(str1, str2)
    print(res)
