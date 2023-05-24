class IndexSorter:
    def __init__(self, input_filename, output_filename):
        self.input_filename = input_filename
        self.output_filename = output_filename
    def run(self):
        line_lengths = []
        lines = []

        with open(self.input_filename, 'r') as file:
            for line in file:
                line_lengths.append(len(line))
                lines.append(line)

        line_length_counts = [0] * (max(line_lengths) + 1)
        for length in line_lengths:
            line_length_counts[length] += 1

        for i in range(1, len(line_length_counts)):
            line_length_counts[i] += line_length_counts[i - 1]

        output = [''] * len(lines)
        for i in range(len(lines) - 1, -1, -1):
            length = line_lengths[i]
            output[line_length_counts[length] - 1] = lines[i]
            line_length_counts[length] -= 1

        with open(self.output_filename, 'w') as file:
            for line in output:
                file.write(line)
