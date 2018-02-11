# Clove Bounty
We're opening up a developer bounty for the community to help contribute to this project. Clove currently supports the major cryptocurrencies, but we want to support *as many as possible*!

### Bounty amount: 50 TAU per successful pull request
### Knowledge required: Intermediate Python Programming
### Time per task: 15 minutes
### How To:

1. Fork the repo into your Github repository.

2. Select an entry from the ALTCOINS.txt file. This is a list of the chains that still need to be implemented.

I've selected `https://www.github.com/216k155/lux/blob/master/src/chainparams.cpp` as an example.

3. Note whether the CPP file is `chainparams.cpp` or `net.cpp.` There are different ways to extract the data for each.

For `chainparams.cpp`, you can find all the information you need in a single file. Search for the `CMainParams` class, and then the CDNSSeedData(https://github.com/216k155/lux/blob/master/src/chainparams.cpp#L144).
