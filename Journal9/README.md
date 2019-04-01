# Journal9
### URL
The URL for the source code of this project is available here:
 https://github.com/ekivolowitz/LIS351Projects/tree/master/Journal9
### Assignment Writeup
#### Intentions
I've been doing some work with AWS, in particular hosting a static page through their Simple Storage Solution service (s3).
I've created some scripts to automate the process of redeploying to the s3 bucket.
#### Input Work Done
Shifted over aws commands from bash to python.
#### Output Results
Generic script to upload to an s3 bucket of your choosing.
#### Approach
I used argparse to get the directory that you'd like to sync, and then shifted my aws shell commands into python.
#### Thoughts on the results
It made some work I had to do today easier, so I'm quite content with the output.
### Dependencies
* [python3](https://www.python.org/download/releases/3.0/)
### Usage

```bash
$ python3 Journal9.py directory/
```
### References
None
