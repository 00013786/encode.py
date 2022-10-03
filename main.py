#defining a function that takes an input called message in encodes it

def print_rle(message):
    n = len(message)
    i = 0
    #lines that are above finds length since it starts from zero, n-1 means it is the end
    while i < n - 1:

        count = 1
        while (i < n - 1 and
               message[i] == message[i + 1]):
            count += 1
            i += 1
        i += 1

        print("*" + message[i - 1] + str(count),
              end="")


if __name__ == "__main__":
    message = "AAAABBBCCCCCCCCDDDDhithereEEEEEEEEEFF"
    print_rle(message)
