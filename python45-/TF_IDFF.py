# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# from nltk.stem import wordNetLemmatizer

# nltk.download('punkt');
# nltk.download('stopwords');
# nltk.download('wordnet');
# nltk.download('punk_tab'); # newer nltk version

# text = 'Students are learning python for ai and machine learning in bhopal!'

# #Step 1: Ttokenise - split into words

# tokens = word_tokenize(text.lower())
# print('Tokens:', tokens)

# #step 2 : Remove stopwords (common words that add no meaning)

# stop = set(stopwords.words('english'))
# filtered = [w for w in tokens if w not in stop and w.isalpha()]


# #step 3: Lemmatise - reduce to root form 
# lemma = wordNetLemmatizer()
# final = [lemma.lemmatize(w) for w in filtered]
# print('after lemmatization:', final)

# #TF-IDF - convert text to number for Ml

# from sklearn.feature_extraction.text import TfidfVectorizer
# docs = ['Python is great for data science ','Machine learning is amzaing ','Ai is the future of tehnology']
# tfidf = TfidfVectorizer()
# matrix = tfidf.fit_transform(docs)
# print('TF-IDF shape:', matrix.shape)  #(3 docs , N unique words)
# print('Features names:', tfidf.get_feature_names_out())



from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#Tranning data product reviews
reviews = [
    ('This product is absolutely amzaing ! highly recommend!', 1),
    ('Great quality and fast delevery very happy!' ,1),
    ('Excellent value for money . work perfectly!', 1),
    ('Loved it i definately but it again.',1),
    ('Super satisfied with this purchase!',1),
    ('Five stars! Outstanding product!',1),
    ('Terrible quality. Broke after 2 days ',0),
    ('Worst purchase ever . complete waste of money!',0),
    ('Very disapointed. not as descrubed at all.',0),
    ('horrible experience . never buying again.',0),
    ('Poor qquality and very late delivery.',0),
    ('Total scam. Do not but this product',0),

]

texts, labels = zip(*reviews)

vectorizer = TfidfVectorizer(ngram_range=(1,2), max_features=500) #max features save from ovwer fitting not take more work
x = vectorizer.fit_transform(texts)
y = list(labels)

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25, random_state=42)

clf = LogisticRegression()
clf.fit(x_train,y_train)
print(f'Accuracy: {accuracy_score(y_test,clf.predict(x_test))*100:.0f}%')

#Test on news reviews

new = ['This is a wonder ful product! totally worth it!',
       'Very bad experience . Quality is awful.',
       'Average product.nothing apecial.']

x_new = vectorizer.transform(new)
for review , pred, prob in zip(new, clf.predict(x_new), clf.predict_proba(x_new)):
    sentiment = 'Positive' if pred == 1 else 'Negative'
    confidence = max(prob)*100
    print(f'[{sentiment} {confidence:.0f}%] {review[:45]}...')