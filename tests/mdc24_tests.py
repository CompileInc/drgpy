import unittest
from drgpy.msdrg import DRGEngine

class TestMCD24(unittest.TestCase):

    def test_mdcs24(self):

        de = DRGEngine()

        drg_lst = de.get_drg_all(["S00459A"], ["001607B"])
        self.assertTrue("955" in drg_lst)
 
        drg_lst = de.get_drg_all(["S00459A"], ["0L8J0ZZ"])
        self.assertTrue("956" in drg_lst)
 
        drg_lst = de.get_drg_all(["S00459A"], ["XRGD0F3"])
        self.assertTrue("959" in drg_lst)
 
        drg_lst = de.get_drg_all(["S00459A"], ["XRGD0F3"])
        self.assertTrue("959" in drg_lst)
 
if __name__=="__main__":
    unittest.main()




