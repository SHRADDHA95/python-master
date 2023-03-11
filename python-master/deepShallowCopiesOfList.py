## Use this file to write your code ##
import copy

ls_ls = [[1,2,3,4,5],["A","B", "C"],["India" ,"South Korea"],["Hindi","Korean"]]

new_ls=ls_ls.copy()
print("#shallow 1" , new_ls ,  "\n")

deep_copied = copy.deepcopy(new_ls)
print("Deep copied #1" , deep_copied , "\n")

new_ls[0][1] = 8
print("#shallow 2 -->" , new_ls ,)
print("#shallow 2 -->original list" , ls_ls , "\n")


deep_copied[1][2]="P"
print("Orginial list --> " , ls_ls)
print("Modified list for deep copy --> " , deep_copied)
