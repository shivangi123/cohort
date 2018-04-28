import json
from google.cloud import bigquery




class CohortAnalysis():
    def __init__(self):
        pass
    def readconf(self, config_file):
        pass

    def cohort(self, cohort_duration, config, query):
        conf = self.readconf(config)
        job_config = bigquery.QueryJobConfig()
        job_config.destination = conf.dest
        conf = self.readconf(config)
        client = bigquery.Client(conf.project_id)
        job =  client.query(query=query, job_config= job_config)
        job.result()










