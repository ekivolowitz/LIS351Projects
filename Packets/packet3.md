# Part 1
1.
```SQL
SELECT * from Furniture;
```
2.
```SQL
SELECT RetailerID from Furniture WHERE FurnitureIsDamaged=True
```
3. 
```SQL
SELECT FurnitureID from (SELECT RetailerID from  Retailer INNER JOIN ON RetailerID FROM Furniture) WHERE FurnitureIsDamaged = True
```
4.
```SQL
SELECT DISTINCT RoomBuilding, RoomNumber FROM Room WHERE RoomManagingDepartment = "LIS" ORDER BY RoomBuilding ASC
```
5.
* `<p>` is a paragraph tag that is simple text grouped together.
* `<b>` is a last resort bold tag that makes the text bold in between the tags. `<strong>` is preferred as of the HTML5 standard.
* `<i>` is an italics tag that italicizes all text in between the tags. `<em>` is preferred as of the HTML standard.
* `<em>` is the preferred italics tag in HTML5.
* `<strong>` is the preferred emboldening tag as of HTML5.
6.
* `<ul>` is an unordered list tag that accepts  `<li>` elements and displays them with bulletpoints instead of numbers.
* `<ol>` is an ordered list tag that accepts `<li>` elements and displays them with an ascending number instead of bullet points.
* `<li>` is a list element that is used to denote children of both `<ul>` and `<ol>` tags.
7.
A `src` and `alt` attributes are required for all `<img>` tags.
8.
```CSS
li {
    font-size: 18pt
}
```
# Part 2
* [part 1](LIS351Packet3/p2_1.png)
* [part 2](LIS351Packet3/p2_2.png)
* [part 3](LIS351Packet3/p2_3.png)
* [part 4](LIS351Packet3/part2_4.png)
* [part 5](LIS351Packet3/p2_5.png)
# Part 3
The HTML validator was very eye opening in how much the browser will fill in for you. For example, the browser will automatically render incomplete tags (tags opened but not closed), tell you errors about why images aren't loading, etc, that we take for granted. The flexibility of a modern web browser is astounding in that in can handle so many different file types, application types (web, mobile android, mobile iOS) etc. Looking back, I will
always use a validator with my HTML because it's such an easy tool to run. This will lead
to consistent results across browsers because the browsers will know how to handle
my code. 
# Part 4
Lots of other students are also CS majors, and had similar errors to mine. The University is pretty good about the pages created for their departments, IE they follow the regulations pretty well. The errors from the other posts were rather trivial, for example duplicate links and type attributes on javascript. 
# Part 5
1. Ethereum
2. I would like to talk about how Ethereum works and why it's a useful cryptocurrency.
3. I was able to put in the core components that describe transactions and accounts on the Ethereum blockchain.
4. possible things to talk about 
* list of accounts and balances
* Search for an account and see transactions for it
These would tie together because you would have a homepage with random accounts pulled from an API, or a search bar to enter an account address, and then you would click on an account and it would bring you to a more detailed page about the ethereum account, and tying in the value of the account based off of a quick calculation from a value queried via an API. 

I would talk about how Ethereum is a future form of computing, and that we should all understand it. If they are interested in a price evaluation, go to the price page. If they want to see accounts, go to the accounts page, or if they want to see a specific account, go to the specific account page. 
5. The colorscheme will be a light gray / white color, with some blues mixed in and black text. 



