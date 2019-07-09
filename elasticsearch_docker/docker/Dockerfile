FROM docker.elastic.co/elasticsearch/elasticsearch:7.1.1

RUN bin/elasticsearch-plugin install analysis-kuromoji

RUN echo "http.max_content_length: 350mb" >> config/elasticsearch.yml
RUN echo "cluster.routing.allocation.disk.threshold_enabled: false" >> config/elasticsearch.yml
RUN echo "http.cors.allow-origin: '*'" >> config/elasticsearch.yml
RUN echo "http.cors.enabled: true" >> config/elasticsearch.yml
