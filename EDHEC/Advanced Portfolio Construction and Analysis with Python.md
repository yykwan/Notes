# Asset Management Paradigm
->Index Investing: Beta , Passive, low cost+index-like
->Low Cost Active: Factor Exposure, Factor Investing, low cost+index-like
->Active Management: Selection and Timing Skill, active, premium priced
Indiciztion = trend of creating new indices that capture the portion of active management that is rule based and systematic + outperform the cap-weighted benchmark in the long run

Nutrient Analogy
-> a factor is a variable which influences the returns of assets
->represents commonality in the returns outside of the individual asset
->exposure to factor risk over the long run yields a reward(the risk premium)
Types of Factors: 
->Macro Factors: growth, inflation
->Statistical Factors: smth extracted from the data that may or may not be identifiable
->Intrinsic Factors / Style Factors: value-growth, momentum, low volatility

Factor Models and the CAPM
->Factor Model = decomposition of the returns of an asset into a set of factor premia
->Factor Premia = returns received in exchange for exposing to a factor
**Eplison in factor model = error term = measure of what might be in the data that is not captured by the factor model
CAPM(predicts alpha term=0)
->excess returnof am asset/risk free rate = (excess return on the market/risk free rate) x beta of the stock
Beta of the stock = covariance of the stock with the market / variance of the market
->various anomalies have explanations that arises from rational risk-based story or a behavioral story
->Rational: high expected returns compensate for negative returns during certain periods(key=defining what those bad times are)
->Behavioral: high expected returns result from agents’ reaction to news
->For some anomalie ->largely rational for others(mostly behavioral)

Multi-Factor models and Fama-French
-sort stocks into deciles based on: size , book/price(measure of value), 
Fama and French(1993) 
-> 3 factor model , factors = market,value,size
SMB = small minus big stocks, HML = high book/price (value) minus low book/price (growth)
->Systematic Factors: small stock effect, value effect -> SMB, HML = zero cost portfolio
**low-vol beats high vol, high quality beats low quality

Sharpe Style Analysis
-> coefficients constraints to sum to 1 (the coefficients are interpretable as weights)
-> can be used to measure Style Drift through a Sliding window analysis over time

Cap-Weighted Indices 
->inefficient portfolios
->tend to be heavily concentrated in a few stocks
Smart(weighted) Benchmarks 
-> fix cap-weighted indices problem(improved risk adjusted performance)

Efficient Harvesting of Equity Risk Premia
Shortcoming
1. 
Problem: CW Indices provide an inefficient diversification of unrewarded and specific risks
Solution: Smarter Weighting Schemes
2. 
Problem: CW Indices provide an inefficient exposure to rewarded systematic risks
Solution: Smart Factor Benchmarks ->better rewarded

Smart Factor Benchmarks Steps
1. Select desired factor exposure(s)
2. Select preferred weighting scheme(s)

Obtaining Efficient Frontier of N Securities
-> estimate N expected returns AND N volatility parameters
-> [N(N-1)/2] Correlations

How to reduce the parameters to estimate?
-> increase sample size ( increase sample period, increase frequency)
-> decrease number of paramters ( decrease the number of assets N, decrease the number of parameters for a fixed N)

Factor Model
-> convenient way to reduce the number of risk parameters to estimate while introducing a reasonable amount of model risk
Implicit Factor Model
-> often preferred since it lets the data tell us what the relevant factors are -> thus alleviating model risk

Statistical Shrinkage
-> equivalent to imposing min/max weight constraints
-> allows one to find the optimal trade-off between sample risk and model risk
-> based on an average of two covariance matrix estimates ( one with high sample risk and one with high model risk)

Volatility changes over time
-> using rolling windows is better than using expanding windows
-> historical volatility estimates are backward looking in nature -> give an estimate for the average volatility over the sample period
Exponentially-weighted average scheme -> assign more weights to more recent observations

ARCH and GARCH Models
-> very convenient but increases the curse of dimensionality
ARCH(T) Model 
-> assign some weight to the long-run variance 
GARCH Model 
-> assign some weight to the previous variance estimate to capture volatility clustering 
GARCH Models: explicitly account for the time-changing nature of volatility -> require additional parameter estimates
A Parsimonious Approach -> consists of mixing them with a factor model -> allowing the variance of the ( uncorrelated ) factors to follow a GARCH model

Sample-Based Estimators
-> may yield misleading expected return estimates by contrasting portfolios with the same final value but different volatility
-> high volatility portfolios produce noisy estimates, leading to large confidence intervals and uncertainty in expected return predictions

Bayesian Statistics as an Alternative
-> differ from frequentist statistics by incorporating prior kowledge about outcomes before analyzing sample data
-> allows for more robust expected return estimates by combining prior beliefs with sample information(especially when sample data is unreliable)

Shrinkage Mean Methodology
-> introduced as a robust prior for estimating expected returns(involves averaging noisy sample estimates with a grand mean)
-> helps improve estimation accuracy(particularly in volatile markets)by reducing the impact of sample variability on expected return calculations

How to understand expected returns?
-> Sharpe ratio: requires expected return estimates for portfolio components(difficult to obtain from sample data)
-> economically motivated priors can improve the estimation of estimation of expected returns, moving beyond the assumption that all returns are equal

Agnostic Priors and their Limitations
-> assuming equal expected returns leads to minimizing volatility(may not align with economic intuition that riskier assets should yield higher returns)
-> more nuanced approach needed to differentiate expected returns based on asset volatility

Factor Models for Better Estimates
-> assets pricing theory suggests that only systematic risk is rewarded, not specific risk that can be diversified away
-> can provide meaningful estimates for expected returns by relating them to systematic risk rather than total risk

Capital Asset Pricing Model (CAPM)
-> the excess expected return of a stock is proportional to its Beta(leads to the Treynor ratio being the same across all stocks)
-> maximize the Sharpe ratio involves optimizing the weighted average of individual stock Betas relative to portfolio volatility
-> Sharpe Ratio = (expected return-risk free rate)/volatility
-> Treynor Ratio = (expected return-risk free rate)/stock beta

Estimation of Expected Returns
-> CAPM-based estimates provide more reasonable expected returns compared to historical mean estimates(may yield unrealistic values)
-> CAPM leads to better portfolio construction, while historical mean estimates can result in extreme and unbalanced portfolios

Multi-Factor Models and Estimation Challenges
-> Arbitrage Pricing Theory generalizes CAPM to a multi-factor setting(requires estimates of excess returns for multiple factors)
-> include assuming equal returns for all factors, using historical data, or relying on active portfolio managers for insights

Black-Litterman Model
-> model helps incorporate active views about expected returns into portfolio construction
-> emphasizes the importance of using a benchmark portfolio as an anchor point for building an active portfolio
-> begins with historical mean returns and CAPM expected returns(highlights the noise in historical estimates)
-> market implied expected returns are extracted, assuming the cap-weighted portfolio is the maximum Sharpe Ratio portfolio

Incorporating Active Views
-> active views can be expressed in absolute or relative terms(allows flexibility in investment strategies) -> confidence levels for these views are set based on the variance of prior estimates(follows classical implementations)

Portfolio Optimization
-> the model allows for the transformation of expected returns into portfolio weights, maximizing the Sharpe Ratio
-> final portfolio reflects the active views while maintaining allocations consistent with the benchmark for assets without expressed views

Expected Returns and Reverse Engineering
-> expected returns are challenging to estimate accurately, making the Black-Litterman model valuable for active portfolio management
-> 1st step involves reverse engineering to extract implied expected returns from a benchmark(serves as a starting point for portfolio optimization)

Combining Active Views with Implied Returns
-> model combines the implied expected returns with active views from managers to create a posterior estimate for expected returns
-> allow a more informed and meaningful portfolio constructin that reflects both market conditions and manager insights

How to understand active views?
-> active views = statements about expected returns on assets, experessed as a normal distribution with a mean and a standard deviation
-> managers express views on certain assets, acknowledging that these views come with varying levels of confidence

Combining Expected Returns
-> Black-Litterman model combines market-implied expected returns with the manager’s active views to create a posterior return vector
-> influenced by the confidence levels in both the benchmark and the active views(allows for a nuanced approach to expected returns)

Implications of Uncertainty
-> if uncertainty about a view increases, model suggests a gradual convergence back to the benchmark expected returns
-> analysis emphasizes that even with low confidence in active views, the portfolio will align closely with the benchmark portfolio over time

How to understand diversification?
-> not concentrating investments in a single asset
-> goal of diversification = achieve a well-rewarded portfolio by balancing investments across various assets

Effective Number of Constituents(ENC)
-> effective number of constituents in a portfolio is not simply the count of assets but considers the allocation of wealth among them
-> A mathematical formula is introduced to calculate ENC, which is the reciprocal of the sum of the squared weights of the assets
-> equal allocation may not lead to a well-balanced portfolio

Global Minimum Variance Portfolio
-> aims to minimize risk without requiring expected return estimates(unique on the efficient frontier)
-> located at the extreme left corner of the efficient frontier graph(represents the lowest risk)

Challenges of Minimum Variance Portfolio
-> while minimizes risk, often leads to a concentrated portfolio(primarily investing in low-volatility assets)
-> concentration can result in lower performace conpared to more diversified portfolios

Improving Minimum Variance Portfolio
-> techniques: imposing a minimum number of contituents can enhance diversification while minimizing variance
-> another method: involve assuming equal volatility among assets, leading to a more balanced portfolio known as the max decorrelation portfolio

How to understand portfolio risk?
-> well-balanced portfolio in terms of dollar allocation may still be concentrated in risk contributions

Calculating Portfolio Variance
-> variance of the portfolio is calculated using the weights and volatilities of the components

Attributing Risk Contributions
-> lies in attributing the risk from the correlation component
-> common method: split the correlation term equally between the stock and bond

How to understand risk parity portfolios?
-> aim for balanced risk contribution rather than equal dollar allocation among assets

Risk Parity Portfolios
-> aims to equalize the risk contribution of each asset, maximizing the effective number of correlated bets
-> focus on equalizing risk contributions

Constructing a Risk Parity Portfolio
-> weights in a risk parity portfolio are inversely proportional to the volatilities of the assets
-> for 2 assets, allocation is adjusted so that the risk contributions from each asset are equal, leading to a more balanced risk profile

Comparison with Equally Weighted Portfolios
-> more efficient in delivering high risk-adjusted performance compared to traditional cap-weighted portfolios
-> can achieve better performance, lower volatility, and reduced maximum drawdown compared to cap-weighted portfolios over time

Key Properties and Applications
-> risk parity portfolios tend to overweight less volatile assets(popular for achieving a balanced risk approach)
-> can be leveraged to match the volatility levels of traditional portfolios, enhancing their practical application in investment strategies

How to understand portfolio variance?
-> portfolio variance is calculated using the weights and covariances of assets, breaking down into contributions from individual asset variances and overlapping covariance terms
-> each asset's contribution to portfolio risk is assessed through its variance and its correlation with other assets
