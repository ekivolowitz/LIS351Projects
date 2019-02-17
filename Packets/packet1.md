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
