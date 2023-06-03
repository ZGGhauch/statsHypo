# -------------------------------------------------------------
# Statistical Hypothesis Tests
# Correlation inference
#
# Author: Ziad Ghauch
# -------------------------------------------------------------


from scipy.stats import pearsonr

from scipy.stats import kendalltau
from sample import Samples
import numpy as np



class Correlation(Samples):
    ''' Measures of correlation/association 
    
    Test 28: Pearson Product–Moment Correlation Coefficient
    Test 28k: Multiple Correlation Coefficient
    Test 28l: Partial Correlation Coefficient
    Test 28m: Semipartial Correlation Coefficient
    Test 29: Spearman’s Rank-Order Correlation Coefficient
    Test 30: Kendall’s Tau
    Test 32: Goodman and Kruskal’s Gamma
    Test 31: Kendall’s Coefficient of Concordance
    Test 16f: Contingency Coefficient
    Test 16g: Phi Coefficient
    Test 16h: Cramér’s Phi Coefficient
    Test 16i: Yule’s Q
    Test 16j: Odds Ratio
    Test 28h: Point-Biserial Correlation Coefficient 
    Test 28i: Biserial Correlation Coefficient 
    Test 28j: Tetrachoric Correlation Coefficient
    Tests 11c/17c/21g/24g/27g: Omega Squared
    Test 21h: Eta Squared
    Test 11b/17b: Cohen’s d Index
    Test 21i/24h/27h: Cohen’s f Index
    '''
    
    def __init__(self, P, Q, alpha, inf_parameters=[], test_title=''):
        super().__init__(P, test_title)
        self.Q=Q
        self.alpha=alpha
        self.inf_parameters=inf_parameters

    def pearson_correlation_coefficient(self):
        ''' Test 28: Pearson Product–Moment Correlation Coefficient
        
        Test for assessing linear relationship between two samples

        Null hypothesis H0: the correlation (rho) between the two variables equals 0
        Alternative hypothesis H1: the correlation between the two variables equals some value other than 0.
        '''
        
        self.test_title = 'Pearson Product–Moment Correlation Coefficient'
        print ('~'+str(self.test_title)+'~')
        
        Samples.get_sample_desciptive_statistics(self.P)
        Samples.get_sample_desciptive_statistics(self.Q)

        stat, p = pearsonr(self.P, self.Q)
        print('stat_true=%.3f, p=%.3f' % (stat, p))        

        #dist_stats = []
        #for _ in range(self.bootstrap_size):
        #    idx = Samples.bootstrap_samples(np.arange(0,self.P.shape[0]), sample_ratio=0.9)
        #    sp = self.P[idx]
        #    sq = self.Q[idx]
        #    num = sum((sp-sp.mean())*(sq-sq.mean()))
        #    den = sum((np.sqrt((sp-sp.mean())**2)*np.sqrt((sq-sq.mean())**2)))
        #    rxy = num/den
        #    sigmar = np.sqrt((1-stat**2)/(len(sp)-2))
        #    stat = rxy / sigmar
        #    dist_stats.append(stat)
        #cutoff, p = Samples.compute_p_value(dist_stats, significance_level=self.alpha, type='one-tail')
        #print('stat=%.3f, p=%.3f' % (stat, p))
        
        if p > self.alpha:
            print('The correlation between the two variables equals 0. Samples probably independent')
        else:
            print('The correlation between the two variables equals some value other than 0. Samples probably dependent. ')
        return (stat, p)


    def spearmans_correlation_coefficient(self):
        ''' Test 29: Spearman’s Rank-Order Correlation Coefficient

        Test for assessing correlation between two samples
        
        H0 (null hypothesis): correlation (rho) between the two variables equals 0
        H1 (alternate hypothesis): the correlation between the two variables equals some value other than 0   
        '''
        
        self.test_title='Spearman’s Rank-Order Correlation Coefficient'
        print ('~'+str(self.test_title)+'~')
        
        Samples.get_sample_desciptive_statistics(self.P)
        Samples.get_sample_desciptive_statistics(self.Q)
        
        from scipy.stats import spearmanr
        stat, p = spearmanr(self.P, self.Q)
        print('stat=%.3f, p=%.3f' % (stat, p))

        if p > self.alpha:
            print('The correlation between the two variables equals 0. Samples probably independent')
        else:
            print('The correlation between the two variables equals some value other than 0. Samples probably dependent. ')
        return (stat, p, dist_stats)        


    def kendall_tau(self):
        ''' Test 30: Kendall’s Tau
        
        Test for assessing correlation between two samples
        
        Null hypothesis H0: the correlation (rho) between the two variables equals 0
        Alternative hypothesis H1: the correlation between the two variables equals some value other than 0.          
        '''
        
        self.test_title='Kendall’s Tau'
        print ('~'+str(self.test_title)+'~')
        
        Samples.get_sample_desciptive_statistics(self.P)
        Samples.get_sample_desciptive_statistics(self.Q)
        
        stat, p = kendalltau(self.P, self.Q)
        print('stat=%.3f, p=%.3f' % (stat, p))
        if p > self.alpha:
            print('The correlation between the two variables equals 0. Samples probably independent')
        else:
            print('The correlation between the two variables equals some value other than 0. Samples probably dependent. ')
        return (stat, p)          

 
    

