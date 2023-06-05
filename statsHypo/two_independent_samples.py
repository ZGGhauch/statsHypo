# -------------------------------------------------------------
# Statistical Hypothesis Tests
# Two independent samples inference
#
# Author: Ziad Ghauch
# -------------------------------------------------------------


from scipy.stats import chi2_contingency
from scipy.stats import ttest_ind
from scipy.stats import mannwhitneyu
from scipy.stats import cramervonmises_2samp
from scipy.stats import ks_2samp
from scipy.stats import epps_singleton_2samp
from scipy.stats import brunnermunzel
from scipy.stats import ansari
from scipy.stats import mood
from sample import Samples



class InferenceTwoIndependentSamples(Samples):
    ''' Inferential statistical tests employed with two independent samples 
    
    Test 11: T-Test for Two Independent Samples
        Test 11a: Hartley’s F Test for Homogeneity of Variance
        Test 11d: Z-test for Two Independent Samples
	    Test 11e: Procedures for Identifying Outliers 
    Test 12: Mann–Whitney U Test
        Test 12a: Randomization Test for Two Independent Samples
        Test 12b: Bootstrap (can be employed for variability)
        Test 12c: Jackknife (can be employed for variability)
    Test 13: Kolmogorov–Smirnov Test for Two Independent Samples
    Test 14: Siegel–Tukey Test for Equal Variability
    Test 15: Moses Test for Equal Variability
    Test 16: Chi square Test
	    Test 16a: Chi-Square Test for Homogeneity
	    Test 16c: Fisher Exact Test
	    Test 16d: Z-test for Two Independent Proportions
		Test 16e: Median Test for Independent Samples 
    Test 21: Single-Factor Between-Subjects Analysis of Variance
        Test 21j: Single-Factor Between-Subjects Analysis of Covariance
    Test 23: Van der Waerden Normal-Scores Test for k Independent Samples 
	Test 36: Cramér-von Mises test for goodness of fit
    Test 37: Epps-Singleton (ES) test statistic
    Test 38: Brunner-Munzel test statistic
    Test 41: Ansari-Bradley test
    Test 42: Mood’s test 
    '''
    
    def __init__(self, P, Q, alpha, inf_parameters=[], test_title=''):
        super().__init__(P, test_title)
        self.Q=Q
        self.alpha=alpha
        self.inf_parameters=inf_parameters


    def t_test_independent(self):
        ''' Test 11: T-test for Two Independent Samples '''

        self.test_title='T-test for Two Independent Samples'
        print ('~'+str(self.test_title)+'~')
        
        Samples.get_sample_desciptive_statistics(self.P)
        Samples.get_sample_desciptive_statistics(self.Q)
        
        stat, p = ttest_ind(self.P, self.Q)

        print('stat=%.3f, p=%.3f' % (stat, p))
        if p > self.alpha:
            print('Probably the same distribution')
        else:
            print('Probably different distributions')
            
            
    def mann_whitney_utest(self):
        ''' Test 12: The Mann–Whitney U Test '''

        self.test_title='Mann–Whitney U-test'
        print ('~'+str(self.test_title)+'~')
        
        Samples.get_sample_desciptive_statistics(self.P)
        Samples.get_sample_desciptive_statistics(self.Q)   
        
        stat, p = mannwhitneyu(self.P, self.Q)

        print('stat=%.3f, p=%.3f' % (stat, p))
        if p > self.alpha:
            print('Probably the same distribution')
        else:
            print('Probably different distributions')            


    def kolmogorov_smirnov_test(self):
        ''' Test 13: The Kolmogorov–Smirnov Test for Two Independent Samples '''
        
        self.test_title='Kolmogorov–Smirnov Test for Two Independent Samples'
        print ('~'+str(self.test_title)+'~')
        
        Samples.get_sample_desciptive_statistics(self.P)
        Samples.get_sample_desciptive_statistics(self.Q)
        
        stat, p = ks_2samp(self.P, self.Q)
        
        print('stat=%.3f, p=%.3f' % (stat, p))
        if p > self.alpha:
            print('Probably the same distribution')
        else:
            print('Probably different distributions')            


    def siegel_tukey_test(self):
        ''' Test 14: Siegel–Tukey Test for Equal Variability '''
    
        self.test_title='Siegel–Tukey Test'
        print ('~'+str(self.test_title)+'~')
    

    def moses_test_variability(self):
        ''' Test 15: Moses Test for Equal Variability '''

        self.test_title='Moses Test for Variability'
        print ('~'+str(self.test_title)+'~')

    
    def chi_square_test(self):
        ''' Test 16: Chi square Test '''
    
        self.test_title='Chi square Test'
        print ('~'+str(self.test_title)+'~')

    

    def chi_square_test_homogeneity(self):
        ''' Test 16a: Chi-Square Test for Homogeneity '''

        self.test_title='The Chi-Square Test for Homogeneity'
        print ('~'+str(self.test_title)+'~')
        
        Samples.get_sample_desciptive_statistics(self.P)
        Samples.get_sample_desciptive_statistics(self.Q)
        
        table = [self.P,self.Q]
        stat, p, dof, expected = chi2_contingency(table)
        print('stat=%.3f, p=%.3f' % (stat, p))
        if p > self.alpha:
            print('Probably independent')
        else:
            print('Probably dependent')


    def single_factor_between_subjects_anova(self):
        ''' Test 21: Single-Factor Between-Subjects Analysis of Variance '''

        self.test_title='Single-Factor Between-Subjects Analysis of Variance'
        print ('~'+str(self.test_title)+'~')
     

    def van_der_waerden_normal_scores(self):
        ''' Test 23: Van der Waerden Normal-Scores Test for k Independent Samples '''
    
        self.test_title='Van der Waerden Normal-Scores Test for k Independent Samples '
        print ('~'+str(self.test_title)+'~')    
        
            
    def cramer_von_mises_goodness_of_fit_test(self):
        ''' Test 36: Cramér-von Mises test for goodness of fit. '''
        
        self.test_title='Cramér-von Mises Test for Goodness of Fit'
        print ('~'+str(self.test_title)+'~')
        
        Samples.get_sample_desciptive_statistics(self.P)
        Samples.get_sample_desciptive_statistics(self.Q)
        
        stat, p = cramervonmises_2samp(self.P, self.Q, method='exact')
        
        print('stat=%.3f, p=%.3f' % (stat, p))
        if p > self.alpha:
            print('Probably the same distribution')
        else:
            print('Probably different distributions')            

        
    def epps_singleton_test(self):
        ''' Test 37: Epps-Singleton (ES) Test Statistic '''

        self.test_title='Epps-Singleton (ES) Test Statistic'
        print ('~'+str(self.test_title)+'~')
        
        Samples.get_sample_desciptive_statistics(self.P)
        Samples.get_sample_desciptive_statistics(self.Q)

        stat, p = epps_singleton_2samp(self.P, self.Q)

        print('stat=%.3f, p=%.3f' % (stat, p))
        if p > self.alpha:
            print('Probably the same distribution')
        else:
            print('Probably different distributions')            
                     

    def brunner_munzel_test(self):
        ''' Test 38: Brunner-Munzel Test Statistic '''

        self.test_title='Brunner-Munzel Test Statistic'
        print ('~'+str(self.test_title)+'~')
        
        Samples.get_sample_desciptive_statistics(self.P)
        Samples.get_sample_desciptive_statistics(self.Q)
        
        stat, p = brunnermunzel(self.P, self.Q)

        print('stat=%.3f, p=%.3f' % (stat, p))
        if p > self.alpha:
            print('Probably the same distribution')
        else:
            print('Probably different distributions')            
        
        
    def ansari_bradley_test(self):
        ''' Test 41: Ansari-Bradley Test '''

        self.test_title='Ansari-Bradley Test'
        print ('~'+str(self.test_title)+'~')
        
        Samples.get_sample_desciptive_statistics(self.P)
        Samples.get_sample_desciptive_statistics(self.Q)

        stat, p = ansari(self.P, self.Q)
        
        print('stat=%.3f, p=%.3f' % (stat, p))
        if p > self.alpha:
            print('Probably the same distribution')
        else:
            print('Probably different distributions')            
                   
 
    def moods_test(self):
        ''' Test 42: Mood’s Test  ''' 
        
        self.test_title='Mood’s Test'
        print ('~'+str(self.test_title)+'~')

        Samples.get_sample_desciptive_statistics(self.P)
        Samples.get_sample_desciptive_statistics(self.Q)

        stat, p = mood(self.P, self.Q)
        
        print('stat=%.3f, p=%.3f' % (stat, p))
        if p > self.alpha:
            print('Probably the same distribution')
        else:
            print('Probably different distributions')            
 
    
 
    
 
    
 
    
 
    
 
    
            
