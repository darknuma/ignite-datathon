# ignite-datathon

... a work in progress

## To work on this Repo (For Collaborators):

- Fork the repo, and do git clone (url)
- Create your own branch.
- Don't Merge any Pull request until collaborators sign off with `"Lgtm: Looks good to me"`

## Requirements

- Make sure you have docker installed and running
  
## How to run this project

```sh
cd ignition-datathon
Run virtualenv venv
pip install -r requirements.txt
docker-compose up --build
dbt init #for the project transformation
dbt debug
dbt run # models
```

## Project Structure

- data_assets
  - csv_files
  - transfom_assets: here we transform csv_files such as `student_data.csv`, `student_classes.csv`, `wassce_results.csv` and `student_info.csv`
- ingestion 
  - init.sql:  docker would run this file
- school_data_warehouse
