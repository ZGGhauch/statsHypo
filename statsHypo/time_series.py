# -------------------------------------------------------------
# Statistical Hypothesis Tests
# Time series inference
#
# Author: Ziad Ghauch
# -------------------------------------------------------------


from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import kpss
from sample import Samples



class TimeSeries(Samples):
    ''' Additional hypothesis testing procedures for time series  
    
    Test 33: Augmented Dickey-Fuller Unit Root Test
    Test 34: Kwiatkowski-Phillips-Schmidt-Shin
    '''
    
    def __init__(self, P, alpha, test_title=''):
        super().__init__(P,test_title)
        self.alpha=alpha
    
    
    def augmented_dickey_fuller_test(self):
        ''' Test 33: Augmented Dickey-Fuller Unit Root Test '''

        self.test_title='Augmented Dickey-Fuller Unit Root Test'
        print ('~'+str(self.test_title)+'~')
        
        Samples.get_sample_desciptive_statistics(self.P)
        
        stat, p, lags, obs, crit, t = adfuller(self.P)
        print('stat=%.3f, p=%.3f' % (stat, p))
        
        if p > self.alpha:
            print('Probably not Stationary')
        else:
            print('Probably Stationary')


    def kwiatkowski_phillips_schmidt_shin_test(self):
        ''' Test 34: Kwiatkowski-Phillips-Schmidt-Shin '''

        self.test_title='Kwiatkowski-Phillips-Schmidt-Shin'
        print ('~'+str(self.test_title)+'~')
        
        Samples.get_sample_desciptive_statistics(self.P)
        
        stat, p, lags, crit = kpss(self.P)
        print('stat=%.3f, p=%.3f' % (stat, p))
        if p > self.alpha:
            print('Probably Stationary')
        else:
            print('Probably not Stationary')  
    
    
    

