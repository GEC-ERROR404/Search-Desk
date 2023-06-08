import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score,confusion_matrix,roc_curve,classification_report
from scikitplot.metrics import plot_confusion_matrix
df_train = pd.read_csv("D:/test/train.txt",delimiter=';',names=['text','label'])
df_val = pd.read_csv("D:/test/val.txt",delimiter=';',names=['text','label'])
df = pd.concat([df_train,df_val])
df.reset_index(inplace=True,drop=True)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df_train = pd.read_csv("D:/test/train.txt",delimiter=';',names=['text','label'])
df_val = pd.read_csv("D:/test/val.txt",delimiter=';',names=['text','label'])
df = pd.concat([df_train,df_val])
df.reset_index(inplace=True,drop=True)
print("Shape of the DataFrame:",df.shape)
print(df.sample(5))
sns.countplot(x=df.label)