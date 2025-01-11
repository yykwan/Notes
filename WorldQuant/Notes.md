# Notes

## Simulation Settings
Instrument Type: Equity<br>
Regions: U.S. , Europe, Asia <br>
Universe = set of trading instruments<br>
Delay = when trade the stock<br>
Decay = linear decay function -> used to reduce turnover<br>
-> Decay-linear(x,n) = x(date)*n + x(date-1)*(n-1)…./n+(n-1)<br>
Truncation = maximum weight for each stock in overall portfolio, recommended: 0.05-0.1<br>
Neutralization: Market / Industry / Sub-INdustry<br>
Pasteurize: replace input values with NaN for instruments not in the Alpha Universe<br>
NaN Handling: replaces NaN values with other values<br>

## Data
Data Field = named collection of data<br>
Matrix = basic type of field with one value of every date and instrument -> no special syntax<br>
Vector = type of field with more than one value for every date and instrument -> needs to be converted into matrix data fields using vector operators before using other operators<br>
Data Value Score = a measure which signifies underutilization of a dataset<br>
Data Coverage = fraction of total instruments present in the universe for which the given data field has a defined value<br>
-> low coverage field? use backfill operators<br>
Vector Data Fields = data fields without fixed sizes<br>
-> number of events recorded per day per instrument varies<br>
Group Data Fields = information about instrument segregation<br>
->used as input to group operator<br>
Group Operators = type of cross-sectional operator that compares stock at a finer level<br>

## Crowding Risk-Neutralized Alphas
Crowding risk = occurs when many investors hold similar positions -> create crowded positions/trades<br>
Problems: unraveling of crowded positions, reduced profitability<br>
Crowding Risk Factors -> for long-short neutralized alphas, insturments with strong momentum<br>
How to simulate? Adjust neutralization to crowding<br>
Code: settings_dict = { “instrumentType” : “Equity”, “region” : “USA”, “universe” : “TOP3000”, “delay”: 1, “decay” : 0, “neutralization”: “CROWDING”, “truncation” : 0.1, “pasteurization”: “ON”, “unitHandling”: “VERIFY”, “nanHandling” : “ON”, “language” : “FASTEXPR”, “visualization” : False }<br>

## Risk Neutralized Alphas
Fama-French Model:  R it - R riskfreereturn = a it + b1 * R marketpremium + b2 * R sizepremium + b3 * R valuepremium + εit<br>
-> if there is significantly positive residual(εit) ->some market anormalies not yet documented<br>
3 Risk Factors’ Sets<br>
1) Slow Factors<br>
->includes market, industry factors and other common lower turnover styles factors<br>
-> for low-turnover signals<br>
2) Fast Factors<br>
-> includes market, industry factors and higher turnover style factors such as reversion alpha<br>
-> for high-turnover signals<br>
3) Slow + Fast Factors<br>
-> for high-turnover signals<br>
2,3-> beneficial where increases in turnover comes with an increase in Sharpe<br>

## Basic Statistics for Data Analysis
Moments = mathematical indicators that represent various characteristics of data distribution<br>
![](WorldQuant/2. Ist Moment (Mean).png)<br> 
Variance = np.var(data)<br>
->measures how spread out data values are from the mean<br>
Standard Deviation = np.std(data)<br>
-> square root of the variance represents the variability of the data<br>
Skewness = skew(data) - need import scipy.stats<br>
-> measures the asymmetry of data distribution<br>
-> positive skewness: heavy right tail ; negative skewness: heavy left tail<br>
Kurtosis = kurtosis(data) - need import scipy.stats<br>
-> measure the tail thickness of a distribution<br>
Covariance = df.cov() ; df=pd.DataFrame({‘A’:[1,2,3],’B’:[4,5,6]})<br>
-> measures the relationship between changes in two variables<br>
Correlation = df.corr(method=‘pearson’)<br>
-> measures the linear relationship between two variables<br>
Quantile = np.percentile(data, [25,50,75])<br>
-> a reference value that divides data into equal intervals<br>

## Handling Missing Values
Types of missing values: <br>
1) MCAR ( Missing Completely At Random) -> missing values occur completely randomly and are independent of other variables or outcomes<br>
2) MAR ( Missing At Random) -> missing values are associated with a specific variable but are unrelated to the outcome variable<br>
3) NMAR ( Not Missing At Random) -> missing values are related to the characteristics of the data itself<br>
How to Handle:<br>
1) Delete Data -> remove rows/columns that contain missing values<br>
2) Imputation -> replace missing values with teh mean of the column(mean, median, mode, K-NN IMputation, MICE(Multiple Imputation by Chained Equations): Imputation of missing values using multiple iterative models, Deep Learning-based Imputation: predict missing values using neural networks)<br>
3) Model-based Replacement -> set the variable with missing values as the dependent variable, and use other variables as independent variables to create a prediction model to replace the missing values<br>
4) Marking the Missing Value -> mark missing value as 0,-1, or as separate labels<br>
Considerations when handling missing data<br>
1) Identify patterns in missing data<br>
2) Minimize data loss<br>
3) Align with analysis goals<br>

## Tests of Statistical Hypotheses
Types of Hypothese<br>
1) Null Hypothesis(H0) -> indicates a basic assumption or current state<br>
2) Alternative Hypothesis(H1) -> opposite hypothesis to H0<br>
Testing Procedure<br>
1) Hypothesis setting -> define H0 and H1<br>
2) Setting the Significance Level(a) -> the probability of allowing an error<br>
3) Calculating test statistics -> calculate statistics(T-statistic, Z-statistic…)<br>
4) Calculating the P-value -> the probability that the observed result would occur under H0-<br>
5) Drawing a conclusion -> evalute the validity of the hypothesis by rejecting or failing to reject H0-<br>
Major Statistical Testing Methods<br>
1) **T-Test** -> used to compare differences between means<br>
->One-Sample T-Test: compare the samples mean with a specific value<br>
->Independent Two-Sample T-Test: compare the means of two independent groups<br>
->Paired T-Test: compare pre- and post-data of the same group<br>
2) **ANOVA(Analysis of Variance)** -> used to test the difference in means among three or more groups<br>
->One-Way ANOVA: evaluate differences among multiple levels of one factor(indeppendent variable)<br>
->Two-Way ANOVA: analysis including two independent variables and their interaction effects<br>
3) **Chi-Square Test** -> compares observed frequencies with expected frequencies in categorical data<br>
->Test of independence: evaluate the relationship between two categorical variables<br>
->Goodness-of-fit test: verify if the ovserved frequencies follow a specific distribution<br>
4) **Correlation Test** -> evaluates the linear relationship between two variables<br>
->Pearson Correlation, Spearman Correlation(measure rank correlation), Kendall Correlation(measure based on consistency and inconsistency between variables)<br>

## Portfolio Optimization
Objectives: balance between risk and return, maximize diversification effects, tailored asset allocation for investment goals<br>
1) **Markowitz Mean-Variance Optimization**<br>
-> optimizes the trade-off between risk and return and provides optimal asset allocation through the efficient frontier<br>
!(WorldQuant/Key Concepts.png)
2) **Black-Litterman Model**<br>
-> integrates market equilibrium and investor beliefs for realistic portfolio construction<br>
!(WorldQuant/given return level.png)
3) **Risk Parity**<br>
-> asset allocation strategy designed to equalize the contribution of each asset to the overall portfolio risk: lowering weights of volatile assets while increasing weights of less volatile assets to enhance stability<br>
!(WorldQuant/Key Concepts.png)

## Outlier Detection in Financial Time Series Data
Why need detect? degraded model performace, errors in risk management, distorted analytical resulty<br>
Types of Outliers:<br>
1) Univariate Outliers: a value in a single variable deviates from the normal distribution<br>
2) Multivariate Outliers: the relationship between multiple variables indicates abnormality<br>
3) Contectual Outliers: abnormal data points when viewed in the context of time or other environmental factors<br>
4) Collective Outliers: data points that are normal individually but exhibit abnormal patterns when grouped<br>
Outlier Detection Methods<br>
1) **IQR(Interquartile Range)**<br>
-> identifies outliers based on quartiles, uses the middle range of the data for detection<br>
-> Calculation Method: IQR=Q3-Q1 , Lower Bound=Q1-1.5IQR, Upper Bound=Q3+1.5IQR<br>
-> Adv: simple and intuitive, Disadv: accuracy decreases for asymmetrical data<br>
2) **Z-Score**<br>
-> measures how many stds a data point is from the mean<br>
-> Calculation Method: (X-mean)/std<br>
-> Adv: effective for symmetric data distributions, clear detection criteria, Disadv: not reliable for skewed data or when extreme values distort the mean and the std<br>
3) **LOF(Local outlier Factor)**<br>
-> destiry-based method that compares the density of a data point to its neighbors to detect outliers<br>
-> Calculation Method: calculate the k-nearest neighbors for each data point, compare the density of the point to the density of its neighbors, points with significantly lower densities are identified as outliers<br>
-> Adv: works well with non-linear data, effectively detects outliers in low-density regions, Disadv: conputationally expensive, results sensitive to k choice<br>
4) **Isolation Forest**<br>
-> detects outliers by randomly isolating data points, easier to isolate=outliers<br>
-> Calculation Method: perform random splitting to isolate data points, calculate the path length(number of splits) for each point, points with shorter path lengths are considered outliers<br>
-> Adv: effective for high-dimensional data, fast for large datasets, Disadv: requires pre-setting the contamination rate(percentage of outliers) which is challenging<br>

## Detecting Outliers in Real Market Data
1) **Data Collection and Preprocessing**<br>
import yfinance as yf<br>
import pandas as pd<br>
#Data Collection<br>
ticker = “AAPL”<br>
data = yf.download(ticker, start=“2018-01-01”, end=“2023-01-01”)[“Close”]<br>
#Calculate returns<br>
returns = data.pct_change().dropna()<br>
returns.name = “Returns”<br>
print(“Returns Head:\n”, returns.head())<br>
2) **Outlier Detection Using IQR**<br>
#Calculate IQR<br>
Q1 = returns.quantile(0.25)<br>
Q3 = returns.quantile(0.75)<br>
IQR = Q3 - Q1<br>
lower_bound = Q1 - 1.5 * IQR<br>
upper_bound = Q3 + 1.5 * IQR<br>
#Detect outliers<br>
outliers_iqr = returns[(returns < lower_bound) | (returns > upper_bound)]<br>
#Print dates and values of outliers<br>
print("IQR Outliers:")<br>
for date, value in outliers_iqr.items():<br>
    print(f"Date: {date}, Outlier Value: {value}")<br>
3) **Outlier Detection Using z-score**<br>
from scipy.stats import zscore<br>
#Calculate Z-Score<br>
z_scores = zscore(returns)<br>
outliers_zscore = returns[abs(z_scores) > 3]<br>
#Print dates and values of outliers<br>
print("Z-Score Outliers:")<br>
for date, value in outliers_zscore.items():<br>
    print(f"Date: {date}, Outlier Value: {value}")<br>
4) **Outlier Detection Using LOF**<br>
from sklearn.neighbors import LocalOutlierFactor<br>
#LOF model<br>
lof = LocalOutlierFactor(n_neighbors=20, contamination=0.05)<br>
outliers_lof = lof.fit_predict(returns.values.reshape(-1, 1))<br>
#Detect outliers<br>
outliers_lof_index = returns.index[outliers_lof == -1]<br>
lof_outliers = returns.loc[outliers_lof_index]<br>
#Print dates and values of outliers<br>
print("LOF Outliers:")<br>
for date, value in lof_outliers.items():<br>
    print(f"Date: {date}, Outlier Value: {value}")<br>
5) **Outlier Detection Using Isolation Forest**<br>
from sklearn.ensemble import IsolationForest<br>
#Isolation Forest model<br>
iso_forest = IsolationForest(contamination=0.05, random_state=42)<br>
outliers_iso = iso_forest.fit_predict(returns.values.reshape(-1, 1))<br>
#Detect outliers<br>
outliers_iso_index = returns.index[outliers_iso == -1]<br>
iso_outliers = returns.loc[outliers_iso_index]<br>
#Print dates and values of outliers<br>
print("Isolation Forest Outliers:")<br>
for date, value in iso_outliers.items():<br>
    print(f"Date: {date}, Outlier Value: {value}")<br>
