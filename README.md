# Clove Bounty
We're opening up a developer bounty for the community to help contribute to this project. Clove currently supports the major cryptocurrencies, but we want to support *as many as possible*!

### Bounty amount: 50 TAU per successful pull request
### Knowledge required: Intermediate Python Programming
### Time per task: 15 minutes
### How To:

Your task is to add altcoins that are not in the repo so far. We've done about 100 for you. Select a coin that is NOT in the network folder. Some on the ALTCOINS.txt file may overlap, so double check.

Then, follow the code to the source and scrape the network information from there. It's super easy. Follow these rules.

1. Does the file end in `chainparams.cpp` or `net.cpp`?

If it's the former, just search for `CMainParams()` and then `vSeeds.push_back(CDNSSeedData` inside of the section. Copy all of the `vSeeds` from here. These are the `seeds`. Sometimes there is also a `CTestNetParams()` included in the source code as well. Be sure to copy these as well for the testnet seeds.

Also, copy and paste the port number. In `chainparam.cpp` files, it's stored in a variable called `nDefaultPort`. There are usually two different values for main and test nets. Ignore RegTest network information.

If the file ends in `net.cpp`, then search for the DNS Seeds (https://github.com/adzcoin/adzcoin/blob/master/src/net.cpp#L1191). Copy and paste the **SECOND** value from each pair. The first doesn't matter! Again, do the same for the testnet if one exists below it.

For the port, these will be in `protocol.h` at the top. Note this, the **FIRST** port is the **TESTNET** port, the second is the default. This is counterintuitive, but is a ternary operator so is actually backwards.

2. Copy all of the information into the template.

Check out an example in the networks folder to understand. Make sure you update all metadata like access date, filenames, symbols, etc. etc.

3. Submit your PR.
