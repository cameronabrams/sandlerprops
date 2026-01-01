from sandlerprops.properties import PropertiesDatabase, get_database
import unittest

class Test_db(unittest.TestCase):
   def setUp(self):
      P = get_database()
      self.P = P

   def test_read(self):
      expected_columns=['No','Formula', 'Name', 'Molwt', 'Tfp', 'Tb', 'Tc', 'Pc',
         'Vc', 'Zc', 'Omega', 'Dipm', 'CpA', 'CpB', 'CpC', 'CpD', 'dHf', 'dGf',
         'Eq', 'VpA', 'VpB', 'VpC', 'VpD', 'Tmin', 'Tmax', 'Lden', 'Tden']
      self.assertTrue(all([x==y for x,y in zip(self.P.properties,expected_columns)]))

   def test_get_methane(self):
      methane = self.P.get_compound('methane')
      self.assertEqual(methane.Formula, 'CH4')
      self.assertEqual(methane.atomdict, {'C':1,'H':4})

   def test_get_phosgene(self):
      phosgene = self.P.get_compound('phosgene')
      self.assertEqual(phosgene.Formula, 'COCl2')
      self.assertEqual(phosgene.atomdict, {'C':1,'O':1,'Cl':2})

   def test_get_trifluoroacetic_acid(self):
      tfa = self.P.get_compound('trifluoroacetic acid')
      self.assertNotEqual(tfa.Formula, 'C2HF3O2') # I reorder formulas
      self.assertEqual(tfa.atomdict, {'C':2,'H':1,'F':3,'O':2})

   def test_get_valeraldehyde(self):
      valeraldehyde = self.P.get_compound('valeraldehyde')
      self.assertEqual(valeraldehyde.Formula, 'C5H10O') # makes sure zero is not replaced by O
      self.assertEqual(valeraldehyde.atomdict, {'C':5,'H':10,'O':1})

   def test_get_nonexistent(self):
      no_cmp = self.P.get_compound('unobtainium')
      self.assertEqual(no_cmp.Name, 'unobtainium')
      self.assertEqual(no_cmp.Formula, 'unobtainium')
      self.assertEqual(no_cmp.Molwt, 0.0)

   def test_get_nonexistant_with_ef(self):
      no_cmp = self.P.get_compound('X3Y4')
      self.assertEqual(no_cmp.Formula, 'X3Y4')
      self.assertEqual(no_cmp.atomdict, {'X':3,'Y':4})
      self.assertEqual(no_cmp.Molwt, 0.0)
    