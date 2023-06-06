# -------------------------------------------------------------
# Statistical Hypothesis Tests
# Two or more independent samples inference
#
# Author: Ziad Ghauch
# -------------------------------------------------------------


from sample import Samples
from scipy.stats import kruskal
from scipy.stats import f_oneway
from scipy.stats import tukey_hsd
from scipy.stats import levene
from scipy.stats import bartlett
from scipy.stats import fligner
from scipy.stats import median_test




class InfTwoOrMoreIndepSamp(Samples):
    ''' Inferential statistical tests employed with two or more independent Samples 
    
    Test 21: Single-Factor Between-Subjects Analysis of Variance
        Test 21a: Multiple T-tests/Fisher’s LSD Test
        Test 21b: Bonferroni–Dunn test
        Test 21c: Tukey’s HSD Test
        Test 21d: Newman–Keuls Test
        Test 21e: Scheffé Test
        Test 21f: Dunnett Test
        Test 21j: Single-Factor Between-Subjects Analysis of Covariance
    Test 22: Kruskal–Wallis One-Way Analysis of Variance by Ranks
    Test 23: Van der Waerden Normal-Scores Test for k Independent Samples
    Test 44: Levene test 
    Test 45: Bartlett’s test
    Test 48: Fligner-Killeen
    Test 49: Mood’s median test
    '''
    
    def __init__(self, P, *listQ, alpha, inf_parameters=[], test_title=''):
        super().__init__(P,test_title)
        self.Q=[] 
        self.Q.append([q for q in listQ])
        self.alpha=alpha
        self.inf_parameters=inf_parameters



    def single_factor_anova(self):
        ''' Test 21: Single-Factor Between-Subjects Analysis of Variance '''

        self.test_title='Single-Factor Between-Subjects Analysis of Variance'
        print ('~'+str(self.test_title)+'~')
            
        Samples.get_sample_desciptive_statistics(self.P)
        [Samples.get_sample_desciptive_statistics(q) for q in self.Q[0]]
        
        stat, p = f_oneway(self.P, *self.Q[0])
        
        print('stat=%.3f, p=%.3f' % (stat, p))
        if p > self.alpha:
            print('Probably the same distribution')
        else:
            print('Probably different distributions')    


    def tukeys_hsd_test(self):
        ''' Test 21c: Tukey’s HSD Test '''

        self.test_title='Tukey’s HSD Test'
        print ('~'+str(self.test_title)+'~')
        
        Samples.get_sample_desciptive_statistics(self.P)
        [Samples.get_sample_desciptive_statistics(q) for q in self.Q[0]]  
        
        stat, p = tukey_hsd(self.P, *self.Q[0])

        print('stat=%.3f, p=%.3f' % (stat, p))
        if p > self.alpha:
            print('Probably the same distribution')
        else:
            print('Probably different distributions')



    def kruskal_wallis_oneway_analysis_variance(self):
        ''' Test 22: Kruskal–Wallis One-Way Analysis of Variance by Ranks '''

        self.test_title='Kruskal–Wallis One-Way Analysis of Variance Test'
        print ('~'+str(self.test_title)+'~')
        
        Samples.get_sample_desciptive_statistics(self.P)
        [Samples.get_sample_desciptive_statistics(q) for q in self.Q[0]]  

        stat, p = kruskal(self.P, *self.Q[0])
        print('stat=%.3f, p=%.3f' % (stat, p))
        if p > self.alpha:
            print('Probably the same distribution')
        else:
            print('Probably different distributions')

    
    def van_der_waerden_normal_test_k_independent_samples(self):
        ''' Test 23: Van der Waerden Normal-Scores Test for k Independent Samples '''

        self.test_title='Van der Waerden Normal-Scores'
        print ('~'+str(self.test_title)+'~')
    

    def levene_test(self):
        ''' Test 44: Levene Test  '''

        self.test_title='Levene Test'
        print ('~'+str(self.test_title)+'~')
                
        Samples.get_sample_desciptive_statistics(self.P)
        [Samples.get_sample_desciptive_statistics(q) for q in self.Q[0]]  
        
        stat, p = levene(self.P, *self.Q[0])

        print('stat=%.3f, p=%.3f' % (stat, p))
        if p > self.alpha:
            print('Probably equal variance')
        else:
            print('Probably non equal variance')


    def bartletts_test(self):
        ''' Test 45: Bartlett’s Test '''

        self.test_title='Bartlett’s Test'
        print ('~'+str(self.test_title)+'~')
        
        Samples.get_sample_desciptive_statistics(self.P)
        [Samples.get_sample_desciptive_statistics(q) for q in self.Q[0]]
        
        stat, p = bartlett(self.P, *self.Q[0])

        print('stat=%.3f, p=%.3f' % (stat, p))
        if p > self.alpha:
            print('Probably equal variance')
        else:
            print('Probably non equal variance')


    def fligner_killeen_test(self):
        ''' Test 48: Fligner-Killeen Test '''

        self.test_title='Fligner-Killeen Test'
        print ('~'+str(self.test_title)+'~')
                
        Samples.get_sample_desciptive_statistics(self.P)
        [Samples.get_sample_desciptive_statistics(q) for q in self.Q[0]]
        
        stat, p = fligner(self.P, *self.Q[0])

        print('stat=%.3f, p=%.3f' % (stat, p))
        if p > self.alpha:
            print('Probably equal variance')
        else:
            print('Probably non equal variance')


    def moods_median_test(self):
        ''' Test 49: Mood’s median Test '''

        self.test_title='Mood’s median Test'
        print ('~'+str(self.test_title)+'~')
        
        Samples.get_sample_desciptive_statistics(self.P)
        [Samples.get_sample_desciptive_statistics(q) for q in self.Q[0]]
        
        stat, p = median_test(self.P, *self.Q[0])
        
        print('stat=%.3f, p=%.3f' % (stat, p))
        if p > self.alpha:
            print('Probably equal medians')
        else:
            print('Probably non equal medians')
       













