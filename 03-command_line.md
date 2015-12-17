# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

>>`pushd` and `popd` - push directory and pop directory. Useful when working in multiple directories at the same time. `pushd` without any argument will switch to the next directory in the stack.

>>`cat` - will print the whole file. This can be useful in redirection to print files together or write to a file.

>>`find` - find files or directories. Will probably be very useful.

>>`grep` - finds things inside files. 

>>`xargs` - takes in a delimited list as an argument for another utility. See q.3 for detailed example.

>>Pipes and redirection - `|`, `<`, `>`, `>>` - Piping the output of the command on the left to the command on the right, send the input from the file on the right to the program on the left, send the output of the program on the left and write it to the file on the right, take the output from the program on the left and appends it to the file on the right.

>>`touch` - make an empty file. Also changes the time on a file.

>>`less` and `more` - ways to view a file in terminal. 

>>`cp` and `mv` - copy or move a file or directory.

---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

>>`ls` lists files and directories in a bare format. `ls -a` lists all files and directories including those which begin with a ".". `ls -l` lists files and directories in long format including the file or directory name, size, modified date and time, owner of file, and it's permission. `ls -lh` lists the same information as `ls -lh` but instead displays the size in human readable format.

---


---

What does `xargs` do? Give an example of how to use it.

>>`xargs` reads delimited strings from the standard input and performs a utility with the strings as arguments. One example of using xargs would be to delete a certain group of files with a similar name or filetype. First you would use `find` to generate a list, and then use `xargs` to take that list as an argument for the `rm` command.
```
$ ls
ex12.txt  oldfile.txt  new file.txt
$ find . -name "*file.txt" -print0 | xargs -0 rm -f
$ ls
ex12.txt
```


---

