frozen_set_1 = frozenset({'C','A','B','D'})
print("frozen_set_1 :",frozen_set_1)

frozen_set_2 = frozenset({2,'A','C',4})
print("frozen_set_2 :",frozen_set_2)

frozen_set_union = frozenset.union(frozen_set_1,frozen_set_2)
print("frozen_set_union :",frozen_set_union)

frozen_set_common = frozenset.intersection(frozen_set_1,frozen_set_2)
print("frozen_set_common :",frozen_set_common)

frozen_set_difference = frozenset.difference(frozen_set_1,frozen_set_2)
print("frozen_set_difference :",frozen_set_difference)

frozen_set_distinct  = frozen_set_2.symmetric_difference(frozen_set_1)
print("frozen_set_distinct :",frozen_set_distinct)

