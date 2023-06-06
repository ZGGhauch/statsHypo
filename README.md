# Parametric and Non-Parametric Hypothesis Testing Suite

Author: Ziad Ghauch

## About

This package provides a comprehensive collection of methods for performing statistical hypothesis testing on sample data in Python. It provides a range of statistical tests commonly used for assessing hypotheses and drawing inferences from sample data. A powerful statistical testing toolkit is provided to analyze and interpret data.

A wide range of statistical tests, such as t-tests, chi-square tests, ANOVA, Mann-Whitney U test, Kruskal-Wallis test, are included. These methods enable you to compare sample means, variances, distributions, and make data-driven decisions about hypotheses. Both parametric tests (assuming specific population distributions) and nonparametric tests (requiring fewer distributional assumptions) are supported, depending on the properties of the underlying data.

Different sampling scenarios are supported to find the appropriate hypothesis tests to compare and draw conclusions adequately, including one-sample, two independent samples, two dependent samples (i.e. paired samples), and more-than-two dependent or independent samples. Each hypothesis test provides detailed results, including test statistics, p-values, confidence intervals, effect sizes, degrees-of-freedom, and other relevant statistical measures. This information enables an analyst to interpret and report the significance of the findings accurately.

The package is designed to seamlessly integrate with popular data analysis libraries such as NumPy, SciPy, and Pandas. You can easily incorporate the hypothesis testing methods into your data analysis workflows, combining them with data manipulation, visualization, and modeling techniques. Moreover a thorough documentation is provided, including a hands-on guide on how to use each hypothesis testing method correctly and effectively. The syntax, parameters, and results are ease to interpret and understand, making it easier to apply the tests to any given dataset. By leveraging the capabilities of this package, you can analyze your sample data in-depth, validate hypotheses, and derive meaningful insights to support evidence-based decision making.

## Installation

** Method 1 **

Using the *setup.py* file, navigate to the package directory, then type
```
python setup.py install
```

** Method 2 **

Using the pip command, you can install this package directly from the GitHub repository
```
pip install git+https://github.com/ZGGhauch/statsHypo
```

** Method 3 **

To download a compressed version of the package
```
wget git+https://github.com/ZGGhauch/statsHypo/archive/master.zip
unzip master.zip
cd optTEST
```

## Supported Statistical Hypothesis Tests

## Single-Sample Statistical Tests

| Hypothesis Test | Method | Data Type  | Statistic Distribution |  Variants |
|:---------:|:-------|:-------------|:-------------|:-------------|
| Single-Sample Z-test | InfOneSamp()<br>.z_test()  | Interval/ratio  | yes  | | 
| Single-Sample T-test  | InfOneSamp()<br>.t_test() |  |  | | 
| Single-Sample Chi-Square Test for a Population Variance | InfOneSamp()<br>.chi_square_test_population_variance() |  |  | | 
| Single-Sample Test for Evaluating Population Skewness | InfOneSamp()<br>.test_population_skewness() |  |  | | 
| Single-Sample Test for Evaluating Population Kurtosis | InfOneSamp()<br>.test_population_kurtosis() |  |  | • D’Agostino–Pearson Test of Normality | 
| Wilcoxon Signed-Ranks Test |  InfOneSamp()<br>.wilcoxon_signed_ranks_test() |  |  | | 
| Kolmogorov–Smirnov Goodness-of-fit Test for a Single Sample | InfOneSamp()<br>.kolmogorov_smirnov_goodness_of_fit_test() |  |  | •  Lilliefors Test for Normality | 
| Chi-Square Goodness-of-Fit Test | InfOneSamp()<br>.chi_square_goodness_of_fit_test |  |  | | 
| Binomial Sign Test for a Single Sample | InfOneSamp()<br>.binomial_sign_test_single_sample() |  |  | • Z-test for Population Proportion<br> • Test for the Median | 
| Single-Sample Runs Test | InfOneSamp()<br>.single_sample_runs_test() |  |  | • Runs Test for Serial Randomness<br> • Frequency Test <br> • Gap Test<br> • Poker Test<br> • Maximum Test<br> • Mean Square Successive Difference Test | 
| Cramér-von Mises test for goodness of fit | InfOneSamp()<br>.cramer_vonmises_test() |  |  | | 
| Cressie-Read power divergence statistic and goodness of fit test | InfOneSamp()<br>.cressie_read_power_divergence_test() |  |  | | 
| Jarque-Bera goodness of fit test | InfOneSamp()<br>.jarque_bera_test() |  |  | | 
| Shapiro-Wilk test | InfOneSamp()<br>.shapiro_wilk_test() |  |  | | 
| Anderson-Darling Test | InfOneSamp()<br>.anderson_darling_test() |  |  | | 
| Anderson-Darling Test for k-samples | InfOneSamp()<br>.anderson_darling_test_k_samples |  |  | | 


## Two-Samples Statistical Tests

| Hypothesis Test | Method | Data Type  | Independent Samples |  Variants |
|:----------:|:-------------|:-------------|:-------------|:-------------|
| T-test for Two Dependent Samples | InfTwoDepSamp()<br>.t_test_dependent() |  | No | • T-test for Homogeneity of Variance<br> • Sandler’s A-test<br> • Z-test for Two Dependent Samples | 
| Wilcoxon Matched-Pairs Signed-Ranks Test | InfTwoDepSamp().wilcoxon_matched_pairs_test() |  | No |  | 
| Binomial Sign Test for Two Dependent Samples | InfTwoDepSamp()<br>.binomial_sign_test_dependent() |  | No |  | 
| McNemar Test | InfTwoDepSamp()<br>.mcnemar_test() |  | No | • Bowker Test of Symmetry | 
| T-Test for Two Independent Samples |  InfTwoIndepSamp()<br>.t_test_independent() |  | Yes | • Hartley’s F-test for Homogeneity of Variance<br> • Z-test for Two Independent Samples<br> • Procedures for Identifying Outliers  | 
| Mann–Whitney U Test | InfTwoIndepSamp()<br>.mann_whitney_utest() |  | Yes | • Randomization Test for Two Independent Samples<br> • Bootstrap<br> • Jackknife | 
| Kolmogorov–Smirnov Test for Two Independent Samples | InfTwoIndepSamp()<br>.kolmogorov_smirnov_test()  |  | Yes |  | 
| Siegel–Tukey Test for Equal Variability | InfTwoIndepSamp()<br>.siegel_tukey_test() |  | Yes |  | 
| Moses Test for Equal Variability | InfTwoIndepSamp()<br>.moses_test_variability() |  | Yes |  | 
| Chi square Test | InfTwoIndepSamp()<br>.chi_square_test() |  | Yes | • Chi-Square Test for Homogeneity<br> • Fisher Exact Test<br> • Z-test for Two Independent Proportions<br> • Median Test for Independent Samples  | 
| Single-Factor Between-Subjects Analysis of Variance | InfTwoIndepSamp()<br>.single_factor_between_subjects_anova()  |  | Yes | • Single-Factor Between-Subjects Analysis of Covariance | 
| Van der Waerden Normal-Scores Test for k Independent Samples  | InfTwoIndepSamp()<br>.van_der_waerden_normal_scores() |  | Yes |  | 
| Cramér-von Mises Test | InfTwoIndepSamp()<br>.cramer_von_mises_goodness_of_fit_test() |  | Yes |  | 
| Epps-Singleton Test | InfTwoIndepSamp()<br>.epps_singleton_test() |  | Yes |  | 
| Brunner-Munzel Test | InfTwoIndepSamp()<br>.brunner_munzel_test() |  | Yes |  | 
| Ansari-Bradley Test | InfTwoIndepSamp()<br>.ansari_bradley_test() |  | Yes |  | 
| Mood’s Test  | InfTwoIndepSamp()<br>.moods_test() |  | Yes |  |  
    

## Two-or-more Samples Statistical Tests

| Hypothesis Test | Method | Data Type  | Independent Samples |  Statistical Test Variants  |
|:----------:|:-------------|:-------------|:-------------|:-------------|
| Single-Factor Between-Subjects Analysis of Variance | InfTwoOrMoreIndepSamp()<br>.single_factor_anova() | | Yes | • Multiple T-tests/Fisher’s LSD Test<br> • Bonferroni–Dunn Test<br> • Tukey’s HSD Test<br> • Newman–Keuls Test<br> • Scheffé Test<br> • Dunnett Test<br> • Single-Factor Between-Subjects Analysis of Covariance |
| Kruskal–Wallis One-Way Analysis of Variance by Ranks | InfTwoOrMoreIndepSamp()<br>.kruskal_wallis_oneway_analysis_variance() | | Yes | |
| Van der Waerden Normal-Scores Test (k Independent Samples) | InfTwoOrMoreIndepSamp()<br>.van_der_waerden_normal_test_k_independent_samples() | | Yes | |
| Levene Test  | InfTwoOrMoreIndepSamp()<br>.levene_test() | | Yes | |
| Bartlett’s Test | InfTwoOrMoreIndepSamp()<br>.bartletts_test() | | Yes | |
| Fligner-Killeen Test | InfTwoOrMoreIndepSamp()<br>.fligner_killeen_test() | | Yes | |
| Mood’s Median Test | InfTwoOrMoreIndepSamp()<br>.moods_median_test() | | Yes | |
| Single-Factor Within-Subjects Analysis of Variance | InfTwoOrMoreDepSamp()<br>.single_factor_anova() | | No | • Multiple T-tests/Fisher’s LSD Test<br> • Bonferroni–Dunn Test<br> • Tukey’s HSD Test<br> • Newman–Keuls Test<br> • Scheffé Test<br> • Dunnett Test<br> |
| Friedman Two-Way Analysis of Variance by Ranks| InfTwoOrMoreDepSamp()<br>.friedman_twoway_analysis_variance() | | No | |        
| Cochran Q Test  | InfTwoOrMoreDepSamp()<br>.cochran_q_test | | No | |     


## Demo 

We provide a select few examples below on running different statistical hypothesis tests for one, two, and three samples, respectively. 

Single-sample Z-test
```
from numpy import random
from single_sample import InfOneSamp

X = random.normal(20.,1.,100)
alpha_val = 0.05

t = InfOneSamp(X, alpha_val, [20.,1.])
print (t.z_test.__doc__)
stat = t.z_test()
```

Two-sample T-test
```
from numpy import random
from two_independent_samples import InfTwoIndepSamp

X = random.normal(20.,1.,100)
Y = random.normal(25.,1.,100)
alpha_val = 0.05

t = InfTwoIndepSamp(X, Y, alpha_val)
print (t.t_test_independent.__doc__)
stat = t.t_test_independent()
```

Three-sample ANOVA 

```
from numpy import random  
from twoormore_indenpendent_samples import InfTwoOrMoreIndepSamp

X = random.normal(20.,1.,100)
Y = random.normal(25.,1.,100)
Z = random.normal(30.,1.,100)
alpha_val = 0.05

t = InfTwoOrMoreIndepSamp(X, Y, Z, alpha=0.05)
print (t.single_factor_anova.__doc__)
stat = t.single_factor_anova()
```

## Reference

+ Sheskin (2011), *Handbook of Parametric and Nonparametric Statistical Procedures*, 5th Ed.
