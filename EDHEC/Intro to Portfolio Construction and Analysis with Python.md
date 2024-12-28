## Introduction to Portfolio Construction and Analysis with Python

#Fundamentals of Returns
Price Returns: (Pt+1 - Pt)/Pt
Total Returns: (Pt+1 + Dt,t+1 - Pt)/Pt
Always use annualized returns for data reporting

# Measures of Risk and Reward
For volatility,
variance = average of the square of the deviations from the mean
Standard Deviation = sqrt(variance)
Annualizing Volatility: sd * sqrt(period)
**around 252 trading days per year

# Risk Adjusted Measures
Return on Risk Ratio = Return / Volatility
Sharpe Ratio = [Return - Risk Free Rate]/ Volatility
Excess Return = [Return/Risk Free Rate] = [Return - Risk Free Rate]

Max Drawdown = maximum loss from the previous high to a subsuquent low

# Construct a Wealth Index(buy and hold)
1. Computing drawdowns
2. Look at prior peak at any point in time
*plot the drawdowns over time to see how long it takes to recover from the drawdowns

# Risk Adjustment Ratio Using Ratio
Calmer Ratio = ratio of annualized return over the trailing 36 months to the maximum drawdown over those trailing 36 months

# Deviations from Normality
Skewness = E[(R-E(R))^3]/[Var(R)]^(3/2)
measure of asymmetry of the distribution, symmetric = 0
mean<median = negative skewness -> p(outcome above mean) > p(outcome below mean)

# Kurtosis = E[(R-E(R))^4]/[Var(R)]^2
measure of the thickness of the fatness of the tail
For Gaussian distribution, kurtosis = 3
Fat tail distribution: Kurtosis > 3 
Excess Kurtosis = Kurtosis - 3

Jarque-Bera Test: JB = (n/6)[S^2 + (K-3)^2/4]
goodness-of-fit test of whether sample data have the skewness and kurtosis matching a normal distribution

# Downside Risk Measures 
uncertainty on downside is what investors are most concerned about
Semi-Deviation = volatility of the sub-sample of below-average or below-zero returns ->focuses more on losses 

Value at Risk(VaR) = maximum potential loss threshold (1% worst case is excluded)
->usually express as a positive percentage
->provides an estimation of potentail loss at a given confidence level

# Methods for Computing VaR ( trade-off exists between sample risk and model risk)
**semi parametric = better ,method
1. Historical (non parametric)
->calculation of VaR based on the distribution of historical changes in the value of the current portfolio under market prices over the specified historical obervation window

2. Variance-Covariance ( parametric gaussian)
->calculation of VaR based on portfolio volatility I.E. on volatilities and correlations of components
->example: for a portfolio with a +5% monthly expected return and 4% monthly volatility, the 95% monthly Gaussian VaR for the portfolio = -(.5%-1.65x4%)=6.1%
->Risk: assuming normal distributions may understate risk

3. Parametric Non Gaussian
-> parametric is good because mitigates the prolem of estimation risk at the cost of model risk 

4. Cornish-Fisher VaR (semi parametric)
-> use Cornish-Fisher Expansion -> can relate the Alpha quantile of non Gaussian distribution to the Alpha quantile of the Gaussian distribution
-> in most typical cases where skewness = - and kurtosis>3 -> give a VaR estimate that is higher than the Gaussian estimate->higher chance of getting a bad outcome

# Optimization and The Efficient Frontier
2-Asset Combination
Returns: R(wA,wB) = wA x Ra + wB x Rb
Volatiliy
->two weights != zero , correlation<1 -> volatility of portfolio < weighted average volatilites
-> perfectly correlated = 1 = straight line on graph
-> as correlation increaases, the volatiliy of the minimum possible volatility portfolio increases

Markowitz Optimization using the graph of return against risk -> plot the efficient frontier by either going up or left

Applying Quadprog to draw the Efficient Frontier
->volatility of portfolio of assets depends on covariances between the assets which depends on the volatilitys and  correlations of the assets
->returns of portfolio depends only on the returns of the component assetese and their weights in the portfolio

# Matrix Form Expression for Portfolio Return: Rp = w^T x R
weight vector(w) = k x 1 Vector of weights
R = k x 1 Vecot of assets returns
For Covariance Matrix: diagonal elements = variance of the assets, 
off-diagonal = the cavariances
Quadratic Optimizer:
->supply a set of constraints and an objective function
Objective function: minimize the variance
Constraints: return must be at certain level, all weights > 0 (no shorting), sum(all weights) = 1

** When a risk-free asset is introduced, the efficient frontier dramatically changes shape and become a straight line
Capital Market Line
when introduce risk free assets-> more feasible portfolios

# Tangency Portfolio(Maximum Sharpe Ratio Portfolio)
->at the tangent point of the Capital Market Line with respect to the Markowitz Efficient Frontier
->slope of line =sharpe of the portfolio
->portfolio that maximizes the reward per unit of risk
->contains no zero exposure to specific risk(only systematic risk) = no exposure to unrewarded risks

Parameter Uncertainty
->Key challenge in Portfolio Optimization = estimation error

Improving Estimates for Expected Returns and Covariance Parameters
**some uncertainty always remain which are particularyly large for expected returns
Expected Returns->not always reliable

# Global Minimum Variance Portfolio(better used in practice)
->no expected return parameter is needed = least sensitive to errors in parameter estimates -> only sensitive to errors in risk parameter estimates
->minimize variance without any expected return targets

Markowitz Analysis is hardly used(due to it tendancy to yield unreasonable corner solutions)
Why? Because the presence of parameter estimates

# Diversification
Benefits of Diversification
->eliminating unrewarded idiosyncratic risk
->effective way to increase the reward per unit of risk
Limits of Diversification
->cannot help to diversify away from systematic risk
Hedging 
-> only effective way to obtain downside protection
Insurance = dynamic hedging
->get downside protection while allowing for upside potential

# CCPI Procedure
-> allows for the construction of convex payoffs
->allocates total assets to a risky assets and a safe assets
->ensure downside protection through dynamic allocation to a risk and a safe assets
-> Investment in Risky Assets : multiplier x (cap - 100%) = Initial Allocation%

# Performance Cap and Threshold Process
->impose the smooth-pasting condition
->threshold value = (floor value + ceiling value)/2

Downside Protection
Gap Risk -> materializes if and only if the loss on the risky portfolio relative to the safe portfolio exceeds 1/M within the trading interval

# Stochastic Model for Asset Returns 
->often assumed to follow a random walk
dSt/St = (r + lambda sigma)dt + Standard Brownian Motion Process(sigma d Wt)
sigma d Wt = random walk in continuous time
lambda = sharpe ratio
Drift of the stock index process 
= expected return of the stock index return = risk-free rate + sharpe ratio x volatility

# Browninan Motion
->can be used to construct more complex asset return models with time varying parameters
->follows a normal distribution with zero mean and variance dt
->used as building blocks for generating scenarios for stock returns
**Variance is proportional to time , Volatility scales as the square-root of time

# Monte Carlo Simulation(with time-varying parameters)
For mean-reverting model for interest rate:
current interest rate value < long-term mean value -> interest rate goes up on average (vice versa)
Expected change in interest rate = speed of mean reversion x (diff in current interest rate value and long term mean value)

# Liability Benchmark
->Funding Ratio = value of assets / value of liabilities
->is assets sufficient to cover liabilities
Liability Hedging Portfolio
->investors main concerns = unexpected increase in the present value of their liabilities
->liability hedging portfolios(LHP) or goal-hedging portfolios(GHP) = portfolios with payoffs matching the date and nominal amount of liability/goal payments
Standard bond = not safe with resepect to the goal
Goal hedging portfolio = a retirement bond(high volatile but safe)
When cash-flow matching is not feasible/practical -> use factor exposure matching
safe portfolios = constructed using cashflow matching or duration matching bond portfolios

# Liability-driven Investing(LDI)
-manage risk and performance separately
Performance Generation 
-> optimal exposure to rewarded risk factors -> Performance-Seeking Portfolio(PSP)
PSP: focus on diversified, efficient access to risk premia only
Hedging(against unexpected shocks)
-> Liability-Hedging Portfolio(LHP)
LHP: focus on hedging impact of fisk factors in liabilities
Fund Separation Theorem
->liability risk is taken care of by the presence of the liability hedging portfolio

# Choosing Policy Portfolio
->Optimal Asset Mix of PSP and LHP
RIsk-Aversion Parameter = a free parameter
IN PRACTICE : increase allocation to PSP until risk budget is exhausted
Risk budgets = set by the stakeholders or agent acting on their behalf
**Increasing allocatin to performance-seeking assets->increase in the median value and the dispersion of the funding ratio distribution

# Conflicts 
->between Short-Term and Long-Term perspectives
->between Dollar and Risk Budget
Solutions
->hide the problem by: higher discount rate, higher risk premia value
->solve the problem by: requesting a higher dollar budget(additional contribution), requesting a higher risk budget, improving the performance-seeking portfolio

# Fund Separation Theorem vs Fund Interaction Theorem
LDI Paradigm->investor welfare depends on how good each building block is at delivering
Interaction between performance and hedging motives->play an important role
**Risk-aversion = 1 ->hold 0% for LHP and 100% for PSP
Strong Benefits Expected from: improving hedging, characteristics of the PSP
Substantial value can be added by aligning PSPs and LHPs
Trade-Off between 2 competing effects
1. improve liability friendliness of the PSP
2. allocate more $ to the PSP for the same risk budget
3. improve liability-friendliness of the PSP
4. each $ invested in the PSP may generate a lower performance

# Liability-friendly Equity Portfolios
->Intuitive Approach: based on Cash-Flow Matching Focus
e.g. stocks with high and stable dividends yield
->Statistical Approach: based on Factor Matching Focus
e.g. stocks with low volatility
