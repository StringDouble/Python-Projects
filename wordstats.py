#Copyright Yoana Stankova 2018
keep = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q','r', 's', 't', 'u', 'w', 'x', 'y', 'z',
        ' ', '-', "'"}

def normalize (s):
    result = ''
    for c in s.lower():
        if c in keep:
            result += c
    return result

def make_freq_dict(s):
    s = normalize(s)
    words = s.split()
    d = {}
    for w in words:
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
    return d

def print_file_stats(fname):
    s = open(fname, 'r'.read())
    num_chars = len(s)
    num_lines = s.count('\n')

    d = make_freq_dict(s)
    num_words = sum(d[w] for w in d)

    1st = [(d[w], w) for w in d]
    1st.sort()
    1st.reverse()

    print("The file '%s' has: " % fname)
    print("   %s characters" % num_chairs)
    print("   %s lines" % num_lines)
    print("   %s words" % num_words)

    print("\nThe top 10 most frequent words are:")
    i = 1
    for count, word in 1st[:10]:
        print('%2s. %4s %s' % (i, count, word))
        i += 1

def main():
    print_file_stats('bill.txt')

if __name__ == '__main__':
    main()
