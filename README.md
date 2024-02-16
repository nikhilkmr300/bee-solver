# bee-solver

This simple script solves The New York Times Spelling Bee challenge. Check it out [here](https://www.nytimes.com/puzzles/spelling-bee).

## How to use

Once you've cloned the repository to your machine, change into the `bee-solver` directory.

Run the script as

```bash
./bee.py
```

or

```bash
./bee.py -d <dict_path>
```

to use with a dictionary of your choice, where `dict_path` is the path to the dictionary. The dictionary must be a file containing alphabetical strings, each word on a new line.

Enter the center character first, then enter the remaining characters, at the respective prompts.

To solve today's live puzzle, run as

```bash
./bee.py -l
```
