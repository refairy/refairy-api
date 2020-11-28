FROM python:3.8
COPY . /app
WORKDIR /app/refairy_api
RUN git clone git://github.com/refairy/textAnalyzer.git
WORKDIR /app

RUN pip install -r requirements.txt --no-cache-dir
RUN pip install -r refairy_api/textAnalyzer/requirements.txt --no-cache-dir
RUN python -m spacy download en
RUN python -m spacy download en_core_web_md
RUN python -m nltk.downloader averaged_perceptron_tagger

CMD python -m refairy_api
