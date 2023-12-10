import pypandoc
import os

# Directory containing your .rst files
source_dir = 'aiogram/docs/'
target_dir = 'aiogram_docs/'

for root, dirs, files in os.walk(source_dir):
    for file in files:
        if file.endswith('.rst'):
            source_file = os.path.join(root, file)
            relative_path = os.path.relpath(root, source_dir)
            output_dir = os.path.join(target_dir, relative_path)

            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            target_file = os.path.join(output_dir, file.replace('.rst', '.md'))

            # Create an empty file if it doesn't exist
            if not os.path.exists(target_file):
                open(target_file, 'a').close()

            try:
                pypandoc.convert_file(source_file, 'md', outputfile=target_file)
                print(f'Converted {source_file} to {target_file}')
            except Exception as e:
                print(f"Error converting {source_file}: {e}")


