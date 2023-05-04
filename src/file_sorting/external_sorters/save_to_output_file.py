import numpy as np

def save_to_output_file(output_filename, array):
    array = sorted(array)
    output_file = open(output_filename, "ab")
    for line in array:
        np.savetxt(output_file, [int(line)], fmt='%1.0f')
    output_file.close()
