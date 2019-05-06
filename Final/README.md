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
AUTH_TOKEN = "<your api token from etherscan.io"
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

## Accessing
Navigate to your favorite web browser and open `localhost:5000`.
