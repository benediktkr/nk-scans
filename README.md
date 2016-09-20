# Scanning North Korea

Daily port scans of the three North Korean IP networks. Not really sure what to do with this yet...

https://en.wikipedia.org/wiki/Internet_in_North_Korea

A lot of this looks like honey pots. 

## Networks

 * Star KP: `175.45.176.0/22`
 * KTPC: `210.52.109.0/24`
 * StarGate: `77.94.35.0/24`


## Changes

17/04/2015: Added the StarGate network and added `-P0` and `-oG` on all network scans. Also moved scanning time from 06:00 (GMT+9) to 12:00 (GMT+9) in hopes of catching more interesting network clients. 

18/04/2015: Removed `-P0`, it was taking too long. 

20/04/2015: I'm probably on a list in NK now. 

# Interesting ports

Humans like even numbers and I've found that there are several hosts listening for something on ports 10000, 20000, 30000, 50000.

