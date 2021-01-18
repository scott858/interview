def get_span(price):
    """
    alternatively use a queue for peak values
    :param price:
    :return:
    """
    len_price = len(price)
    span = [1] * len_price
    for i in range(1, len_price):
        if price[i] >= price[i - 1]:
            i_last = i - 1 - span[i - 1]
            while price[i] > price[i_last] and i_last >= 0:
                i_last = i_last - span[i_last]
            span[i] = i - i_last

    return span


