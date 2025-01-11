# Operators
## Arithmetic
1) abs(x) -> absolute value of x<br>
2) add(x,y,filter-false), x+y -> add all inputs, if filter=true -> filter all NaN=0 beforehand<br>
3) densify(x) -> converts grouping field of many buckets into lesser number of only available buckets -> higher efficiency<br>
4) divide(x,y) , x/y<br>
5) inverse(x) -> 1/x<br>
6) max(x,y,…)<br>
7) min(x,y,..)<br>
8) multiply(x,y…,filter=False) -> filter sets NaN values =1<br>
9) power(x,y)<br>
10) reverse(x) -> -x<br>
11) s_log_1p(x) -> confine function to a shorter range using log<br>
12) sign(x) -> if input = NaN ; return NaN<br>
13) signed_power(x,y) -> sign(x)*(abs(x)^y)<br>
14) subtract(x,y,filter=false) , x-y -> if filter=true -> filter all input NaN to 0 before subtract<br>
## Logical
1) and(input1,input2)<br>
2) if_else(input1, input2,input3)<br>
3) input1 <= input2<br>
4) input1 == input2<br>
5) input1 > input 2<br>
6) input1 >= input2<br>
7) input1 != input2<br>
8) is_nan(input) -> if (input==NaN) return 1 else return 0 <br>
9) not(x)<br>
10) or(input1,input2)<br>
## Time Series
1) days_from_last_change(x) -> amount of days since last change of x<br>
2) hump(x, hump = 0.01) -> limits amount and magnitude of changes in input -> reduces turnover<br>
3) inst_tvr(x,d) -> Total trading value/Total holdng value in past d days<br>
4) last_diff_values(x,d) -> returns last x value not equal to current x value from last d days<br>
5) ts_arg_max(x,d) -> returns the relative index of the max value in the time series for the past d days<br>
6) ts_arg_min(x,d) -> returns the relative index of the min value in the time series for the past d days<br>
7) ts_av_diff(x,d) -> returns x-tsmean(x,d), but ignore NaNs during mean computation<br>
8) ts_backfill(x, lookback=d, k=1, ignore = “NaN) ->replace NaN or 0 values with meaningful value<br>
9) ts_decay_exp_window(x,d,factor=f) -> returns exponential decay of x with smoothing factor for the past d days<br>
10) ts_delay(x,d) -> returns x value d days ago<br>
11) ts_delta(x,d) -> returns x-ts_delay(x,d)<br>
12) ts_delta_limit(x,y,limit_volume = 0.1) -> limit the change in the Alpha position x between dates to a specified fraction of y (range of 0-1)<br>
13) ts_mean(x,d) -> returns average value of x for the past d days<br>
14) ts_median(x,d) -> returns median value of x for the past d days<br>
15) ts_product(x,d) -> returns product of x for the past d days<br>
16) ts_quantlie(x,d,driver=“gaussian”) -> calculates ts_rank and apply an inverse cumulative density function from driver distribution<br>
-> Drivers: “ gaussian”, “uniform” , “cauchy” distribution<br>
17) ts_rank(x,d,constant=0) -> rank values of x for each instrument over the past d days, return rank of current value + constant<br>
18) ts_scale(x,d,constant=0) -> returns (x-ts_min(x,d))/(ts_max(x,d)-ts_min(x,d))+constant<br>
19) ts_std_dev(x,d)<br>
20) ts_sum(x,d)<br>
21) ts_zscore(x,d) -> reduces outliers and drawdown<br>
22) ts_corr(x,y,d) -> returns correlation of x and y for past d days<br>
23) ts_count_nans(x,d) -> returns the number of NaN values in x for past d days<br>
24) ts_covariance(y,x,d) -> returns covariance of y and x for the past d days<br>
## Cross Sectional 
1) normalize(x,useStd=false,limit=0.0) -> calculates mean value of all valid alpha values for a certain date, then subtracts mean from each element<br>
2)quantile(x,driver=gaussian,sigma=1.0) -> rank raw vector, shift ranked Alpha vector, apply distribution(gaussian, uniform, cauchy)<br>
-> if uniform, subtract each Alpha value with mean of all Alpha values in the Alpha vector<br>
3) rank(x, rate=2) ->precise sort->rate=0; -> rank input among all instrument and returns an equally distributed number between 0.0 and 1.0<br>
4) regression_neut(y,x) -> conduct cross-sectional regression on stocks with Y as target and X as independent variable<br>
5) scale(x, scale=1, longscale=1, shortscale=1) -> scales input to booksize<br>
6) truncate(x, maxPercent=0.01) -> truncates all values of x to maxPercent<br>
7) winsorize(x, std=4) -> winsorizes x to make sure all values in x are between lower and upper limit (multiples of std)<br>
8) zscore(x) -> (x-mean(x))/std(x) ; -> measures how unusual a data point is in relation to the mean<br>
## Vectors
1) vec_avg(x) -> mean of vector field x<br>
2) vec_count(x) -> number of elements in vector field x<br>
3) vec_sum(x) -> sum of vector field x<br>
## Transformational
1) bucket(rank(x),range=“0,1,0.1” or buckets=“2,5,6,7,10”) -> converts float values into indexes for user-specified buckets<br>
2) left_tail(x, maximum=0) -> NaN everything greater than maximum<br>
3) right_tail(x, minimum=0) -> NaN everything less than minimum<br>
4) trade_when(x,y,z) -> change Alpha values only under a specified condition; <br>
-> can close Alpha positions(assign NaN) under specified condition<br>
## Group
1) group_backfill(x,group,d,std=4.0) -> if a certain value for a certain date and instrument is NaN, from the set of same group instruments, calculate winsorizeed mean of all non-NaN values over last d days<br>
2) group_mean(x, weight, group) -> all elements in group equal mean<br>
3) group_median( x, group) -> all elements in group equal to median value of group<br>
4) group_neutralize(x,group) -> neutralize Alpha against group<br>
5) group_normalize(x, group, constantCheck=False, tolerance=0.01, scale=1) -> normalizes input such that each group absolute sum = 1<br>
6) group_rank(x, group) -> each elements in a group is assigned the corresponding rank in this group<br>
7) group_zscore(x, group) -> calculate group zscore<br><br>
