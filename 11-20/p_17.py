'''
If all the numbers from 1 to 1000 (one thousand)
inclusive were written out in words,
how many letters would be used?
'''
num_map = {'0': '', '1': 'one', '2': 'two', '3': 'three',
           '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
           '8': 'eight', '9': 'nine', '10': 'ten', '11': 'eleven',
           '12': 'twelve', '13': 'thirteen', '14': 'fourteen',
           '15': 'fifteen', '16': 'sixteen', '17': 'seventeen',
           '18': 'eighteen', '19': 'nineteen', '20': 'twenty',
           '30': 'thirty', '40': 'forty', '50': 'fifty', '60': 'sixty',
           '70': 'seventy', '80': 'eighty', '90': 'ninety'}
#key corresponds to length of digit
power_map = {4: 'thousand', 3: 'hundredand'}


def num_chunker(num):
    for index, digit in enumerate(num):
        #for teens
        if num[index:] in num_map and num[index:] != '0':
            yield num[index:]
            break
        #add appropriate amount of zeros after digit
        chunk = digit + '0' * ((len(num) - 1) - index)
        #if chunk is just zeros skip it
        if chunk == '0' * len(chunk):
            continue
        yield chunk


def num_to_word(num):
    key = []
    for chunk in num_chunker(num):
        if chunk in num_map:
            #then below one-hundred
            key.append(num_map[chunk])
        else:
            #chunk >= 100
            key.append(num_map[chunk[0]])
            key.append(power_map[len(num)])

    if len(key) == 2 and key[1] == 'hundredand':
        key[1] = key[1].replace('and', "")

    return ''.join(key)

answer = sum([len(num_to_word(x)) for x in map(str, xrange(1, 1001))])
print answer
