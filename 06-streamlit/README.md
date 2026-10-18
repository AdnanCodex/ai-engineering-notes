# 📂 Datasets

The notebooks read their data from this folder using relative paths such as `../data/train.csv`.
Datasets are **not included** in the repository. Download them and place the files here.

| Notebook | Files needed |
|---|---|
| `03_Pandas/01_Pandas_DataFrames` | `ipl-matches.csv`, `batsman_runs_ipl.csv`, `movies.csv` |
| `03_Pandas/02_Pandas_Strings` | `titanic.csv` |
| `03_Pandas/03_Pandas_GroupBy` | `imdb-top-1000.csv`, `deliveries.csv` |
| `03_Pandas/04_Pandas_Merging_and_Joins` | `courses.csv`, `students.csv`, `reg-month1.csv`, `reg-month2.xlsx`, `matches.csv`, `deliveries.csv` |
| `03_Pandas/05_Pandas_MultiIndex_and_Pivot` | `expense_data.csv`, `time_series_covid19_confirmed_global.csv`, `time_series_covid19_deaths_global.csv` |
| `03_Pandas/06_Pandas_DateTime` | `titanic.csv` |
| `04_Data_Visualization/01_Matplotlib` | `batter.csv`, `batsman_season_record.csv`, `sharma-kohli.csv`, `gayle-175.csv`, `vk.csv`, `big-array.npy` |
| `05_Data_Cleaning/01_Data_Accessing_and_Cleaning` | `patients.csv`, `treatments.csv`, `treatments_cut.csv`, `adverse_reactions.csv` |
| `06_EDA/01_Titanic_EDA` | `train.csv`, `test.csv` (Kaggle Titanic) |

`01_Python`, `02_NumPy` and `04_Data_Visualization/02_Seaborn` need no external files (Seaborn loads its sample datasets by itself).

> `titanic.csv` and `train.csv` are the same passenger data under different names.
> Files created by the notebooks (`data/cleaned/`, `clinical_trials.xlsx`) are listed in `.gitignore`.
