# python3

#B = 13
#Q = 256

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file)
    # to choose which input type will follow
    #
    # after input type choice
    # read two lines
    # first line is pattern
    # second line is text in which to look for pattern
    # return both lines in one return
    input_choice = input()
    if  input_choice[0].lower() == "i":
        pattern = input()
        text = input()

    elif input_choice[0].lower() == "f":
        file = open(input_choice.split(" ", 1)[1], encoding="utf-8")
        data = file.readlines()
        pattern = str(data[0])
        text = str(data[1])

    return (pattern.rstrip(), text.rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm and return an iterable variable
    pat_len = len(pattern)
    txt_len = len(text)
    pat_hash = 0    # hash value for pattern
    txt_hash = 0    # hash value for txt
    multiplier = 1
    Q = 256
    B = 13
    occurances = []
    # The value of multiplier would be "pow(B, pat_len-1)%Q"
    for i in range(pat_len-1):
        multiplier = (multiplier*B) % Q
    # Calculate the hash value of pattern and first window of text
    for i in range(pat_len):
        pat_hash = (B*pat_hash + ord(pattern[i])) % Q
        txt_hash = (B*txt_hash + ord(text[i])) % Q
    # Slide the pattern over text one by one
    for i in range(txt_len-pat_len+1):
        # Check the hash values of current window of text and pattern if the hash values match
        # then only check for characters one by one
        if pat_hash == txt_hash:
            # Check for characters one by one
            for j in range(pat_len):
                if text[i+j] != pattern[j]:
                    break
                else:
                    j += 1
            # if pat_hash == txt_hash and pattern[0...pat_len-1] = text[i, i+1, ...i+pat_len-1]
            if j == pat_len:
                occurances.append(i)
        # Calculate hash value for next window of text: Remove leading digit, add trailing digit
        if i < txt_len-pat_len:
            txt_hash = (B*(txt_hash-ord(text[i])*multiplier) + ord(text[i+pat_len])) % Q
            # We might get negative values of txt_hash, converting it to positive
            if txt_hash < 0:
                txt_hash = txt_hash+Q

    if len(occurances) == 0:
        return [0]
    return occurances


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
