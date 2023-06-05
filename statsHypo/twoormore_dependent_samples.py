# -------------------------------------------------------------
# Statistical Hypothesis Tests
# Two or more dependent samples inference
#
# Author: Ziad Ghauch
# -------------------------------------------------------------


from sample import Samples
from scipy.stats import friedmanchisquare



class InferenceTwoOrMoreDependentSamples(Samples):
    ''' Inferential statistical tests employed with two or more dependent Samples
    
    Test 24: Single-Factor Within-Subjects Analysis of Variance
        Test 24a: Multiple t Tests/Fisher’s LSD Test
        Test 24b: Bonferroni–Dunn Test
        Test 24c: Tukey’s HSD Test
        Test 24d: Newman–Keuls Test
        Test 24e: Scheffé Test
        Test 24f: Dunnett Test
    Test 25: Friedman Two-Way Analysis of Variance by Ranks
    Test 26: Cochran Q Test
    '''
    
    def __init__(self, P, *listQ, alpha, inf_parameters=[], test_title=''):
        super().__init__(P, test_title)
        self.Q=[] 
        self.Q.append([q for q in listQ])
        self.alpha=alpha
        self.inf_parameters=inf_parameters

    
    def single_factor_anova(self):
        ''' Test 24: Single-Factor Within-Subjects Analysis of Variance '''
        
        self.test_title='Single-Factor Within-Subjects ANOVA'
        print ('~'+str(self.test_title)+'~')
        
 
    def friedman_twoway_analysis_variance(self):
        ''' Test 25: Friedman Two-Way Analysis of Variance by Ranks'''

        self.test_title='Friedman Two-Way Analysis of Variance by Ranks'
        print ('~'+str(self.test_title)+'~')
        
        Samples.get_sample_desciptive_statistics(self.P)
        [Samples.get_sample_desciptive_statistics(q) for q in self.Q[0]]
        
        stat, p = friedmanchisquare(self.P, *self.Q[0])
        
        print('stat=%.3f, p=%.3f' % (stat, p))
        if p > self.alpha:
            print('Probably same distribution')
        else:
            print('Probably different distributions')
        

    def cochran_q_test(self):
        ''' Test 26: Cochran Q Test '''

        self.test_title='Cochran Q Test'
        print ('~'+str(self.test_title)+'~')