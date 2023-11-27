import numpy as np


class ContentFilter:

    def __init__(self, filename):
        try:
            with open(filename, 'r') as f:
                self.file = filename
                self.content = f.readlines()

        except (FileNotFoundError, TypeError, OSError) as e:
            new_filename = input(" Please enter a valid file name: ")
            self.__init__(new_filename)

        self.char = 0
        self.alpha_char = 0
        self.numer_char = 0
        self.whit_char = 0
        self.num_lines = 0

        for line in self.content:
            self.char += len(line)
            self.alpha_char += sum([word.isalpha() for word in line])
            self.numer_char += sum([word.isdigit() for word in line])
            self.whit_char += sum([word.isspace() for word in line])
            self.num_lines += 1

    def uniform(self, filename, mode='w', case='upper'):
        if mode not in ['w', 'x', 'a']:
            raise ValueError("Mode must be 'w', 'x', or 'a'!")
        elif case not in ['lower', 'upper']:
            raise ValueError("Case must be 'lower' or 'upper'!")

        with open(filename, mode) as outfile:
            if case == 'upper':
                for line in self.content:
                    outfile.write(line.upper())
                outfile.write("\n")
            else:
                for line in self.content:
                    outfile.write(line.lower())
                outfile.write("\n")

    def reverse(self, filename, mode='w', unit='line'):
        if mode not in ['w', 'x', 'a']:
            raise ValueError("Mode must be 'w', 'x', or 'a'!")
        elif unit not in ['line', 'word']:
            raise ValueError("Unit must be 'line' or 'word'!")

        with open(filename, mode) as outfile:
            if unit == 'line':
                for line in self.content:
                    words = line.split()
                    rev_line = " ".join(reversed(words))
                    outfile.write(rev_line + "\n")

            else:
                for line in self.content:
                    outfile.write(line[::-1] + "\n")


    def transpose(self, filename, mode='w'):
        if mode not in ['w', 'x', 'a']:
            raise ValueError("Mode must be 'w', 'x', or 'a'!")

        word_matrix = []
        for line in self.content:
            words = line.split()
            word_matrix.append(words)

        word_matrix = np.array(word_matrix).T

        with open(filename, mode) as outfile:
            for row in word_matrix:
                line = " ".join(row)
                outfile.write(line + "\n")

    def __str__(self):
        return ("Source file:\t{}\n".format(self.file)
                + "Total characters:\t{}\n".format(self.char)
                + "Alphabetic characters:\t{}\n".format(self.alpha_char)
                + "Numerical characters:\t{}\n".format(self.numer_char)
                + "Whitespace characters:\t{}\n".format(self.whit_char)
                + "Number of lines:\t{}".format(self.num_lines))


cf = ContentFilter("cf_example1.txt")
cf.uniform("uniform.txt", mode='w', case='upper')
cf.uniform("uniform.txt", mode='a', case='lower')
cf.reverse("reverse.txt", mode='w', unit='word')
cf.reverse("reverse.txt", mode='a', unit='line')
cf.transpose("transpose.txt", mode='w')
print(cf)
