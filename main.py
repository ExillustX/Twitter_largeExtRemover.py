import os
import click

files = []

@click.command()
@click.argument('path')

def main(path):
    for file in os.listdir(path):
        if file.endswith('.jpg_large') or file.endswith('.png_large'):
            files.append(file)
    destructive_feedback = input('Do you really want to rename these files? Press Y to confirm... {}{}'.format('\n', files))
    if destructive_feedback == 'y':
        for file in files:
            os.rename(os.path.join(path, file), os.path.join(path, file[:-6]))
            print('Renaming: ' + file)

if __name__ == '__main__':
    main()