# Clove Bounty
We're opening up a developer bounty for the community to help contribute to this project. Clove currently supports the major cryptocurrencies, but we want to support *as many as possible*!

Bounty IOUs
- geeknam, 3 PRs, 150τ, 0x1D32129Dc5A235336Cc4F01Fe41E9b5f97F1261c

### Bounty amount: 50 TAU per successful pull request
### Knowledge required: Intermediate Python Programming
### Time per task: 15 minutes
### How To:

Fork the repo into your Github repository.

Select an entry from the ALTCOINS.txt file. This is a list of the chains that still need to be implemented.

I've selected `https://www.github.com/216k155/lux/blob/master/src/chainparams.cpp` as an example.

Note whether the CPP file is `chainparams.cpp` or `net.cpp.` There are different ways to extract the data for each.

For `chainparams.cpp`, you can find all the information you need in a single file. Search for the `CMainParams` class, and then the CDNSSeedData(https://github.com/216k155/lux/blob/master/src/chainparams.cpp#L144).

Copy the *2nd* entry for each seed, like so:

```
"5.189.142.181",
"5.77.44.147",
"209.250.254.156",
"45.76.114.209",
"luxseed1.luxcore.io",
"luxseed2.luxcore.io",
"luxseed3.luxcore.io",
"luxseed4.luxcore.io"
```

These are your main net seeds.

Now do the same for the `CTestParams` class (https://github.com/216k155/lux/blob/master/src/chainparams.cpp#L188). I found only one seed for this chain (https://github.com/216k155/lux/blob/master/src/chainparams.cpp#L222).

```
"88.198.192.110"
```

Some chains have no testnets.
