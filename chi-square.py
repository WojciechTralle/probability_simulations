"""Visualizing Chi-square probability density functions in Python."""

from scipy.stats import chi2
import matplotlib.pyplot as plt


def plot_chi_square(nu):
    """
    Plot the probability density function of a Chi-square(nu)
    distribution, where nu is the number of degrees of freedom.
    """

    # Use the 99.9th percentile as the upper plotting limit.
    max_x = chi2.ppf(0.999, df=nu)

    x = [max_x * i / 1000 for i in range(1, 1001)]
    y = chi2.pdf(x, df=nu)

    plt.figure()
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title(f"Chi-square pdf: ν = {nu}")
    plt.grid(True, alpha=0.3)
    plt.show()


if __name__ == "__main__":
    # Experiments
    for nu in [1, 2, 3, 5, 10, 20, 50, 100]:
        plot_chi_square(nu)
        
# Examples

# nu = 12

# P(X <= x)
# print(chi2.cdf(5.23, df=nu))

# P(X > x)
# print(1 - chi2.cdf(5.23, df=nu))

# x such that P(X <= x) = p
# print(chi2.ppf(0.05, df=nu))