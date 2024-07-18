class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///your_database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    S3_BUCKET = 'generative-drive'
    S3_REGION = 'ap-south-2'
    S3_CLIENT = {
        'access_key': 'AKIAQRXHCGVRPFHDJ7NP',
        'secret_key': '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',
        'region': 'ap-south-2'
    }
    GENAI_API_KEY = 'AIzaSyCF8LRXPCW6HnNqSMdut-PQqek4nruTpvE'
