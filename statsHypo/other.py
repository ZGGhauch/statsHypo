# -------------------------------------------------------------
# Statistical Hypothesis Tests
# Other inference methods
#
# Author: Ziad Ghauch
# -------------------------------------------------------------


from sample import Samples


class Other(Samples):
    ''' Miscellaneous procedures 
    
    Test 28n: Procedure for comparing k studies with respect to significance level
    Test 28o: Stouffer procedure for obtaining a combined significance level for k studies
    Test 28p: Procedure for comparing k studies with respect to effect size
    Test 28q: Procedure for obtaining a combined effect size for k studies
    '''
    def __init__(self, P, Q, alpha, inf_parameters=[], test_title=''):
        super().__init__(P, test_title)
        self.Q=Q
        self.alpha=alpha
        self.inf_parameters=inf_parameters



    

