from sandlerprops.properties import Properties
import unittest
import os
import shutil

class Test_db(unittest.TestCase):
   def test_read(self):
      P=Properties()
      expected_columns=['Formula', 'Name', 'Molwt', 'Tfp (K)', 'Tb (K)', 'Tc (K)', 'Pc (bar)',
         'Vc', 'Zc', 'Omega', 'Dipm', 'CpA', 'CpB', 'CpC', 'CpD', 'dHf', 'dGf',
         'Eq', 'VpA', 'VpB', 'VpC', 'VpD', 'Tmin', 'Tmax', 'Lden', 'Tden']
      obtained_columns=list(P.D.columns)
      self.assertTrue(all([x==y for x,y in zip(obtained_columns,expected_columns)]))
    