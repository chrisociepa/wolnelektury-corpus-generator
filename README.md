# wolnelektury-corpus-generator

The aim of this repository is to provide a script that allows for a simple and fast way to download all books in txt format and save them to disk. These books can be further used in accordance with the rules described on [wolnelektury.pl](https://wolnelektury.pl/info/zasady-wykorzystania/).

## Dependencies:

- Python 3
- [tqdm](https://pypi.org/project/tqdm/)

## Run

Using the `collect.py` script, you can easily download all ebooks in the txt format from wolnelektury.pl using their API. Here's an example of how to run it (make sure the `books/` directory exists or change the path in the script - `TXT_FILES_DIR`):

```
$ python collect.py
```

Correct, as simple as that :)
