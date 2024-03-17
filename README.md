# CS 247 Project
## Running the models
### Locally
Create a virtual environment
```
python3 -m venv venv
```
Activate the virtual environment
```
source venv/bin/activate
```
Choose which model you want to run by using
```
cd model
```
Download the necessary requirements
```
pip3 install -r requirements.txt
```
Open the `model` Jupyter notebook using
```
jupyter notebook model.ipynb
```
Run all cells in the notebook by using Cell > Run All

Note that the requirements.txt is large because it uses `pip freeze --local` when run on Google Colab which uses all of the Colab Python versions.
### Colab
Upload the notebook to Google Drive then open it and click Runtime > Run All.
## References
Attribute GNN is from the
[AGNN for strict cold start paper](https://ieeexplore.ieee.org/abstract/document/9261110)
and uses the [paper's code](https://github.com/lylbaidu/AGNN)
