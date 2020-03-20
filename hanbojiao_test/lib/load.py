import pandas as pd
import numpy as np
import time
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.externals import joblib
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
import xgboost
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
import time
from scipy.io import loadmat
from sklearn.preprocessing import StandardScaler

# class load():
#     def load_data(filename):
#         raw_data = pd.read_csv(filename)
#         raw_data['filename'] = [str(i).zfill(4)+'.jpg' for i in raw_data['Index'].tolist()]
#         raw_data['pointsname'] = [str(i).zfill(4)+'.mat' for i in raw_data['Index'].tolist()]
#         return raw_data

#     #read points data from mat data
#     def load_points(points_path,data):
#         n = data.shape[0]
#         points_data = np.zeros([n,156])
#         start_time = time.time()
#         for i in range(n):
#             result = loadmat(points_path+data['pointsname'][i])
#             key = sorted(result.keys())[-1]
#             points = result[key]
#             points_data[i,:]=points.reshape(156)
#         print("--- %s seconds ---" % (time.time() - start_time))
#         return points_data
    
    
    