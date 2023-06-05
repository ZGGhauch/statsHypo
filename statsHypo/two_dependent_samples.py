# -------------------------------------------------------------
# Statistical Hypothesis Tests
# Two dependent samples inference
#
# Author: Ziad Ghauch
# -------------------------------------------------------------



from sample import Samples
from scipy.stats import ttest_rel
from scipy.stats import wilcoxon



class InferenceTwoDependentSamples(Samples):
    ''' Inferential statistical tests employed with two dependent samples 
    
    Test 17: T-test for Two Dependent Samples
        Test 17a: T-test for Homogeneity of Variance
        Test 17d: Sandler’s A-test
        Test 17e: Z-test for Two Dependent Samples
    Test 18: Wilcoxon Matched-Pairs Signed-Ranks Test
    Test 19: Binomial Sign Test for Two Dependent Samples
    Test 20: McNemar Test
        Test 20a: Bowker Test of Symmetry
    '''

    def __init__(self, P, Q, alpha, inf_parameters=[], test_title=''):
        super().__init__(P, test_title)
        self.Q=Q
        self.alpha=alpha
        self.inf_parameters=inf_parameters

    
    def t_test_dependent(self):
        ''' Test 17: T-test for Two Dependent Samples '''

        self.test_title='T-test for Two Dependent Samples'
        print ('~'+str(self.test_title)+'~')
        
        Samples.get_sample_desciptive_statistics(self.P)
        Samples.get_sample_desciptive_statistics(self.Q)
        
        stat, p = ttest_rel(self.P, self.Q)
        print ('stat=%.3f, p=%.3f'  % (stat,p) )
        
        if p > self.alpha:
            print ('Probably the same distribution')
        else:
            print ('Probably different distributions')
            

    def wilcoxon_matched_pairs_test(self):
        ''' Test 18: Wilcoxon Matched-Pairs Signed-Ranks Test '''

        self.test_title='Wilcoxon Matched-Pairs Signed-Ranks Test'
        print ('~'+str(self.test_title)+'~')
        
        Samples.get_sample_desciptive_statistics(self.P)
        Samples.get_sample_desciptive_statistics(self.Q)
        
        stat, p = wilcoxon(self.P, self.Q)

        print('stat=%.3f, p=%.3f' % (stat, p))
        if p > self.alpha:
            print('Probably the same distribution')
        else:
            print('Probably different distributions')


    def binomial_sign_test_dependent(self):
        ''' Test 19: Binomial Sign Test for Two Dependent Samples '''
        
        self.test_title='Binomial Sign Test for Two Dependent Samples'
        print ('~'+str(self.test_title)+str('~'))


    def mcnemar_test(self):
        ''' Test 20: McNemar Test '''
        
        self.test_title='McNemar Test'
        print ('~'+str(self.test_title)+str('~'))

