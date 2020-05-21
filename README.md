# Name

recipe.foodinc

## Description

A django based webapp for documented recipes

## Usage
After cloning, review the "requirements.sh" bash script.
After review, make any changes and run the script to automate
setup of missing packages, folders, and files.

## Google Cloud SQL - Postgres setup

0. Make sure billing is enabled for project.
1. Select GCP project to work with in cloud console.
2. In [APIs & Services], enable [Cloud SQL Admin API].

NOTE: MAKE SURE CLOUD SDK IS INSTALLED AND INITIALIZED
LINK: https://cloud.google.com/sdk/docs

3. Make sure you're logged in to gcloud on the command-line.
4. check current active gcloud configuration by running...
   [gcloud auth list]
5. To change the active account, run...
   [gcloud config set account `ACCOUNT`]
6. To change the active project, run...
   [gcloud config set project `PROJECT_ID`]
7. enable sqladmin with gcloud
   [gcloud services enable sqladmin]
8. install the Cloud SQL Proxy for in the root folder as manage.py, run...
   [ curl -o cloud_sql_proxy https://dl.google.com/cloudsql/cloud_sql_proxy.darwin.amd64 ]
9. make the proxy executable, run...
   [chmod +x cloud_sql_proxy]
10. Create a Cloud SQL for PostgreSQL instance.
    [gcloud sql instances describe [YOUR_INSTANCE_NAME]]
11. same the output from the previous step
12. start the Cloud SQL Proxy by using the [CONNECTION_NAME] from the output
  [ ./cloud_sql_proxy -instances="[YOUR_INSTANCE_CONNECTION_NAME]"=tcp:5432 ]


## Google Cloud STORAGE - Cloud storage bucket setup for static files

NOTE: MAKE SURE CLOUD SDK IS INSTALLED AND INITIALIZED
LINK: https://cloud.google.com/sdk/docs

1. Create a cloud storage bucket, run...
   [gsutil mb gs://<your-gcs-bucket-name>]
2. Make bucket publicly readable, run...
   [gsutil defacl set public-read gs://<your-gcs-bucket-name>]
3. collect static files to 'static'
4. Upload the static content to Cloud Storage, run...
   [ gsutil rsync -R static/ gs://<your-gcs-bucket-name>/static ]
5. Set the value of [STATIC_URL] is settings.py to the following URL
    [https://storage.googleapis.com/<your-gcs-bucket>/static/]  



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Credit
realpython.com
Jasmine Finer

## License
[MIT](https://choosealicense.com/licenses/mit/)
