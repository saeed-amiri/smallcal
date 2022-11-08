from constants import MolarMass
import typing


class Doc:
    """calculate weight precentage, molar, molal,..."""


class WeightPrecentage:
    """calculate weight precentage of the each system"""
    def __init__(self) -> None:
        pass

    def cal_weight_precent(self,
                           a_type: str,  # type of 1st sample
                           num_a: int,  # Number of molecules of 1st
                           num_b: int,  # Number of molecules of 2nd
                           b_type: str  # type of 2nd sample
                           ) -> any:
        """calculate weight percent"""
        wghtper: float  # Weight percent of the samples
        


