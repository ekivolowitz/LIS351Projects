
# Journal4
### URL
The URL for the source code of this project is available here: https://github.com/ekivolowitz/LIS351Projects/tree/master/Journal4
### Assignment Writeup
#### Intentions
I didn't like that I was copy/pasting project setup code from journal to journal, because it would leave artifacts behind. For example, Journal3 has Journal2's heading. I wanted to create a program to generate a new journal for me.
#### Input Work Done
Quickly refreshed myself on `argparse` and then template-ized all the components of a basic project that I've done. Then I wrote some code to handle command line input and generate the desired content.
#### Output Results
This project was generated with `create.py` and then `create.py` and `constants.py` were moved into the directory, so I'd say that it worked pretty well.
#### Approach
I was familiar with `argparse` before this project, and I already knew how to check for file existence, and how to create files/directories. So, I combined all of those pieces together to create this tool. 
#### Thoughts on the results
I'm happy with its outcome, because I'll use it every week to generate a new journal. There's no cooler feeling than using something that you've built. 
### Dependencies
* [python3](https://www.python.org/download/releases/3.0/)

### Usage

```bash
$ python3 create.py Journal4 python --file create.py --purpose "Project to create other LIS351 journal templates." --author "Evan Kivolowitz" --URL "https://github.com/ekivolowitz/LIS351Projects/tree/master/Journal4"
```

### References
* [argparse](https://docs.python.org/3/howto/argparse.html)
* [os](https://docs.python.org/3/library/os.html)
* [flask quickstart](http://flask.pocoo.org/docs/1.0/quickstart/)
