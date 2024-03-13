import heapq
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt

path = "../Results"
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
    return min_rmse, min_mae, rmse, mae


# smallest_rmse, smallest_mae, smallest_result = -1, -1, ""
results = []
for result in result_files:
    min_rmse, min_mae, rmse, mae = parse_result(result)
    heapq.heappush(results, (min_rmse, min_mae, result, rmse, mae))

sorted_results = [heapq.heappop(results) for _ in range(len(results))]
# for result in sorted_results:
#     print(f"{result[2].split('/')[1]} with RMSE {result[0]}, MAE: {result[1]}")

num_epochs = len(mae)
rmse_results = [result[3] for result in sorted_results[:3]]
mae_results = [result[4] for result in sorted_results[:3]]
labels = ["LLMRec", "ColdGAN", "Base AttributeGNN"]
for i, rmse in enumerate(rmse_results):
    plt.plot(range(1, num_epochs+1), rmse, label=labels[i])
plt.xlabel("Epoch")
plt.ylabel("RMSE")
plt.title("RMSE of base AttributeGNN vs augmented with ColdGAN or LLMRec data")
plt.legend()
# integer x label: https://stackoverflow.com/a/52229882/14842908
plt.xticks(range(1, num_epochs+1))
plt.savefig("best_rmse_results.png")
plt.show()

for i, mae in enumerate(mae_results):
    plt.plot(range(1, num_epochs+1), mae, label=labels[i])
plt.xlabel("Epoch")
plt.ylabel("MAE")
plt.title("MAE of base AttributeGNN vs augmented with ColdGAN or LLMRec data")
plt.xticks(range(1, num_epochs+1))
plt.legend()
plt.savefig("best_mae_results.png")
plt.show()
