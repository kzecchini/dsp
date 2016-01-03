[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

>> In this question, we begin by sumlating a drawing of sample size n = 10 from an exponential distribution with lambda = 2. This experiment is simulated 1000 times. The standard error and a 90% confidence interval are calculated. The experiment was repeated with increasing values the sample size. We see that as n increases, standard error decreases. We also see that the confidence interval therefore decreases. The true value of lambda = 2 is present in every confidence interval constructed. A table of values is shown below:

n | Standard Error | 90% Confidence Interval
- | -------------- | -----------------------
10 | 0.877500275721 | (1.2567398346141148, 3.8097768787167823)

50 | 0.295196462143 | (1.5883914609261527, 2.5555610022931874)

100 | 0.202574294314 | (1.7006691299126004, 2.3596017547167221)

500 | 0.0897126938355 | (1.8645681524178541, 2.1555698575055171)

1000 | 0.0614363330403 | (1.8996704108770956, 2.1017648588958959)
2000 | 0.0438949273657 | (1.9317340581575793, 2.0734398183883354)

>> Plots were made for the sampling distribution of the estimator L for each value of n. An example of the sampling distribution for n = 500 is shown. The other sampling distributions can be found in the [images folder](img).

<img src="chap08sampleestimation500.jpg" title="Simulated Sample n = 500"/>

>> Additionally, the standard error was plotted against sample size. The relationship is non linear. The standard error decreases rapidly for a sample size between 10 and 100. Then it begins to have a much smaller slope for larger values of n.

<img src="chap08stderrvsn.jpg" title="Standard Error vs. n"/>

>> The code used to produce these results is shown below:

```
    from __future__ import print_function

    import thinkstats2
    import thinkplot

    import math
    import numpy as np


    def RMSE(estimates, actual):
        """Computes the root mean squared error of a sequence of estimates.

        estimate: sequence of numbers
        actual: actual value

        returns: float RMSE
        """
        e2 = [(estimate-actual)**2 for estimate in estimates]
        mse = np.mean(e2)
        return math.sqrt(mse)


    def SimulateSample(lam=2, n=10, m=1000):
        """Plots the sampling distribution of the L estimator for an exponential parameter.

        lam: lambda value for exponential distribution
        n: sample size
        m: number of iterations
        """
        def VertLine(x, y=1):
            thinkplot.Plot([x, x], [0, y], color='0.8', linewidth=3)

        estimates = []
        for _ in range(m):
            xs = np.random.exponential(1.0/lam, n)
            lamest = 1.0/np.mean(xs)
            estimates.append(lamest)

        cdf = thinkstats2.Cdf(estimates)
        stderr = RMSE(estimates, lam)
        ci = (cdf.Percentile(5), cdf.Percentile(95))

        VertLine(ci[0])
        VertLine(ci[1])

        # plot the CDF
        thinkplot.Cdf(cdf)
        thinkplot.Save(root='chap08sampleestimation%d' % n,
                       xlabel='Sample Mean',
                       ylabel='CDF',
                       title='Sampling Distribution for n = %d' % n)

        return [stderr, ci]


    def main():
        stderr = []
        ns = [10, 50, 100, 500, 1000, 2000]
        for n in ns:
            result = SimulateSample(n=n)
            stderr.append(result[0])
            print (n, result[0], result[1])
        thinkplot.Plot(ns, stderr)
        thinkplot.Save(root='chap08stderrvsn',
                       xlabel='Number of Samples',
                       ylabel='Standard Error',
                       title='Sample Size vs. Standard Error')


    if __name__ == '__main__':
        main()
```
