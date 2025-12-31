# sandlerprops

> A Python interface to the pure-component properties database that originally accompanied the textbook _Chemical, Biochemical, and Engineering Thermodynamics_ (4th edition) by Stan Sandler (Wiley, USA).

## Installation

```sh
pip install sandlerprops
```

## Usage example

### Command-line interface

```bash
$ sandlerprops find methane
Found exact match: methane (index 116)
$ sandlerprops find methanx
methanx not found.  Here are similars:
methane
methanol
ethane
ethanol
methylal
methyl amine
nitromethane
deutromethane
methyl silane
dimethylamine
$ sandlerprops show benzene
Properties of benzene (index 343):
  No        : 343
  Formula   : C6H6
  Name      : benzene
  Molwt     :  78.114    g/mol
  Tfp       :  278.7     K
  Tb        :  353.2     K
  Tc        :  562.2     K
  Pc        :  48.90     bar
  Vc        :  259.000   m3/mol
  Zc        :  0.271
  Omega     :  0.212
  Dipm      : 0
  CpA       : -33.92     J/mol-K
  CpB       :  0.4739    J/mol-K2
  CpC       : -3.0170e-04 J/mol-K3
  CpD       :  7.1300e-08 J/mol-K4
  dHf       :  82980.0   J/mol
  dGf       :  129700.0  J/mol
  Eq        : 1
  VpA       : -6.98273
  VpB       :  1.33213
  VpC       : -2.62863
  VpD       : -3.33399
  Tmin      :  288.0     K
  Tmax      :  562.2     K
  Lden      :  0.885
  Tden      :  289.0
```

### API

```python
>>> from sandlerprops.properties import Properties as P
>>> m = P.get_compound('methane')
>>> m.Molwt
16.043
>>> p.U.Molwt
'g/mol'
>>> m.Tc
190.4
>>> p.U.Tc
'K'
>>> e = P.get_compound('ethanz')
ethanz not found.  Here are similars:
ethane
methane
ethanol
methanol
ethyl amine
ethylene
methylal
methyl amine
ethylbenzene
nitromethane
```

## Release History

* 0.2.1
    * updated formatting
* 0.1.0
    * command-line interface
* 0.0.3
    * returns similar names found in database if requested name is not found
* 0.0.2
    * Updated dependencies
* 0.0.1
    * Initial version

## Meta

Cameron F. Abrams – cfa22@drexel.edu

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/cameronabrams](https://github.com/cameronabrams/)

## Contributing

1. Fork it (<https://github.com/cameronabrams/sandlerprops/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
