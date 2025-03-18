"""
    Beckhoff KL1104
    4 channel digital input
"""

from .io_module import io_module

class Beckhoff_KL1104(io_module):
    
    def __init__(self):
        print()