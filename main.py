# Importar as bibliotecas necessárias
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.ml.feature import RegexTokenizer, StopWordsRemover
from pyspark.ml.classification import NaiveBayes, NaiveBayesModel
from pyspark.ml import Pipeline
from pyspark.sql.functions import col, udf
from pyspark.sql.types import StringType
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Inicializar o Spark
sc = SparkContext(appName="SentimentAnalysis")
spark = SparkSession(sc)

# Carregar os dados de tweets
data = spark.read.csv("tweets.csv", header=True, inferSchema=True)

# Pré-processamento dos dados
tokenizer = RegexTokenizer(inputCol="text", outputCol="words", pattern="\\W")
stop_words = StopWordsRemover(inputCol="words", outputCol="filtered")
pipeline = Pipeline(stages=[tokenizer, stop_words])
data = pipeline.fit(data).transform(data)

# Análise de sentimentos
sia = SentimentIntensityAnalyzer()


def sentiment_score(text):
    return sia.polarity_scores(text)["compound"]


sentiment_score_udf = udf(sentiment_score, StringType())
data = data.withColumn("sentiment_score", sentiment_score_udf(col("text")))

# Treinar um modelo de classificação de Naive Bayes
nb = NaiveBayes(smoothing=1.0, modelType="multinomial",
                labelCol="sentiment", featuresCol="filtered")
model = nb.fit(data)

# Salvar o modelo treinado
model.save("nb_model")

# Carregar o modelo treinado
model = NaiveBayesModel.load("nb_model")

# Fazer previsões em novos dados
new_data = spark.read.csv("new_tweets.csv", header=True, inferSchema=True)
new_data = pipeline.fit(new_data).transform(new_data)
predictions = model.transform(new_data)

# Exibir as previsões de sentimentos
predictions.select("text", "prediction").show()
