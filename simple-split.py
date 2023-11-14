def split_file(input_file, output_path, lines_per_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    total_lines = len(lines)
    file_counter = 1
    start_index = 0

    while start_index < total_lines:
        end_index = min(start_index + lines_per_file, total_lines)
        output_file = f"{output_path}/part_{file_counter}.txt"

        with open(output_file, 'w', encoding='utf-8') as output:
            output.writelines(lines[start_index:end_index])

        start_index = end_index
        file_counter += 1

if __name__ == "__main__":
    input_file_path = "C:/Users/.../Desktop/Dossier/exemple.txt"
    output_directory = "C:/Users/.../Desktop/Dossier/SPLIT"
    lines_per_file = 10000 # A modifier par le nombre de lignes que vous souhaitez

    split_file(input_file_path, output_directory, lines_per_file)
