import sys

def split_file(file_name):
    with open(file_name, 'r') as f:
        content = f.read()
    
    chunk_size = 127
    num_chunks = (len(content) + chunk_size - 1) // chunk_size
    
    for i in range(num_chunks):
        chunk_content = content[i * chunk_size:(i + 1) * chunk_size]
        with open(f'chunk_{i + 1}', 'w') as chunk_file:
            chunk_file.write(chunk_content)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python splitter.py <input_file>")
    else:
        input_file = sys.argv[1]
        split_file(input_file)
