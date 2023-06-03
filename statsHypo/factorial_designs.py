# -------------------------------------------------------------
# Statistical Hypothesis Tests
# Factorial design inference
#
# Author: Ziad Ghauch
# -------------------------------------------------------------


from sample import Samples


class InferenceFactorialDesigns(Samples):
    ''' Inferential statistical tests employed with factorial designs 
    
    Test 27: Between-Subjects Factorial Analysis of Variance
    Test 27a: Multiple T-tests/Fisher’s LSD Test
    Test 27b: Bonferroni–Dunn Test
    Test 27c: Tukey’s HSD Test
    Test 27d: Newman–Keuls Test
    Test 27e: Scheffé Test
    Test 27f: Dunnett Test
    Test 27i: Factorial Analysis of Variance for a Mixed Design
    Test 27j: Within-Subjects Factorial Analysis of Variance
    '''
    def __init__(self, P, Q, alpha, inf_parameters=[], test_title=''):
        super().__init__(P, test_title)
        self.Q=Q
        self.alpha=alpha
        self.inf_parameters=inf_parameters


   

