# Adwords-Placing
## Adwords Placing Problem via Online Bipartite Graph Matching


### Problem
We are given a set of advertisers each of whom has a daily budget 𝐵𝑖. When a user performs a query, an ad request is placed online and a group of advertisers can then bid for that advertisement slot. The bid of advertiser 𝑖 for an ad request 𝑞 is denoted as 𝑏𝑖𝑞. We assume that the bids are small with respect to the daily budgets of the advertisers (i.e., for each 𝑖 and 𝑞, 𝑏𝑖𝑞≪𝐵𝑖). Moreover, each advertisement slot can be allocated to at most one advertiser and the advertiser is charged his bid from his/her budget. The objective is to maximize the amount of money received from the advertisers.

For this project, we make the following simplifying assumptions:
1. For the optimal matching (used for calculating the competitive ratio), we will assume everyone’s budget is completely used.
2. The bid values are fixed (unlike in the real world where advertisers normally compete by incrementing their bid by 1 cent).
3. Each ad request has just one advertisement slot to display.


### Datasets
We are provided with a small dataset called bidder_dataset.csv. This dataset contains information about the advertisers. There are four columns: advertiser ID, query that they bid on, bid value for that query, and their total budget (for all the keywords). The total budget is only listed once at the beginning of each advertiser’s list.
In addition, the file queries.txt contains the sequence of arrivals of the keywords that the advertisers will bid on. These queries will arrive online and a fresh auctioning would be made for each keyword in this list.

### Project Requirements
For this project, we implement the Greedy, MSVV, and Balance algorithms as described below. The code also calculates the revenue for the given keywords list (in that order) as well as calculate an estimation of a competitive ratio. The competitive ratio is defined as the minimum of 𝐴𝐿𝐺/𝑂𝑃𝑇, where 𝐴𝐿𝑇 is the mean revenue of your algorithm over all possible input sequences and 𝑂𝑃𝑇 is the optimal matching. To estimate the value of 𝐴𝐿𝐺, we simply compute the revenue over 100 random permutations of the input sequence and calculate the mean value.

### Project Details:
● Use either python or R for your implementation. Your file should be called either adwords.py or adwords.R
● The code takes one argument as input, which will denote which algorithm to run. The input arguments will be given as: greedy, balance, or msvv.
● The code writes to the console the calculated revenue using the chosen algorithm on queries.txt as given as well as the estimation of the competitive ratio. We simply print these two numbers on two separate lines.
● NOTE: At some points in the algorithms below, two or more advertisers will tie for an advertisement slot. In this case, we choose the advertiser with the smallest ID.

### Greedy:
1) For each query 𝑞
  a) If all neighbors (bidding advertisers for 𝑞) have spent their full budgets
    i) continue
  b) Else, match 𝑞 to the neighbor with the highest bid.

### MSVV:
Let 𝑥𝑢 be the fraction of advertiser's budget that has been spent up and 𝜓(𝑥𝑢) = 1−𝑒(𝑥𝑢−1).
1) For each query 𝑞
  a) If all neighbors have spent their full budgets
    i) continue
  b) Else, match 𝑞 to the neighbor 𝑖 that has the largest 𝑏𝑖𝑞∗𝜓(𝑥𝑢) value.

### Balance:
1) For each query 𝑞
  a) If all neighbors have spent their full budgets
    i) continue
  b) Else, match 𝑞 to the neighbor with the highest unspent budget. 
