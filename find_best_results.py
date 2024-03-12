import heapq
from os import listdir
from os.path import isfile, join

path = "Results"
result_files = [path + "/" + f for f in listdir(path) if isfile(join(path, f))]


def parse_result(filename):
    with open(filename) as f:
        contents = f.read()
    lines = contents.split("\n")
    # format is: metric = value
    # rmse, mse, mae
    rmse = lines[0].split("=")[1][1:]
    mae = lines[2].split("=")[1][1:]
    # string is formatted as python list
    rmse = eval(rmse)
    mae = eval(mae)
    min_rmse = min(rmse)
    min_mae = min(mae)
    return min_rmse, min_mae


# smallest_rmse, smallest_mae, smallest_result = -1, -1, ""
results = []
for result in result_files:
    min_rmse, min_mae = parse_result(result)
    heapq.heappush(results, (min_rmse, min_mae, result))

sorted_results = [heapq.heappop(results) for _ in range(len(results))]
for result in sorted_results:
    print(f"{result[2].split('/')[1]} with RMSE {result[0]}, MAE: {result[1]}")
