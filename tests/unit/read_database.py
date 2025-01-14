from sandlerprops.properties import Properties
def test_read():
    P=Properties()
    expected_columns=['Formula', 'Name', 'Molwt', 'Tfp (K)', 'Tb (K)', 'Tc (K)', 'Pc (bar)',
       'Vc', 'Zc', 'Omega', 'Dipm', 'CpA', 'CpB', 'CpC', 'CpD', 'dHf', 'dGf',
       'Eq', 'VpA', 'VpB', 'VpC', 'VpD', 'Tmin', 'Tmax', 'Lden', 'Tden']
    obtained_columns=list(P.D.columns)
    assert all([x==y for x,y in zip(obtained_columns,expected_columns)])
    