from matplotlib_venn import venn3
import matplotlib.pyplot as plt

oyster = 100
maitake = 33
lions_mane = 23
both_oyster_maitake = 23
both_maitake_lions_mane = 12
both_oyster_lions_mane = 10
all_3 = 2

venn3([set(['Oyster']*oyster + ['Maitake']*maitake + ['Lions Mane']*lions_mane),
      set(['Oyster', 'Maitake']*both_oyster_maitake),
      set(['Maitake', 'Lions Mane']*both_maitake_lions_mane),
      set(['Oyster', 'Lions Mane']*both_oyster_lions_mane),
      set(['Oyster', 'Maitake', 'Lions Mane']*all_3)],
      set_labels = ('Oyster', 'Maitake', 'Lions Mane'))

plt.show()
