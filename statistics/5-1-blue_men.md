[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> As a part of the Behavioral Risk Factor Surveillance System, respondents were interviewed and asked questions about their demographics. Based on the data, a normal model with mean 178.0 cm and standard deviation 7.7 cm can approximate the distribution of male height. The Blue Man Group only accepts male applicants who are between 5' 10" and 6' 1" tall. We can calculate the percentage of men who qualify based on height through two methods. The first method is using the cdf of the normal distribution and evaluating it at 177.8 cm and 185.4 cm as the lower and upper bounds. We have:
```
import scipy.stats
mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
lower = dist.cdf(177.8)
upper = dist.cdf(185.4)
return lower, upper, upper-lower
```
We get values of lower = 0.48963902786483265, upper = 0.83173371081078573, and the difference of 0.34209468294595308. This means that about 34.32% of the male population lies in the range eligible for the Blue Man Group.

>> A different approach to this problem would be to perform a hypothesis test on the distribution. We could say the hypotheses are H0: 177.8 < mu < 185.4 and H1: (mu < 177.8) or (mu > 185.4). We will use a significance level of alpha = 0.05. Our test statistic would be two Z scores for the upper and lower bounds:
>>> Zlow = (177.8 - 178.0)/7.7 = -0.025974025974024498 <br/>
Zhigh = (185.4 - 178.0)/7.7 = 0.9610389610389618

>> The range we are looking for is P(-0.0260 < Z < 0.9610) = 0.83173371081078573 - 0.48963902786483265 = 0.34209468294595308
Again we see the same result of about 34.32% of the male population lies within the range eligible for the Blue Man Group. And since the p-values are much larger than the significance level, we fail to reject the null that the mean does lie within this range.
