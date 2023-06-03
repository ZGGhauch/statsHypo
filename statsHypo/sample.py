# -------------------------------------------------------------
# Statistical Hypothesis Tests
# Sampling class
#
# Author: Ziad Ghauch
# -------------------------------------------------------------

from scipy.stats import describe 
from scipy.stats import gaussian_kde
from numpy import sqrt, quantile, random, quantile, array


class Samples:
    ''' Samples class
    
    Samples from one or two populations '''
    
    bootstrap_size = 10000 # boostrap resampling (class variable)
    
    def __init__(self, P, test_title):
        self.P=P  # sample P from population 
        self.test_title = test_title
    
    def set_p(self, P):
        self.P=P 
    
    def set_test_title(self, test_title):
        self.test_title=test_title 
    
    def get_p(self):
        return self.P
    
    def get_test_title(self):
        return self.test_title


    @staticmethod
    def get_sample_desciptive_statistics(_sample):
        ''' Generate samples descriptive statistics '''
        print ('\t'+'|'+'-'*30+'|', end='\n')
        print ('\t'+'  DESCRIPTIVE STATISTICS', end='\n')
        print ('\t'+'|'+'-'*30+'|', end='\n')
        print ('\t'+'  Size ..........: '+str(_sample.shape[0]), end='\n')
        print ('\t'+'  Min ...........: '+str(round(describe(_sample)[1][0], 3)), end='\n')
        print ('\t'+'  25%  ..........: '+str(round(quantile(_sample,.25), 3)), end='\n')
        print ('\t'+'  50%  ..........: '+str(round(quantile(_sample,.50), 3)), end='\n')
        print ('\t'+'  75%  ..........: '+str(round(quantile(_sample,.75), 3)), end='\n')
        print ('\t'+'  Max ...........: '+str(round(describe(_sample)[1][1], 3)), end='\n')
        print ('\t'+'  Mean ..........: '+str(round(describe(_sample)[2], 3)), end='\n')
        print ('\t'+'  Std Dev .......: '+str(round(sqrt(describe(_sample)[3]), 3)), end='\n')
        print ('\t'+'  Skewness ......: '+str(round(describe(_sample)[4], 3)), end='\n')
        print ('\t'+'  Kurtosis ......: '+str(round(describe(_sample)[5], 3)), end='\n')
        print ('\t'+'|'+'-'*30+'|', end='\n')


    @staticmethod 
    def get_sample_density(_sample):
        ''' Density measure of samples using Gaussian Kernel Density Estimate 
        '''
        density = gaussian_kde(_sample)
        density.covariance_factor = lambda:cov_factor
        density._compute_covariance()
        return density


    @staticmethod
    def bootstrap_samples(_sample, sample_ratio=0.8):
        ''' Compute bootstrap samples of a statistic 
         
        Sample (with replacement) a subset of size (sample_ratio * N) the original data of size N.
        
        Parameters
        ----------
        _sample : original data of size (N,)
        sample_ratio : fraction of the original data to include in the resampling scheme
        
        Returns
        -------
        bootstrap sample of size (sample_ratio * N,)
        '''
        
        N = _sample.shape[0]
        return random.choice(_sample, size=int(sample_ratio*N), replace=True)
    
    @staticmethod
    def compute_p_value(_statistic, significance_level, type):
        ''' Compute p-value from statistic distribution (given significance level) '''
        _statistic = array(_statistic)
        if type == 'one-tail':
            cutoff = quantile(_statistic, 1.0-significance_level)
            pval = float(len(_statistic[_statistic>=cutoff])) / float(len(_statistic))
            return (cutoff, pval)
        elif type == 'two-tail':
            cutoff = quantile(_statistic, 1.0-significance_level/2.)
            pval = len(_statistic[_statistic>=cutoff])/len(_statistic)
            return (cutoff, pval)            
        
        

