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

| Hypothesis Test    | Method | Data Type  | Statistic Distribution |  Variants |
|----------|:-------------:|:-------------:|:-------------:|:-------------:|
|Test 1: Single-Sample Z-test | InferenceSingleSample().z_test()  | Interval/ratio  | yes  | | 
|Test 2: Single-Sample T-test  | InferenceSingleSample().t_test() |  |  | | 
|Test 3: Single-Sample Chi-Square Test for a Population Variance | InferenceSingleSample().chi_square_test_population_variance() |  |  | | 
|Test 4: Single-Sample Test for Evaluating Population Skewness | InferenceSingleSample().test_population_skewness() |  |  | | 
|Test 5: Single-Sample Test for Evaluating Population Kurtosis | InferenceSingleSample().test_population_kurtosis() |  |  | Test 5a: The D’Agostino–Pearson Test of Normality [dagostino_pearson_test_normality()] | 
|Test 6: Wilcoxon Signed-Ranks Test |  InferenceSingleSample().wilcoxon_signed_ranks_test() |  |  | | 
|Test 7: Kolmogorov–Smirnov Goodness-of-fit Test for a Single Sample | InferenceSingleSample().kolmogorov_smirnov_goodness_of_fit_test() |  |  | Test 7a: The Lilliefors Test for Normality | 
|Test 8: Chi-Square Goodness-of-Fit Test | InferenceSingleSample().chi_square_goodness_of_fit_test |  |  | | 
|Test 9: Binomial Sign Test for a Single Sample | InferenceSingleSample().binomial_sign_test_single_sample() |  |  |  Test 9a: Z-test for a Population Proportion ; Test 9b: Single-Sample Test for the Median | 
|Test 10: Single-Sample Runs Test | InferenceSingleSample().single_sample_runs_test() |  |  | Test 10a: The Runs Test for Serial Randomness ; Test 10b: The Frequency Test (for Randomness) ; Test 10c: The Gap Test (for Randomness) ; Test 10d: The Poker Test (for Randomness) ; Test 10e: The Maximum Test (for Randomness)  ; Test 10f: The Mean Square Successive Difference Test (for serial randomness) ; | 
|Test 35: Cramér-von Mises test for goodness of fit | InferenceSingleSample().cramer_vonmises_test() |  |  | | 
|Test 37: Cressie-Read power divergence statistic and goodness of fit test | InferenceSingleSample().cressie_read_power_divergence_test() |  |  | | 
|Test 40: Jarque-Bera goodness of fit test | InferenceSingleSample().jarque_bera_test() |  |  | | 
|Test 43: Shapiro-Wilk test | InferenceSingleSample().shapiro_wilk_test() |  |  | | 
|Test 46: Anderson-Darling Test | InferenceSingleSample().anderson_darling_test() |  |  | | 
|Test 47: Anderson-Darling Test for k-samples | InferenceSingleSample().anderson_darling_test_k_samples |  |  | | 


## Two-Samples Statistical Tests

| Hypothesis Test    |      Method      | Data Type  | Independent Samples |  Variants |
|----------|:-------------:|:-------------:|:-------------:|:-------------:|
| Test 17: T-test for Two Dependent Samples | InferenceTwoDependentSamples().t_test_dependent() |  | No | Test 17a: T-test for Homogeneity of Variance ; Test 17d: Sandler’s A-test ; Test 17e: Z-test for Two Dependent Samples | 
| Test 18: Wilcoxon Matched-Pairs Signed-Ranks Test | InferenceTwoDependentSamples().wilcoxon_matched_pairs_test() |  | No |  | 
| Test 19: Binomial Sign Test for Two Dependent Samples | InferenceTwoDependentSamples().binomial_sign_test_dependent() |  | No |  | 
| Test 20: McNemar Test | InferenceTwoDependentSamples().mcnemar_test() |  | No |  Test 20a: Bowker Test of Symmetry | 
| Test 11: T-Test for Two Independent Samples |  InferenceTwoIndependentSamples().t_test_independent() |  | Yes | Test 11a: Hartley’s F Test for Homogeneity of Variance ; Test 11d: Z-test for Two Independent Samples ; Test 11e: Procedures for Identifying Outliers  | 
| Test 12: Mann–Whitney U Test | InferenceTwoIndependentSamples().mann_whitney_utest() |  | Yes | Test 12a: Randomization Test for Two Independent Samples ; Test 12b: Bootstrap (can be employed for variability) ; Test 12c: Jackknife (can be employed for variability) | 
| Test 13: Kolmogorov–Smirnov Test for Two Independent Samples | InferenceTwoIndependentSamples().kolmogorov_smirnov_test()  |  | Yes |  | 
| Test 14: Siegel–Tukey Test for Equal Variability | InferenceTwoIndependentSamples().siegel_tukey_test() |  | Yes |  | 
| Test 15: Moses Test for Equal Variability | InferenceTwoIndependentSamples().moses_test_variability() |  | Yes |  | 
| Test 16: Chi square Test | InferenceTwoIndependentSamples().chi_square_test() |  | Yes | Test 16a: Chi-Square Test for Homogeneity ; Test 16c: Fisher Exact Test ; Test 16d: Z-test for Two Independent Proportions ; Test 16e: Median Test for Independent Samples  | 
| Test 21: Single-Factor Between-Subjects Analysis of Variance | InferenceTwoIndependentSamples().single_factor_between_subjects_anova()  |  | Yes | Test 21j: Single-Factor Between-Subjects Analysis of Covariance | 
| Test 23: Van der Waerden Normal-Scores Test for k Independent Samples  | InferenceTwoIndependentSamples().van_der_waerden_normal_scores() |  | Yes |  | 
| Test 36: Cramér-von Mises Test | InferenceTwoIndependentSamples().cramer_von_mises_goodness_of_fit_test() |  | Yes |  | 
| Test 37: Epps-Singleton Test | InferenceTwoIndependentSamples().epps_singleton_test() |  | Yes |  | 
| Test 38: Brunner-Munzel Test | InferenceTwoIndependentSamples().brunner_munzel_test() |  | Yes |  | 
| Test 41: Ansari-Bradley Test | InferenceTwoIndependentSamples().ansari_bradley_test() |  | Yes |  | 
| Test 42: Mood’s Test  | InferenceTwoIndependentSamples().moods_test() |  | Yes |  |  
    

## Two-or-more Samples Statistical Tests

| Hypothesis Test    |      Method      | Data Type  | Independent Samples |  Variants |
|----------|:-------------:|:-------------:|:-------------:|:-------------:|
| Test 21: Single-Factor Between-Subjects Analysis of Variance | InferenceTwoOrMoreIndenpendentSamples().single_factor_anova() | | Yes | Test 21a: Multiple T-tests/Fisher’s LSD Test ; Test 21b: Bonferroni–Dunn test ;  Test 21c: Tukey’s HSD Test ; Test 21d: Newman–Keuls Test ; Test 21e: Scheffé Test ; Test 21f: Dunnett Test ; Test 21j: Single-Factor Between-Subjects Analysis of Covariance |
| Test 22: Kruskal–Wallis One-Way Analysis of Variance by Ranks | InferenceTwoOrMoreIndenpendentSamples().kruskal_wallis_oneway_analysis_variance() | | Yes | |
| Test 23: Van der Waerden Normal-Scores Test (k Independent Samples) | InferenceTwoOrMoreIndenpendentSamples().van_der_waerden_normal_test_k_independent_samples() | | Yes | |
| Test 44: Levene Test  | InferenceTwoOrMoreIndenpendentSamples().levene_test() | | Yes | |
| Test 45: Bartlett’s Test | InferenceTwoOrMoreIndenpendentSamples().bartletts_test() | | Yes | |
| Test 48: Fligner-Killeen Test | InferenceTwoOrMoreIndenpendentSamples().fligner_killeen_test() | | Yes | |
| Test 49: Mood’s Median Test | InferenceTwoOrMoreIndenpendentSamples().moods_median_test() | | Yes | |
| Test 24: Single-Factor Within-Subjects Analysis of Variance | InferenceTwoOrMoreDependentSamples().single_factor_anova() | | No | Test 24a: Multiple t Tests/Fisher’s LSD Test ; Test 24b: Bonferroni–Dunn Test ; Test 24c: Tukey’s HSD Test ; Test 24d: Newman–Keuls Test ; Test 24e: Scheffé Test ; Test 24f: Dunnett Test |
| Test 25: Friedman Two-Way Analysis of Variance by Ranks| InferenceTwoOrMoreDependentSamples().friedman_twoway_analysis_variance() | | No | |        
| Test 26: Cochran Q Test  | InferenceTwoOrMoreDependentSamples().cochran_q_test | | No | |     
       
        
## Reference

+ Sheskin (2011), *Handbook of Parametric and Nonparametric Statistical Procedures*, 5th Ed.
