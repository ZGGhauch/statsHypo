# Parametric and Non-Parametric Hypothesis Testing Suite

## About

This package provides a comprehensive collection of methods for performing statistical hypothesis testing on sample data in Python. It provides a range of statistical tests commonly used for assessing hypotheses and drawing inferences from sample data. Whether you are a data scientist, researcher, or analyst, this package offers a powerful toolkit to analyze and interpret data.

A wide range of statistical tests, such as t-tests, chi-square tests, ANOVA, Mann-Whitney U test, Kruskal-Wallis test, are included. These methods enable you to compare sample means, proportions, variances, and distributions, and make informed decisions about hypotheses.

Both parametric tests (assuming specific population distributions) and nonparametric tests (requiring fewer distributional assumptions) are supported. You can choose the appropriate test based on the characteristics of your data and the underlying assumptions.

The package offers methods for various sample scenarios. Whether you have one sample, two independent samples, paired samples, or multiple independent samples, you can find the relevant hypothesis tests to compare and draw conclusions.

Each hypothesis test provides detailed results, including test statistics, p-values, confidence intervals, effect sizes, degrees of freedom, and other relevant statistical measures. This information enables you to interpret and report the significance of the findings accurately.

The package is designed to seamlessly integrate with popular data analysis libraries such as NumPy, SciPy, and Pandas. You can easily incorporate the hypothesis testing methods into your data analysis workflows, combining them with data manipulation, visualization, and modeling techniques.

The package comes with thorough documentation and examples that illustrate how to use each hypothesis testing method effectively. You can quickly understand the syntax, parameters, and interpretation of results, making it easier to apply the tests to your own datasets.

The package provides a robust and user-friendly environment for conducting statistical hypothesis tests. By leveraging the capabilities of this package, you can analyze your sample data in-depth, validate hypotheses, and derive meaningful insights to support evidence-based decision making.

## Author

Ziad Ghauch

## Installation

# Supported Statistical Hypothesis Tests

## Single-Sample Statistical Tests

| Hypothesis Test | Method | Data Type  | Statistic Distribution |  Variants |
|:---------:|:-------|:-------------|:-------------|:-------------|
| Single-Sample Z-test | InferenceSingleSample()<br>.z_test()  | Interval/ratio  | yes  | | 
| Single-Sample T-test  | InferenceSingleSample()<br>.t_test() |  |  | | 
| Single-Sample Chi-Square Test for a Population Variance | InferenceSingleSample()<br>.chi_square_test_population_variance() |  |  | | 
| Single-Sample Test for Evaluating Population Skewness | InferenceSingleSample()<br>.test_population_skewness() |  |  | | 
| Single-Sample Test for Evaluating Population Kurtosis | InferenceSingleSample()<br>.test_population_kurtosis() |  |  | Test 5a: The D’Agostino–Pearson Test of Normality [dagostino_pearson_test_normality()] | 
| Wilcoxon Signed-Ranks Test |  InferenceSingleSample()<br>.wilcoxon_signed_ranks_test() |  |  | | 
| Kolmogorov–Smirnov Goodness-of-fit Test for a Single Sample | InferenceSingleSample()<br>.kolmogorov_smirnov_goodness_of_fit_test() |  |  | The Lilliefors Test for Normality | 
| Chi-Square Goodness-of-Fit Test | InferenceSingleSample()<br>.chi_square_goodness_of_fit_test |  |  | | 
| Binomial Sign Test for a Single Sample | InferenceSingleSample()<br>.binomial_sign_test_single_sample() |  |  |  Z-test for a Population Proportion; Single-Sample Test for the Median | 
| Single-Sample Runs Test | InferenceSingleSample()<br>.single_sample_runs_test() |  |  | The Runs Test for Serial Randomness ; The Frequency Test (for Randomness) ; The Gap Test (for Randomness) ; The Poker Test (for Randomness) ; The Maximum Test (for Randomness)  ; The Mean Square Successive Difference Test (for serial randomness) ; | 
| Cramér-von Mises test for goodness of fit | InferenceSingleSample()<br>.cramer_vonmises_test() |  |  | | 
| Cressie-Read power divergence statistic and goodness of fit test | InferenceSingleSample()<br>.cressie_read_power_divergence_test() |  |  | | 
| Jarque-Bera goodness of fit test | InferenceSingleSample()<br>.jarque_bera_test() |  |  | | 
| Shapiro-Wilk test | InferenceSingleSample()<br>.shapiro_wilk_test() |  |  | | 
| Anderson-Darling Test | InferenceSingleSample()<br>.anderson_darling_test() |  |  | | 
| Anderson-Darling Test for k-samples | InferenceSingleSample()<br>.anderson_darling_test_k_samples |  |  | | 


## Two-Samples Statistical Tests

| Hypothesis Test | Method | Data Type  | Independent Samples |  Variants |
|:----------:|:-------------|:-------------|:-------------|:-------------|
| T-test for Two Dependent Samples | InferenceTwoDependentSamples()<br>.t_test_dependent() |  | No | T-test for Homogeneity of Variance ; Sandler’s A-test ; Test 17e: Z-test for Two Dependent Samples | 
| Wilcoxon Matched-Pairs Signed-Ranks Test | InferenceTwoDependentSamples().wilcoxon_matched_pairs_test() |  | No |  | 
| Binomial Sign Test for Two Dependent Samples | InferenceTwoDependentSamples()<br>.binomial_sign_test_dependent() |  | No |  | 
| McNemar Test | InferenceTwoDependentSamples()<br>.mcnemar_test() |  | No | Bowker Test of Symmetry | 
| T-Test for Two Independent Samples |  InferenceTwoIndependentSamples()<br>.t_test_independent() |  | Yes | Hartley’s F Test for Homogeneity of Variance ; Z-test for Two Independent Samples ; Procedures for Identifying Outliers  | 
| Mann–Whitney U Test | InferenceTwoIndependentSamples()<br>.mann_whitney_utest() |  | Yes | Randomization Test for Two Independent Samples ; Bootstrap (can be employed for variability) ; Jackknife (can be employed for variability) | 
| Kolmogorov–Smirnov Test for Two Independent Samples | InferenceTwoIndependentSamples()<br>.kolmogorov_smirnov_test()  |  | Yes |  | 
| Siegel–Tukey Test for Equal Variability | InferenceTwoIndependentSamples()<br>.siegel_tukey_test() |  | Yes |  | 
| Moses Test for Equal Variability | InferenceTwoIndependentSamples()<br>.moses_test_variability() |  | Yes |  | 
| Chi square Test | InferenceTwoIndependentSamples()<br>.chi_square_test() |  | Yes | Chi-Square Test for Homogeneity ; Fisher Exact Test ; Z-test for Two Independent Proportions ; Median Test for Independent Samples  | 
| Single-Factor Between-Subjects Analysis of Variance | InferenceTwoIndependentSamples()<br>.single_factor_between_subjects_anova()  |  | Yes | Single-Factor Between-Subjects Analysis of Covariance | 
| Van der Waerden Normal-Scores Test for k Independent Samples  | InferenceTwoIndependentSamples()<br>.van_der_waerden_normal_scores() |  | Yes |  | 
| Cramér-von Mises Test | InferenceTwoIndependentSamples()<br>.cramer_von_mises_goodness_of_fit_test() |  | Yes |  | 
| Epps-Singleton Test | InferenceTwoIndependentSamples()<br>.epps_singleton_test() |  | Yes |  | 
| Brunner-Munzel Test | InferenceTwoIndependentSamples()<br>.brunner_munzel_test() |  | Yes |  | 
| Ansari-Bradley Test | InferenceTwoIndependentSamples()<br>.ansari_bradley_test() |  | Yes |  | 
| Mood’s Test  | InferenceTwoIndependentSamples()<br>.moods_test() |  | Yes |  |  
    

## Two-or-more Samples Statistical Tests

| Hypothesis Test | Method | Data Type  | Independent Samples |  Statistical Test Variants  |
|:----------:|:-------------|:-------------|:-------------|:-------------|
| Single-Factor Between-Subjects Analysis of Variance | InferenceTwoOrMoreIndenpendentSamples()<br>.single_factor_anova() | | Yes | Multiple T-tests/Fisher’s LSD Test ; Bonferroni–Dunn test ;  Tukey’s HSD Test ; Newman–Keuls Test ; Scheffé Test ; Dunnett Test ; Single-Factor Between-Subjects Analysis of Covariance |
| Kruskal–Wallis One-Way Analysis of Variance by Ranks | InferenceTwoOrMoreIndenpendentSamples()<br>.kruskal_wallis_oneway_analysis_variance() | | Yes | |
| Van der Waerden Normal-Scores Test (k Independent Samples) | InferenceTwoOrMoreIndenpendentSamples()<br>.van_der_waerden_normal_test_k_independent_samples() | | Yes | |
| Levene Test  | InferenceTwoOrMoreIndenpendentSamples()<br>.levene_test() | | Yes | |
| Bartlett’s Test | InferenceTwoOrMoreIndenpendentSamples()<br>.bartletts_test() | | Yes | |
| Fligner-Killeen Test | InferenceTwoOrMoreIndenpendentSamples()<br>.fligner_killeen_test() | | Yes | |
| Mood’s Median Test | InferenceTwoOrMoreIndenpendentSamples()<br>.moods_median_test() | | Yes | |
| Single-Factor Within-Subjects Analysis of Variance | InferenceTwoOrMoreDependentSamples()<br>.single_factor_anova() | | No | Multiple t Tests/Fisher’s LSD Test ; Bonferroni–Dunn Test ; Tukey’s HSD Test ; Newman–Keuls Test ; Scheffé Test ; Dunnett Test |
| Friedman Two-Way Analysis of Variance by Ranks| InferenceTwoOrMoreDependentSamples()<br>.friedman_twoway_analysis_variance() | | No | |        
| Cochran Q Test  | InferenceTwoOrMoreDependentSamples()<br>.cochran_q_test | | No | |     


# Demo 

We provide a select few examples below on running different statistical hypothesis tests for one, two, and three samples, respectively. 

Single-sample Z-test
```
from numpy import random
from single_sample import InferenceSingleSample

X = random.normal(20.,1.,100)
alpha_val = 0.05

t = InferenceSingleSample(X, alpha_val, [20.,1.])
print (t.z_test.__doc__)
stat = t.z_test()
```

Two-sample T-test
```
from numpy import random
from two_independent_samples import InferenceTwoIndependentSamples

X = random.normal(20.,1.,100)
Y = random.normal(25.,1.,100)
alpha_val = 0.05

t = InferenceTwoIndependentSamples(X, Y, alpha_val)
print (t.t_test_independent.__doc__)
stat = t.t_test_independent()
```

Three-sample ANOVA 

```
from numpy import random  
from twoormore_indenpendent_samples import InferenceTwoOrMoreIndenpendentSamples

X = random.normal(20.,1.,100)
Y = random.normal(25.,1.,100)
Z = random.normal(30.,1.,100)
alpha_val = 0.05

t = InferenceTwoOrMoreIndenpendentSamples(X, Y, Z, alpha=0.05)
print (t.single_factor_anova.__doc__)
stat = t.single_factor_anova()
```

## Reference

+ Sheskin (2011), *Handbook of Parametric and Nonparametric Statistical Procedures*, 5th Ed.
