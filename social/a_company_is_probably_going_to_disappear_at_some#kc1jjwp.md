Here is a export of the database: 

- CSV https://archive.org/download/atlasobscura/atlasobscura.csv

- SQLite https://archive.org/download/atlasobscura/atlasobscura.db

I've packaged all ~27,000 up into a FlatGeobuf, which is an efficient format to use with QGIS. You can use `ogr2ogr` to convert to other spatial formats.

- FlatGeobuf https://archive.org/download/atlasobscura/atlasobscura.fgb

Python script to merge the JSON files into a SQLite database: https://github.com/chapmanjacobd/computer/blob/main/bin/atlas_obscura_map.py

    $ lb eda atlasobscura.db --end-row inf

## atlasobscura.db:media
### Shape

(26479, 16) 

### Sample of rows

|       |    id | title                                | subtitle                                                                                                   | city      | country        | location            | url                                                              | hide_from_maps   | physical_status   | thumbnail_url                                                                                                                                                                                                                                                                                                                                                             | thumbnail_url_3x2                                                                                                                                                                                                                                                                                                                                                         |   coordinates_lat |   coordinates_lng |   distance | content_location_title   | thing_type   |
|-------|-------|--------------------------------------|------------------------------------------------------------------------------------------------------------|-----------|----------------|---------------------|------------------------------------------------------------------|------------------|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|-------------------|------------|--------------------------|--------------|
|     0 |  1406 | Pritzker Military Museum & Library   | A military museum and library dedicated to the citizen soldier.                                            | Chicago   | United States  | Chicago, Illinois   | https://www.atlasobscura.com/places/pritzker-military-library    |                  |                   | https://img.atlasobscura.com/mLrXo0RGi-zPDb51s8GSPwCBuS73M8uNPL3JqueFQpQ/rs:fill:200:200:1/g:ce/q:81/sm:1/scp:1/ar:1/aHR0cHM6Ly9hdGxh/cy1kZXYuczMuYW1h/em9uYXdzLmNvbS91/cGxvYWRzL3BsYWNl/X2ltYWdlcy9TbmFw/c2hvdC0yMDA3LTA1/LTMxLTIxLTA1LTA4/LTc1NDA0NS5qcGc.jpg                                                                                                           |                                                                                                                                                                                                                                                                                                                                                                           |           41.8806 |        -87.6247   |   0.243872 |                          |              |
|     1 | 52369 | Finca La Luisa                       | Visit the ruins of a magnificent mansion confiscated by Fidel Castro.                                      | Havana    | Cuba           | Havana, Cuba        | https://www.atlasobscura.com/places/finca-la-luisa               |                  |                   | https://img.atlasobscura.com/k_PTM9PMXiG2wB7VUhPMrR_Lx8nts4BV9oiAA6rjqjE/rs:fill:200:200:1/g:ce/q:81/sm:1/scp:1/ar:1/aHR0cHM6Ly9hdGxh/cy1kZXYuczMuYW1h/em9uYXdzLmNvbS9h/cHBfdXBsb2Fkcy9w/bGFjZV9pbWFnZXMv/dXNlcl8zNDc0NTM2/X2Q0OTdiODA5LTM5/ZGYtNGFkMi1iNTNj/LWVmYWQxOTY0ODU3/MA.jpg                                                                                      |                                                                                                                                                                                                                                                                                                                                                                           |           23.036  |        -82.3764   |   9.11713  |                          |              |
| 26478 | 54099 | Le Gouffre de Padirac (Padirac Cave) | This impressive chasm is one of the longest natural underground cavities in the world.                     | Padirac   | France         | Padirac, France     | https://www.atlasobscura.com/places/le-gouffre-de-padirac-france | false            |                   | https://img.atlasobscura.com/VT3bsmi4NX6gJcMg9hes6BavsyTiHnVc6EuY-J_mIVc/rs:fill:200:200:1/g:ce/q:81/sm:1/scp:1/ar:1/aHR0cHM6Ly9hdGxh/cy1kZXYuczMuYW1h/em9uYXdzLmNvbS91/cGxvYWRzL3BsYWNl/X2ltYWdlcy8yMGRk/MDc2Mi1kY2I0LTRl/YzAtYWM3ZS0xNjQy/YmRmYTZkZjc0MjI0/MjRiMjI3NTk3Mzk5/MGRfR291ZmZyZV9k/ZV9QYWRpcmFjLmpw/Zw.jpg                                                    | https://img.atlasobscura.com/OA3vAcWmQ3qSh4RNKM4x7HWbzDjzQ72drHvHaCGRjBg/rs:fill:204:136:1/g:ce/q:81/sm:1/scp:1/ar:1/aHR0cHM6Ly9hdGxh/cy1kZXYuczMuYW1h/em9uYXdzLmNvbS91/cGxvYWRzL3BsYWNl/X2ltYWdlcy8yMGRk/MDc2Mi1kY2I0LTRl/YzAtYWM3ZS0xNjQy/YmRmYTZkZjc0MjI0/MjRiMjI3NTk3Mzk5/MGRfR291ZmZyZV9k/ZV9QYWRpcmFjLmpw/Zw.jpg                                                    |           44.8553 |          1.75034  |  21.4427   |                          |              |

#### Value stats

| column                 | values         | null          | zero      | empty_string   |
|------------------------|----------------|---------------|-----------|----------------|
| id                     | 26479 (100.0%) | 0 (0.0%)      | 0 (0.0%)  | 0 (0.0%)       |
| title                  | 26479 (100.0%) | 0 (0.0%)      | 0 (0.0%)  | 0 (0.0%)       |
| subtitle               | 26479 (100.0%) | 0 (0.0%)      | 0 (0.0%)  | 0 (0.0%)       |
| url                    | 26479 (100.0%) | 0 (0.0%)      | 0 (0.0%)  | 0 (0.0%)       |
| thumbnail_url          | 26479 (100.0%) | 0 (0.0%)      | 0 (0.0%)  | 0 (0.0%)       |
| thumbnail_url_3x2      | 6045 (22.8%)   | 20434 (77.2%) | 0 (0.0%)  | 0 (0.0%)       |
| hide_from_maps         | 4924 (18.6%)   | 21555 (81.4%) | 0 (0.0%)  | 0 (0.0%)       |
| content_location_title | 664 (2.5%)     | 25815 (97.5%) | 0 (0.0%)  | 0 (0.0%)       |
| thing_type             | 664 (2.5%)     | 25815 (97.5%) | 0 (0.0%)  | 0 (0.0%)       |
| coordinates_lat        | 26476 (100.0%) | 0 (0.0%)      | 3 (0.0%)  | 0 (0.0%)       |
| coordinates_lng        | 26476 (100.0%) | 0 (0.0%)      | 3 (0.0%)  | 0 (0.0%)       |
| distance               | 20441 (77.2%)  | 5974 (22.6%)  | 64 (0.2%) | 0 (0.0%)       |
| location               | 26476 (100.0%) | 0 (0.0%)      | 0 (0.0%)  | 3 (0.0%)       |
| country                | 26472 (100.0%) | 0 (0.0%)      | 0 (0.0%)  | 7 (0.0%)       |
| city                   | 25859 (97.7%)  | 90 (0.3%)     | 0 (0.0%)  | 530 (2.0%)     |
| physical_status        | 993 (3.8%)     | 15 (0.1%)     | 0 (0.0%)  | 25471 (96.2%)  |
