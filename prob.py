import scipy.stats as stats

n = 10  # Number of trials
p = 0.16  # Probability of success

# Calculate the probability for each number of successful trials (0 to n)
probabilities = [stats.binom.pmf(k, n, p) for k in range(n+1)]

# Print the probabilities
for k, prob in enumerate(probabilities):
    print(f"Probability of {k} successful trials: {prob}")
