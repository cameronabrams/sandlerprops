# Author: Cameron F. Abrams <cfa22@drexel.edu>

import pandas as pd
import numpy as np

from argparse import Namespace
from difflib import SequenceMatcher
from importlib.resources import files

class PropertiesDatabase:
    datafile_path = files('sandlerprops.resources').joinpath('data','properties_database.csv')
    def __init__(self):
        D = pd.read_csv(self.datafile_path, header=0, index_col=None)
        self.D = D.rename(columns={
            'Tfp (K)': 'Tfp',
            'Tb (K)': 'Tb',
            'Tc (K)': 'Tc',
            'Pc (bar)': 'Pc'})
        unitlist = [
            '', # no. (unique)
            '', # formula
            '', # name (unique)
            'g/mol', # molecular weight
            'K', # triple point temperature
            'K', # boiling point temperature
            'K', # critical temperature
            'bar', # critical pressure
            'm3/mol', # critical volume
            '', # critical compressibility
            '', # acentric factor
            '', # DIPM
            'J/mol-K', # ideal gas heat capacity coeff 1
            'J/mol-K2', # ideal gas heat capacity coeff 2
            'J/mol-K3', # ideal gas heat capacity coeff 3
            'J/mol-K4', # ideal gas heat capacity coeff 4
            'J/mol', # ideal gas enthalpy of formation at 298.15 K
            'J/mol', # ideal gas entropy of formation at 298.15 K   
            '', # vapor pressure equation type number
            '', # vapor pressure coeff 1
            '', # vapor pressure coeff 2
            '', # vapor pressure coeff 3
            '', # vapor pressure coeff 4
            'K', # vapor pressure temperature range min
            'K', # vapor pressure temperature range max
            '', # liquid density at Tden
            ''] # liquid density temperature for reference
        formatters = [
            '{:<10d}', # no. (unique)
            '{:<s}', # formula
            '{:<s}', # name (unique)
            '{:< 10.3f}', # molecular weight
            '{:< 10.1f}', # triple point temperature
            '{:< 10.1f}', # boiling point temperature
            '{:< 10.1f}', # critical temperature
            '{:< 10.2f}', # critical pressure
            '{:< 10.3f}', # critical volume
            '{:< 10.3f}', # critical compressibility
            '{:< 10.3f}', # acentric factor
            '{:<10g}', # DIPM
            '{:< 10.2f}', # ideal gas heat capacity coeff 1
            '{:< 10.4f}', # ideal gas heat capacity coeff 2
            '{:< 10.4e}', # ideal gas heat capacity coeff 3
            '{:< 10.4e}', # ideal gas heat capacity coeff 4
            '{:< 10.1f}', # ideal gas enthalpy of formation at 298.15 K
            '{:< 10.1f}', # ideal gas entropy of formation at 298.15 K   
            '{:<10d}', # vapor pressure equation type number
            '{:< 10.5f}', # vapor pressure coeff 1
            '{:< 10.5f}', # vapor pressure coeff 2
            '{:< 10.5f}', # vapor pressure coeff 3
            '{:< 10.5f}', # vapor pressure coeff 4
            '{:< 10.1f}', # vapor pressure temperature range min
            '{:< 10.1f}', # vapor pressure temperature range max
            '{:< 10.3f}', # liquid density at Tden
            '{:< 10.1f}'] # liquid density temperature for reference
        self.properties = list(self.D.columns)
        unitdict = {k: v for k,v in zip(self.properties, unitlist)}
        formatterdict = {k: v for k,v in zip(self.properties, formatters)}
        self.U = Namespace(**unitdict)
        self.F = Namespace(**formatterdict)

    def show_properties(self, args: Namespace = None):
        for p in self.properties:
            unit = self.U.__dict__[p]
            if unit:
                fmted = self.F.__dict__[p].format(p)
                print(f'{fmted} ({unit})')
            else:
                print(f'{fmted}')

    def find_compound(self, args: Namespace):
        compound_name = args.compound_name
        record = self.get_compound(compound_name)
        if record is not None:
            print(f'Found exact match: {record.Name} (index {record.No})')

    def show_compound_properties(self, args: Namespace):
        compound_name = args.compound_name
        record = self.get_compound(compound_name)
        if record is not None:
            print(f'Properties of {record.Name} (index {record.No}):')
            for p in self.properties:
                value = record.__dict__[p]
                unit = self.U.__dict__[p]
                formatted_value = self.F.__dict__[p].format(value)
                if unit:
                    print(f'  {p:<10s}: {formatted_value} {unit}')
                else:
                    print(f'  {p:<10s}: {formatted_value}')

    def get_compound(self, name, near_matches=10):
        row = self.D[self.D['Name'] == name]
        if not row.empty:
            d = row.to_dict('records')[0]
            return Namespace(**d)
        else:
            print(f'{name} not found.  Here are similars:')
            scores = []
            for n in self.D['Name']:
                scores.append(SequenceMatcher(None, name, n).ratio())
            scores = np.array(scores)
            si = np.argsort(scores)
            sorted_names = np.array(self.D['Name'])[si]
            top_sorted_names = sorted_names[-near_matches:][::-1]
            for n in top_sorted_names:
                print(n)
        return None
        
# Properties = PropertiesDatabase()
