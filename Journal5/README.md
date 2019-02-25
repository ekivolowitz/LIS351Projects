
# Journal5
### Case Study Project
I would like to research bitcoin and its price fluctuations throughout time.
### URL
The URL for the source code of this project is available here: https://github.com/ekivolowitz/LIS351Projects/tree/master/Journal5
### Assignment Writeup
#### Intentions
Taking Bryan's feedback from Journal4, I implemented a way to maintain flexibility in journal creation, but also implement automatically naming journal's based on time.
#### Input Work Done
I added a flag to the command line arguments (`--dated`) that will access the `dates.json` file and see what to name the Journal based on time.
#### Output Results
The project worked as expected. My code in J4 allowed for easy extensibility, so I really only had to add the logic for handling the date:
```python3
if args.dated:
    with open("dates.json", "r") as f:
        data = json.load(f)
        now = getDate()
        currDate = datetime.datetime.strptime(now, "%m/%d/%Y")
        journalName = "default"
        previous = None
        for i,date in enumerate(data.keys()):
            print(date)
            loadedDate = datetime.datetime.strptime(date, "%m/%d/%Y")
            if currDate < loadedDate:
                if i > 0:
                    journalName = data[previous]
                else:
                    journalName = data[date] # should be 0
                break
            previous = date
        args.project = journalName
```
The only modification I had to make to in the actual project gen code was:
```python3
if args.dated:
    program_name = args.project + ".py"
```
#### Approach
I wrote a json file with dates of the journals as the key, and journal names as the value. Then I searched the keys in ascending order, finding the first key that was larger than the current date, and used that value as the project name.
#### Thoughts on the results
It was fun to write this code because it made me realize that the code I wrote for the last project was well structured. It took very few changes to implement new functionality.
### Dependencies
* [python3](https://www.python.org/download/releases/3.0/)


### Usage
```bash
$ python3 create.py Journal5 python --dated --purpose "Modification of Journal4 per Bryan's feedback from the grading. This has a flag set so that you can auto create Journal names and default files based on the date." --author "Evan Kivolowitz" --URL "https://github.com/ekivolowitz/LIS351Projects/tree/master/Journal5"
```

### References
* [Journal4](https://github.com/ekivolowitz/LIS351Projects/tree/master/Journal4)
* [DateTime Documentation](https://docs.python.org/3/library/datetime.html)
