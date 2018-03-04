# codejam
A repository for my scripts and solutions to Google Code Jam problems, written in Haskell and Python.
https://code.google.com/codejam/

To run a Python script, pipe an input file into the stdin, e.g. `python -m qualifier.2016_Q_pancakes < sample.in`. Alternatively, run the file with a command-line argument, e.g. `python -m qualifier.2016_Q_pancakes sample.in` or  `python -m qualifier.2016_Q_pancakes sample.in sample.out`.

To run a Haskell script, compile the .hs file, pipe the stdin into the executable, and pipe the standard output to file, e.g. :
```
ghc Tidy.hs && ./Tidy < sample.in > sample.out
```
