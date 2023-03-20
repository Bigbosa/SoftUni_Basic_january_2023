length = float(input()) * 100
width = float(input()) * 100


all_workspace_of_cols = (width - 100) // 70
all_workspace_cols = length // 120

all_spaces = all_workspace_of_cols * all_workspace_cols - 3
print(int(all_spaces))

