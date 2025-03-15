import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from GhostData.GhostData import SetPessoa
a = SetPessoa()


print(a.get_data())




