lab06.ipynb's fetch cell was already removed earlier this session (it now
reads directly from `data/raw/`, no live pull) -- this folder is pruned to only
the files it actually reads. The `path/to/your/file.parquet` reference in the
notebook is a placeholder in prose text, not a real file. (`lab06.ipynb`
itself is demoted to optional/alternate material as of 2026-07-20 --
`geopandas_recap.ipynb` below is the actual Week 7 lab pick.)

`geopandas_recap.ipynb` (Week 7's actual "GeoPandas Recap" lab, adapted from
PS Lab 6) needs three files here, moved from `labs/w08/data/raw/` on 2026-07-20
once a folder-rename put this notebook in the wrong week's folder:
- `Land_Boundary_20251008.geojson` -- Berkeley jurisdictional boundary
- `tl_2023_06_tract.zip` -- Census TIGER/Line California tract geometries (32.5MB,
  cached locally instead of a live 32MB fetch from census.gov on every run; same
  file also cached in `labs/w06/data/raw/` for `seaborn_plotting.ipynb`)
- `alameda_tracts23.csv` -- pre-fetched Census ACS data (population + median household
  income per tract), same shape as the notebook's live Census API pull. Kept as a
  documented fallback per the notebook's own guidance ("If the Census API is not
  working..."), not the primary read path -- the live API call stays the default so
  students still practice using it.
