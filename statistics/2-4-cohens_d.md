[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> One way to describe the difference between two groups is by comparing mean difference and pooled variability using Cohen's d. In this example we are interested in the total weight in pounds of first born babies as compared to all others. The python code used to compute Cohen's d is shown below:
```
import nsfg
import math


df = nsfg.ReadFemPreg()
firsts = df[df.birthord == 1]
others = df[df.birthord > 1]


def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d

print CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
print CohenEffectSize(firsts.prglngth, others.prglngth)
```
The result is -0.089. This means that the difference in means between first born babies and all others is -0.089 standard deviations. This is small, and not significant enough to assert that first born babies weigh less than others. This is similar to comparing the length of pregnancy between firsts and others with a Cohen's d of 0.029. Again, it is small and not indicative of a meaningful relationship.