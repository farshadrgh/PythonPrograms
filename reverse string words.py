class reverse:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))


print(reverse().reverse_words('This is a test for the program'))