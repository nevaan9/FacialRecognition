import sklearn
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
i = 0
for key in cancer:
    print(key)

print(len(cancer['target']))
print(len(cancer['data']))

print(cancer['data'][0])