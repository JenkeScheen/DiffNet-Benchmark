import lomap
import matplotlib.pyplot as plt

db_mol = lomap.DBMolecules("test/basic/")

strict, loose = db_mol.build_matrices()

nx_graph = db_mol.build_graph() 
