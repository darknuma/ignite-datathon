# ignite-datathon

## About this Project

DataFestAfrica Hackathon 2024: Improving  Academic Outcome For Secondary Education, Team Ignite uses data generation method to model Federal Government Unity Schools for data, and we utilise
some core data about student history of results and current results, student bios, class bios, the school former's historical results for wassce and jamb.

- Data Engineering: Use of **PostgreSQL** for the database warehouse, going forward data is collected from the schools and ingested to PostgreSQL database.
- Data Analytics: Use of **PowerBI** to generate insights
- Data Science Prediction: ...

## To work on this Repo (For Collaborators)

- Fork the repo, and do `git clone (url)`
- Create your own branch.
- Don't merge to main for your Pull request until collaborators sign off with `"Lgtm: Looks good to me"`

## Requirements

- Make sure you have docker installed and running
  
## How to run this project

```sh
cd ignition-datathon
virtualenv venv
pip install -r requirements.txt
docker-compose up --build
dbt init # for the project transformation
dbt debug #  test connections have passed
dbt run # models
```

## Project Structure

- data_assets
  - csv_files
  - transform_assets: here we transform csv_files such as `student_data.csv`, `student_classes.csv`, `wassce_results.csv` and `student_info.csv`
- ingestion  
  - init.sql:  docker would run this file
- school_data_warehouse: run dbt models for transformation for student_results.sql  
