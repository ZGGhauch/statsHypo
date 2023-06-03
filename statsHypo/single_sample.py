# -------------------------------------------------------------
# Statistical Hypothesis Tests
# Single Sample Inference
#
# Author: Ziad Ghauch
# -------------------------------------------------------------


from scipy.stats import normaltest
from scipy.stats import chisquare
from scipy.stats import cramervonmises
from scipy.stats import power_divergence
from scipy.stats import ks_1samp
from scipy.stats import jarque_bera
from scipy.stats import shapiro
from scipy.stats import anderson
from scipy.stats import anderson_ksamp
from sample import Samples
from numpy import sqrt, mean, log, abs




class InferenceSingleSample(Samples):
    ''' Inferential statistical tests employed with a single sample
        
    Test 1: Single-Sample Z-test
    Test 2: Single-Sample T-test 
    Test 3: Single-Sample Chi-Square Test for a Population Variance
    Test 4: Single-Sample Test for Evaluating Population Skewness
    Test 5: Single-Sample Test for Evaluating Population Kurtosis
        Test 5a: D’Agostino–Pearson Test of Normality
    Test 6: Wilcoxon Signed-Ranks Test
    Test 7: Kolmogorov–Smirnov Goodness-of-fit Test
        Test 7a: Lilliefors Test for Normality
    Test 8: Chi-Square Goodness-of-Fit Test
    Test 9: Binomial Sign Test for a Single Sample
        Test 9a: Z-test for a Population Proportion
        Test 9b: Single-Sample Test for the Median 
    Test 10: Single-Sample Runs Test
    Test 10a: Runs Test for Serial Randomness
        Test 10b: Frequency Test (for Randomness)
        Test 10c: Gap Test (for Randomness)
        Test 10d: Poker Test (for Randomness)
        Test 10e: Maximum Test (for Randomness)
        Test 10f: Mean Square Successive Difference Test
    Test 35: Cramér-von Mises test for goodness of fit
    Test 37: Cressie-Read power divergence statistic 
    Test 40: Jarque-Bera goodness of fit test
    Test 43: Shapiro-Wilk test
    Test 46: Anderson-Darling test
    Test 47: Anderson-Darling test for k-samples
    '''
    
    def __init__(self, P, alpha, inf_parameters=[], test_title=''):
        super().__init__(P, test_title)
        self.alpha=alpha
        self.inf_parameters=inf_parameters
   
    def set_p(self, P):
        self.P=P

    def get_p(self):
        return self.P
    
    def set_alpha(self, alpha):
        self.alpha=alpha

    def get_alpha(self):
        return self.alpha


    def z_test(self):
        ''' Test 1: Single-Sample Z-test 
        
        Parametric test to assess the likelihood that a sample is derived from a population 
        with known parameters (i.e. mean, sigma); Population assumed Gaussian. Perform Z-test
        only when population paramerers (mean and sigma) are known. The test statistic is 
        based on the Gaussian distribution.
        
        H0 (null hypothesis): 
        	-> mean of the sample equals the population mean 
        H1 (alternate hypothesis): 
        	-> mean of the sample does not equal (i.e. nondirectional, two-tailed
            	test) the population mean, or 
        	-> mean of the sample is less than the population mean (directional, 
            	one-tailed left test), or 
        	-> mean of the sample is greater than the population mean (directional,
            	one-tailed right test)
        
        Parameters
        ----------
        P : sample of size (N,1) from the population (mu, sigma)
        
        Return
        ------
        zstat : single-sample Z-test statistic
        '''
        
        self.test_title='Single-Sample Z-test'
        print ('~'+str(self.test_title)+'~')
        
        Samples.get_sample_desciptive_statistics(self.P)
        pop_mean, pop_std = self.inf_parameters[0], self.inf_parameters[1]
        
        zstat = (mean(self.P) - pop_mean) / (pop_std/sqrt(len(self.P))) 
        print ('stat=%.3f' % (zstat))
        

    def t_test(self):
        ''' Test 2: The Single-Sample T-test  

        Parametric test to assess the likelihood that a sample is derived from a population 
        with known parameters mean but unknown sigma; Population assumed Gaussian. Perform T-test
        only when population std dev paramerer (i.e. sigma) is unknown or when sample size N is
        small. The test statistic is based on the t-distribution. 
        
        H0 (null hypothesis): 
        	-> mean of the sample equals the population mean 
        H1 (alternate hypothesis): 
        	-> mean of the sample does not equal (i.e. nondirectional, two-tailed
            	test) the population mean, or 
        	-> mean of the sample is less than the population mean (directional, 
            	one-tailed left test), or 
        	-> mean of the sample is greater than the population mean (directional,
            	one-tailed right test)
        
        Parameters
        ----------
        P : sample of size (N,1) from the population (mean mu)
        
        Return
        ------
        tstat : single-sample T-test statistic        
        '''
        
        self.test_title='Single-Sample T-test'
        print ('~'+str(self.test_title)+'~')
        
        Samples.get_sample_desciptive_statistics(self.P)
        
        pop_mean = self.inf_parameters[0]
        #from scipy.stats import ttest_1samp
        #stat, p = ttest_1samp(self.P, popmean=pop_mean)
        #print ('stat=%.3f, p=%.3f' % (stat,p))
        
        n = len(self.P)
        sx = sqrt((sum(self.P**2) - (sum(self.P))**2 / n) / (n-1)) / sqrt(n)
        tstat = (mean(self.P) - pop_mean) / sx
        print ('stat=%.3f' % (tstat))

        #if p > self.alpha:
        #    print ('Mean of population the sample represents equals mu_target')
        #else:
        #    print ('Mean of population sample represents is not equal to mu_target.')


    def chi_square_test_population_variance(self):
        ''' Test 3: Single-Sample Chi-Square Test for a Population Variance 

        Statistical inference single-sample test to assess the likelihood that 
        a sample with variance s^2 is derived from a population 
        with variance sigma^2. The test statistic is based on the chi-square 
        distribution, with the assumptions that the population from which the 
        sample is drawn is normal. 
        
        H0 (null hypothesis): 
        	-> variance of the sample equals the population variance 
        H1 (alternate hypothesis): 
        	-> variance of the sample does not equal (i.e. nondirectional, two-tailed
            	test) the population variance, or 
        	-> variance of the sample is less than the population variance (directional, 
            	one-tailed left test), or 
        	-> variance of the sample is greater than the population variance (directional,
            	one-tailed right test)
        
        Parameters
        ----------
        P : sample of size (N,1) from the population (variance sigma^2)
        
        Return
        ------
        chisquarestat : single-sample chi-square test statistic          
        '''
        
        self.test_title='Single-Sample Chi-Square Test'
        print ('~'+str(self.test_title)+'~')
 
        pop_var = (self.inf_parameters[0])**2    
        
        Samples.get_sample_desciptive_statistics(self.P) 
        
        n = len(self.P)   
        s2 = (sum(self.P**2) - (sum(self.P)**2) / n) / (n-1)
        chisquarestat = (n-1)*s2/pop_var
        
        print ('stat=%.3f' % (chisquarestat))


    def test_population_skewness(self):
        ''' Test 4: Single-Sample Test for Evaluating Population Skewness 
        
        Statistical test for assessing whether a sample comes from a symmetrical
        distribution (i.e. no skew).
        
        H0 (null hypothesis): 
        	-> sample is drawn from a population with no skew (i.e. symmetrical distribution) 
        H1 (alternate hypothesis): 
        	-> sample is drawn from a population with positive or negative skew 
            	(i.e. nondirectional, two-tailed test), or 
        	-> sample is drawn from a population with positive skew (directional, 
            	one-tailed left test), or 
        	-> variance of the sample is greater than the population variance (directional,
            	one-tailed right test)
        
        Parameters
        ----------
        P : sample of size (N,1) from the population
        
        Return
        ------
        skewstat : single-sample skew test statistic         
        '''

        self.test_title='Single-Sample Test for Evaluating Population Skewness'
        print ('~'+str(self.test_title)+'~')
        
        Samples.get_sample_desciptive_statistics(self.P)
        
        n = len(self.P)
        m3 = (n*sum((self.P - mean(self.P))**3)) / ((n-1)*(n-2))
        st = sqrt((sum((self.P - mean(self.P))**2)) / (n-1))
        g1 = m3 / st**3
        sb1 = (n-2)*g1/(sqrt(n*(n-1)))
        A = sb1 * sqrt((n+1)*(n+3)/(6*(n-2)))
        B = 3 * (n**2 + 27*n -70) * (n+1) * (n+3) / ((n-2) * (n+5) * (n+7) * (n+9))
        C = sqrt(2*(B-1))-1
        D = sqrt(C)
        E = 1./sqrt(log(D))
        F = A / (sqrt(2./(C-1)))
        stewstat = E * log(F + sqrt(F**2+1))
        print ('stat=%.3f' % (stewstat))
        
		#from scipy.stats import skewtest
        #stat, p = skewtest(self.P)
        #print ('stat=%.3f, p=%.3f' % (stat,p))
        #if p > self.alpha:
        #    print ('Skewness of the population that the sample was drawn from is the same as that of a corresponding normal distribution')
        #else:
        #    print ('Skewness of the population that the sample was drawn from is not the same as that of a corresponding normal distribution')
        

    def test_population_kurtosis(self):
        ''' Test 5: Single-Sample Test for Evaluating Population Kurtosis
         
        Statistical test for assessing whether a sample comes from a population
        distribution with no kurtosis (i.e. mesokurtic).
        
        H0 (null hypothesis): 
        	-> sample is drawn from a population with no kurtosis (i.e. mesokurtic distribution) 
        H1 (alternate hypothesis): 
        	-> sample is drawn from a population distribution that is not mesokurtic 
            	(i.e. nondirectional, two-tailed test), or 
        	-> sample is drawn from a population with platykurtic distribution (directional, 
            	one-tailed left test), or 
        	-> sample is drawn from a population with leptokurtic distribution  (directional,
            	one-tailed right test)
        
        Parameters
        ----------
        P : sample of size (N,1) from the population
        
        Return
        ------
        kurtosisstat : single-sample kurtosis test statistic           
        '''

        self.test_title='Single-Sample Test for Evaluating Population Kurtosis'
        print ('~'+str(self.test_title)+'~')
        
        Samples.get_sample_desciptive_statistics(self.P)
        
        n = len(self.P)
        m4 = ((sum((self.P-mean(self.P))**4)*n*(n+1)/(n-1))-3*(sum((self.P-mean(self.P))**2))**2)/((n-2)*(n-3))
        st = sqrt((sum((self.P - mean(self.P))**2)) / (n-1))
        g2 = m4 / st**4
        G = 24*n*(n-2)*(n-3)/((n+1)**2*(n+3)*(n+5))
        H = (n-2)*(n-3)*abs(g2)/((n+1)*(n-1)*sqrt(G))
        J = (6*(n**2-5*n+2)/((n+7)*(n+9))) * sqrt((6*(n+3)*(n+5))/(n*(n-2)*(n-3)))
        K = 6 + 8./J *(2./J + sqrt(1+4./(J**2)))
        L = (1-2./K)/(1+H*sqrt(2./(K-4)))
        kurtosisstat = (1-2./(9*K)-L**(1./3)) / (sqrt(2./(9*K)))
        print ('stat=%.3f' % (kurtosisstat))
        

        from scipy.stats import kurtosistest
        stat, p = kurtosistest(self.P) 
        print ('stat=%.3f, p=%.3f' % (stat,p))

        #if p > self.alpha:
        #    print ('Kurtosis of the population that the sample was drawn from is the same as that of a corresponding normal distribution')
        #else:
        #    print ('Kurtosis of the population that the sample was drawn from is not the same as that of a corresponding normal distribution')
        
        
    def dagostino_pearson_test_normality(self):
        ''' Test 5a: D’Agostino–Pearson Test of Normality

        Test for assessing goodness-of-fit for a normal distribution
        
        Null hypothesis H0: The sample is derived from a normally distributed population.
        Alternative hypothesis H1: The sample is not derived from a normally distributed population.
        '''

        self.test_title='D’Agostino–Pearson Test of Normality'
        print ('~'+str(self.test_title)+'~')
        
        Samples.get_sample_desciptive_statistics(self.P)
        
        stat, p = normaltest(self.P)
        
        print('stat=%.3f, p=%.3f' % (stat, p))
        if p > self.alpha:
            print('The sample is probably derived from a normally distributed population.')
        else:
            print('The sample is probably not derived from a normally distributed population.')
        return (stat, p)


    def  wilcoxon_signed_ranks_test(self):
        '''  Test 6: Wilcoxon Signed-Ranks Test '''
        self.test_title='Wilcoxon Signed-Ranks Test'
        print ('~'+str(self.test_title)+'~')


    def kolmogorov_smirnov_goodness_of_fit_test(self):
        ''' Test 7: Kolmogorov–Smirnov Goodness-of-fit Test '''

        self.test_title='Kolmogorov–Smirnov Goodness-of-fit Test'
        print ('~'+str(self.test_title)+'~')
        
        Samples.get_sample_desciptive_statistics(self.P)
        _cdf = self.inf_parameters[0]
        
        stat, p = ks_1samp(self.P, cdf=_cdf)

        print('stat=%.3f, p=%.3f' % (stat, p))
        if p > self.alpha:
            print('The sample fits with the expected distribution.')
        else:
            print('The sample does not fit with the expected distribution.')
        return (stat, p)


    def chi_square_goodness_of_fit_test(self):
        ''' Test 8: Chi-Square Goodness-of-Fit Test '''

        self.test_title='Chi-Square Goodness-of-Fit Test'
        print ('~'+str(self.test_title)+'~')
        
        Samples.get_sample_desciptive_statistics(self.P)
        fexp = self.inf_parameters[0]
        
        stat, p = chisquare(self.P, f_exp=fexp)
        
        print('stat=%.3f, p=%.3f' % (stat, p))
        if p > self.alpha:
            print('The sample fits with the expected distribution.')
        else:
            print('The sample does not fit with the expected distribution.')
        return (stat, p)


    def binomial_sign_test_single_sample(self):
        ''' Test 9: Binomial Sign Test for a Single Sample '''
        self.test_title='Binomial Sign Test'
        print ('~'+str(self.test_title)+'~') 


    def single_sample_runs_test(self):
        ''' Test 10: Single-Sample Runs Test '''
        self.test_title='Single-Sample Runs Test'
        print ('~'+str(self.test_title)+'~')
        

    def cramer_vonmises_test(self):
        ''' Test 35: Cramér-von Mises Test '''

        self.test_title='Cramér-von Mises Test'
        print ('~'+str(self.test_title)+'~')
        
        Samples.get_sample_desciptive_statistics(self.P)
        _cdf = self.inf_parameters[0]
        
        stat, p = cramervonmises(self.P, cdf=_cdf)
        
        print('stat=%.3f, p=%.3f' % (stat, p))
        if p > self.alpha:
            print('The sample fits with the expected cumulative distribution.')
        else:
            print('The sample does not fit with the expected cumulative distribution.')
        return (stat, p)


    def cressie_read_power_divergence_test(self):
        ''' Test 37: Cressie-Read Power Divergence Statistic '''

        self.test_title='Cressie-Read Power Divergence Statistic'
        print ('~'+str(self.test_title)+'~')
        
        Samples.get_sample_desciptive_statistics(self.P)
        fexp = self.inf_parameters[0]
        
        stat, p = power_divergence(self.P, f_exp=fexp)

        print('stat=%.3f, p=%.3f' % (stat, p))
        if p > self.alpha:
            print('The sample fits with the expected distribution.')
        else:
            print('The sample does not fit with the expected distribution.')
        return (stat, p)
 

    def jarque_bera_test(self):
        ''' Test 40: Jarque-Bera Goodness of Fit Test '''

        self.test_title='Jarque-Bera Goodness of Fit Test'
        print ('~'+str(self.test_title)+'~')
        
        Samples.get_sample_desciptive_statistics(self.P)
        
        stat, p = jarque_bera(self.P)

        print('stat=%.3f, p=%.3f' % (stat, p))
        if p > self.alpha:
            print('sample data has the skewness and kurtosis matching a normal distribution.')
        else:
            print('sample data does not have the skewness and kurtosis matching a normal distribution.')
        return (stat, p)


    def shapiro_wilk_test(self):
        ''' Test 43: Shapiro-Wilk Test '''

        self.test_title='Shapiro-Wilk Test'
        print ('~'+str(self.test_title)+'~')
        
        Samples.get_sample_desciptive_statistics(self.P)
        
        stat, p = shapiro(self.P)
        print('stat=%.3f, p=%.3f' % (stat, p))
        if p > self.alpha:
            print('The sample was probably drawn from a normal distribution.')
        else:
            print('The sample was probably not drawn from a normal distribution.')
        return (stat, p)
 

    def anderson_darling_test(self):
        ''' Test 46: Anderson-Darling Test '''

        self.test_title='Anderson-Darling Test'
        print ('~'+str(self.test_title)+'~')
        
        Samples.get_sample_desciptive_statistics(self.P)
        _dist = self.inf_parameters[0]
        
        stat, p = anderson(self.P, dist=_dist)
        
        print('stat=%.3f, p=%.3f' % (stat, p))
        if p > self.alpha:
            print('The sample is drawn from a population that follows target distribution')
        else:
            print('Sample is not drawn from a population that follows target distribution')
        return (stat, p)


    def anderson_darling_test_k_samples(self):
        ''' Test 47: Anderson-Darling Test for k-samples '''

        self.test_title='Anderson-Darling Test for k-samples'
        print ('~'+str(self.test_title)+'~')
        
        Samples.get_sample_desciptive_statistics(self.P)
        
        stat, p = anderson_ksamp(self.P)
        
        print('stat=%.3f, p=%.3f' % (stat, p))
        if p > self.alpha:
            print('The sample is probably drawn from same distribution')
        else:
            print('Sample is probably not drawn from the same distribution')
        return (stat, p)
        















