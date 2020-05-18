# naive algorythm
def nfind(string, text):
    naive_position = []
    if string and text:
        for n in range(len(text) - len(string) + 1):
            m = 0
            while m < len(string) and text[n + m] == string[m]:
                m += 1
                if m == len(string):
                    naive_position.append(n)
    return naive_position


# prefix table
def lps(string):
    lps_array = [0 for i in range(len(string))]
    i = 0
    j = 1
    while j < len(string):
        if string[i] == string[j]:
            lps_array[j] = i + 1
            i += 1
            j += 1
        else:
            if i != 0:
                i = lps_array[i - 1]
            else:
                j += 1
    return lps_array


# KMP algorythm
def kmpfind(string, text):
    kmp_position = []
    if string and text:
        prefix = lps(string)
        n = 0
        m = 0
        while n < len(text) - len(string):
            if text[n] == string[m]:
                n += 1
                m += 1
            else:
                if m != 0:
                    m = prefix[m - 1]
                else:
                    n += 1
            if m == len(string):
                kmp_position.append(n - m)
                m = prefix[m - 1]
    return kmp_position
