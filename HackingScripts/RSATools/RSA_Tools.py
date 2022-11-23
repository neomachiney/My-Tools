#!/usr/bin/python3
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-f', '--file', type=str, help="Incorrect id_rsa file")
parser.add_argument('-o', '--output', type=str, help="Correct id_rsa file (When not specified, .correct of file will be output)")
argv = parser.parse_args()
if not argv.file:
    print("Use --help")
    exit()
if not argv.output:
    argv.output = argv.file + ".correct"

def check_len(id_rsa: str) -> bool:
    data = open(id_rsa, 'r')
    data_list = data.read().splitlines()[1:-2]
    for i in range(len(data_list)):
        if len(data_list[i]) != 70:
            data.close()
            return False
    data.close()
    return True

def correct_rsa(id_rsa: str):
    concat_item = ""
    num_single_line = 70
    corrected_data_list = []
    real_rsa = []

    data = open(id_rsa, 'r')
    data_list = data.read().splitlines()
    header = data_list[0]
    footer = data_list[-1]
    data_list_strip = data_list[1:-1]
    print(f"Stripped : {data_list_strip}")
    for index in range(len(data_list_strip)):
        concat_item += str(data_list_strip[index])
    rsa_single, rsa_broken = (divmod(len(concat_item),num_single_line))
    for i in range(rsa_single):
        corrected_data_list.append(concat_item[:num_single_line])
        concat_item = concat_item[num_single_line:]
    corrected_data_list.append(concat_item)
    data.close()
    real_rsa.append(header)
    real_rsa.append(corrected_data_list)
    real_rsa.append(footer)
    return(real_rsa)


def file_from_list(real_rsa: list, filename: str) -> bool:
    header = real_rsa[0]
    payload = real_rsa[1]
    footer = real_rsa[2]
    try:
        with open(filename, 'w') as f:
            f.write(f"{header}\n")
            for item in payload:
                f.write(f"{item}\n")
            f.write(f"{footer}\n")
        f.close()
        return True
    except KeyboardInterrupt:
        exit(0)
    except:
        return False
def main():
    if check_len(argv.file) == False:
        correct_list = correct_rsa(argv.file)
        file_from_list(correct_list, argv.output)
    else:
        print ("Your File is OK! Connect to the SSH server")
        exit(0)
if __name__=="__main__":
    main()
