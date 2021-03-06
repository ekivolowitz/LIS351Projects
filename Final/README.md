# LIS351 Final
In the `docker build` step, it will copy the code from the current working directory into the container. 
The reason I had to do this is because I didn't want *my* API key to be public on the github.
I apologize that that forces you the reader to do some legwork. 
## Prereqs
1. Create an account with [Etherscan](https://etherscan.io/register).
2. Navigate to [Etherscan's api page and create an access key](https://etherscan.io/myapikey).
Click on "Create a new API-KEY token".
3. Clone this [github repository](https://github.com/ekivolowitz/LIS351Projects).
4. `cd` into `LIS351Projects/Final` and create a file called `secrets.py`. The contents should look like the following:
```python3
AUTH_TOKEN = "<your api token from etherscan.io>"
```
Note that your API key *should* be inbetween quotes as it is a string.

In order to run the project, your directory should be structured like so:
```
.
├── DATA_TYPES.py
├── DB_Api.py
├── EthApi.py
├── README.md
├── app.db
├── dockerfile
├── main.py
├── secrets.py # This is what you have to add exactly as directed.
├── static
│   ├── ETHEREUM-ICON_Black_small.png
│   └── style.css
└── templates
    ├── account.html
    ├── base.html
    ├── block.html
    ├── home.html
    ├── price.html
    ├── search.html
    └── transaction.html

2 directories, 17 files

```
## Building and Running
```bash
docker build -t flaskapp .
docker run -it -p 0.0.0.0:5000:5000 flaskapp
```
## Helpful Information
I suggest looking at `0x8f215bf78d61d45b0d2055dcd60e7c37651ce0ab` for an account address and then following links to get other search fields. 
The url would be
```
http://localhost:5000/address/0x8f215bf78d61d45b0d2055dcd60e7c37651ce0ab
```
Once you have the fields, you can then search them in the search dropdown menu.

Here is the schema fetched from the sqlite3 database: 
![schema](schema.PNG)
## Accessing
Navigate to your favorite web browser and open `localhost:5000`.

Assuming that you have created the `secrets.py` file, you should be able to run the docker container.
I tested it on my Windows desktop, Mac laptop, and Linux (ubuntu 16.04) VM and it ran in all of them. 
