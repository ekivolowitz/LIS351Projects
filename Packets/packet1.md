# Packet 1
## Part 1
1. The Operating System is most responsible for how files are stored on the hard drive.
2. A word is 4 bytes, which is 32 bits.
3. -86 
```
-128 + 32 + 8 + 2
-118 + 32 
-86
```
4. Say that people that really like Gushers also often purchase and really like Fruit by 
the foot. That puts Gushers and Fruit by the Foot in the same neighborhood. Then there is some
way of measuring distance between items, like the difference per user of rating of both of these
items. This is then collected and spread over all of the reviews. Items with a very small distance
are then suggested, thus, item to item recommendation.
5. A user to user recommendation scores a recommendation between two people as the sum of the differences of their reviews. So, if two people score one item identically, their recommendation score is 0. If they then rate another item as a 5, and a 3, then their score becomes 2 (absolute value of 5 - 3). Recommendations of what people with low scores have purchased will then be given.
6. ASCII can only hold up to 128 characters, which can't contain all of the emojis and non ASCII characters from other languages. To only render ASCII and not UTF-8 would make the web inaccessible for many people.
7. A local IP address is one assigned to your device from your router or switch. That's different from the public IP address because it's not publically viewable to anyone off your network. You must also be connected to the same switch or router to see your machine's local IP. A public IP is one assigned to you by your ISP (it may change unless you request a static) so that they can route your traffic to you. 
8. There are 13 route nameservers.
9. Your phone is the client and Facebook's servers is the server.
10. A sampling rate is the number of audio samples of an analog signal per second. The higher the sampling rate of a track, the closer of an approximation your digital signal is to the original analog signal. 
11. That color would be primarily red, but a lighter tone probably skewing more towards a pink.
12. They would be able to zero in on your identity by querying all students that have taken LIS351 in the spring of 2019, who are in a certain section, who have scored the exact score provided in the class data.
13. There are magnetic discs called platters, a needle head, an arm, and a rotor to spin the discs at a certain speed.
## Part 2
1. `rockhopper-01.cs.wisc.edu` IP address: 128.105.37.191, Public IP Address: 128.105.37.255. `rockhopper-02.cs.wisc.edu` IP address: 128.105.37.192, Public IP Address 128.105.37.255
I found that the IPs are similar except for the least significant placeholder, the 191 and 192. Also both the Public IP Addresses are the same. This doesn't surprise me because I would expect that all the machines in a lab would be tied to some sort of switch, which we are seeing the public IP for. No number is higher than 255 either.
2. `ISLAB18m` Private IP address: 128.104.96.68, Public IP address: 128.104.97.255
`rockhopper-01.cs.wisc.edu` Private IP Address: 128.105.37.191, Public IP Address: 128.105.37.255
No number is higher than 255. The Private IPs are both different, which makes sense as they're on different parts of campus,  receiving different DHCP leases. The Public IPs both end in 255 as well.
3. I think that I got these results because the computers are not linked on the same switch, or going through the same router, or tied to the same upstream link. 
4. All 9 of the first results are me, so 100%.
5. You could use a google hack, like `site: facebook.com "Evan Kivolowitz"`

## Part 3
### What do I have inside my home that is worth protecting?
Things that I would like to protect
* Clothes
* Computer equipment
* Phone
* Headphones
* Tablet
* Books
* TV

These answers were derived in terms of things that are somewhat expensive and how often they are used. Clothes and computers are then obviously at the top.
### Who do I want to protect it from?
Certain objects I protect more than others. For example, I'm ok with my friends borrowing my clothes, TV, or books, but not my computer, iPad, or headphones. I would categorize who I want to protect my possessions from into three categories.
* Family
* Friends
* Not Friends or Family
Each category gains stricter protections. I would lend anything to my family should they ask for it, some things to my friends, and nothing to people I do not know.
### How bad are the consequences if I fail?
If I fail to protect my possessions, the consequences could be very bad. In the worst case, I could lose them entirely. Equally as bad, a bad actor could destroy my possessions.
### How likely is it that I will need to protect it?
I take preventative measures which reduces the likelihood that I will need to protect my possessions. For example, my door is always locked. I don't leave my possessions in public places without me being with it.
### How much trouble am I willing to go through to try to prevent potential consequences?
As mentioned in the previous question, I make small amounts of effort concentrated in the right ways to ensure that I won't have trouble come up in the future. Should someone steal a non serialized object (clothes, books, or headphones), I would see if I could get footage of them being stolen. Should a higher value, serialized object be stolen, I would go the cops with my information about where I last saw the item, its unique identifying information (MAC address, Serial Number, etc.) which I have all backed up elsewhere.
## Part 4
### Discussion 1.1
Of the ~ 10 responses that I looked at, 6 of them said that they saw a representative example of their major in the photos, meanwhile 4 of them said they did not. It was interesting to see that the responses I looked at, they reported that they expected to see more white men in the images, (representative of their experience), or that they saw a good distribution of sex and race, but a poor distribution of age, which was in line with their experience.
### Discussion 1.2
A lot of people understand the idea of a schema, I think; I'm interested to see how they handle it in the context of a database table. Something that would be interesting to see is how people comprehend the idea of SQL and queries, and requirements for schemas. For example, most RDBMS's require a unique identifier, which we did not. How would we apply that in a meaningful way to this project? 
### Discussion 1.3
Something that I've seen in almost every post is the notion of using a password manager to protect their accounts. This is a good practice, and it's one that I use, but the buck doesn't stop there. The best a password manager can do is prevent one exploited site's password from being known and used in another site to log in for you. Password security, in my opinion, is really only 10% on us as users. The majority of the work is done by the sites we visit, and we are at their mercy. We trust that they salt their passwords, and use up to date, publically vetted cryptographic functions, and that they require TLS (HTTPS) connections instead of pure HTTP. 