Hello friends,

I've added some subcommands to aid in exploring files. By default both commands load only the first 20,000 rows of data, if possible. Some formats like Parquet don't allow that. 

The reports that it generates are markdown. If anyone has any other ideas for other statistics to include please open a [request](https://github.com/chapmanjacobd/library/issues/new?assignees=&labels=&projects=&template=feature_request.md&title=).

    pip install xklb pandas 

If you want to load data from AWS S3 you also need `s3fs`

If you want to load data from GCP GCS you also need `gcsfs`

Here is an example of the new eda command with a random CSV I found:

    $ library eda https://www.stats.govt.nz/assets/Uploads/Business-operations-survey/Business-operations-survey-2022/Download-data/business-operations-survey-2022-business-finance.csv
    
    ## https://www.stats.govt.nz/assets/Uploads/Business-operations-survey/Business-operations-survey-2022/Download-data/business-operations-survey-2022-business-finance.csv:0
    ### Shape

    (6627, 6) 

    ### Sample of rows

    |      | description                                                            | industry                   |   level | size   | line_code   |   value |
    |------|------------------------------------------------------------------------|----------------------------|---------|--------|-------------|---------|
    |    0 | Type of outstanding debt: bank overdrafts                              | total                      |       0 | 619 employees        | D0201       |   13215 |
    |    1 | Type of outstanding debt: bank overdrafts                              | total                      |       0 | 2049 employees        | D0201       |    3405 |
    |    2 | Type of outstanding debt: bank overdrafts                              | total                      |       0 | 5099 employees        | D0201       |     978 |
    | 6624 | Number of years business is dealing with main bank: more than 10 years | Arts & recreation services |       1 | total  | D2100.04    |     264 |
    | 6625 | Number of years business is dealing with main bank: more than 10 years | Other services             |       1 | total  | D2100.04    |     936 |
    | 6626 | Number of years business is dealing with main bank: more than 10 years | total                      |       0 | total  | D2100.04    |   24012 |

    ### Summary statistics

    |       |       level |     value |
    |-------|-------------|-----------|
    | count | 6627        |  6627     |
    | mean  |    1.40426  |   421.938 |
    | std   |    0.673548 |  2071.7   |
    | min   |    0        |     0     |
    | 25%   |    1        |     3     |
    | 50%   |    2        |    27     |
    | 75%   |    2        |   153     |
    | max   |    2        | 42840     |

    ### Pandas columns with 'converted' dtypes

    | column      | original_dtype   | converted_dtype   |
    |-------------|------------------|-------------------|
    | description | object           | string            |
    | industry    | object           | string            |
    | level       | int64            | Int64             |
    | size        | object           | string            |
    | line_code   | object           | string            |
    | value       | int64            | Int64             |

    ### Numerical columns

    #### Bins

    | level           |   count |
    |-----------------|---------|
    | (-0.002, 0.333] |     705 |
    | (0.333, 0.667]  |       0 |
    | (0.667, 1.0]    |    2538 |
    | (1.0, 1.333]    |       0 |
    | (1.333, 1.667]  |       0 |
    | (1.667, 2.0]    |    3384 |

    | value              |   count |
    |--------------------|---------|
    | (-42.84, 7140.0]   |    6565 |
    | (7140.0, 14280.0]  |      27 |
    | (14280.0, 21420.0] |      15 |
    | (21420.0, 28560.0] |      11 |
    | (28560.0, 35700.0] |       5 |
    | (35700.0, 42840.0] |       4 |

    ### Missing values

    0 nulls/NaNs (0.0% dataset values missing)

If there are missing values in the data the command will output some info about that. 

Here is a file from S3 to illustrate that:

    $ library eda s3://aws-roda-ml-datalake/yt8m/vocabulary.csv

    ## s3://aws-roda-ml-datalake/yt8m/vocabulary.csv:0
    ### Shape

    (3862, 9) 

    ### Sample of rows

    |      |   Index |   TrainVideoCount | KnowledgeGraphId   | Name             | WikiUrl                                        | Vertical1             |   Vertical2 |   Vertical3 | WikiDescription                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
    |------|---------|-------------------|--------------------|------------------|------------------------------------------------|-----------------------|-------------|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    |    0 |       0 |            788288 | /m/03bt1gh         | Game             | https://en.wikipedia.org/wiki/Game             | Games                 |         nan |         nan | A game is structured form of play, usually undertaken for enjoyment and sometimes used as an educational tool. Games are distinct from work, which is usually carried out for remuneration, and from art, which is more often an expression of aesthetic or ideological elements. However, the distinction is not clear-cut, and many games are also considered to be work or art. Key components of games are goals, rules, challenge, and interaction. Games generally involve mental or physical stimulation, and often both. Many games help develop practical skills, serve as a form of exercise, or otherwise perform an educational, simulational, or psychological role. Attested as early as 2600 BC, games are a universal part of human experience and present in all cultures. The Royal Game of Ur, Senet, and Mancala are some of the oldest known games.                                                                                                                                                                                                                                                                                                                                                |
    |    1 |       1 |            539945 | /m/01mw1           | Video game       | https://en.wikipedia.org/wiki/Video_game       | Games                 |         nan |         nan | A video game is an electronic game that involves human or animal interaction with a user interface to generate visual feedback on a video device such as a TV screen or computer monitor. The word video in video game traditionally referred to a raster display device, but as of the 2000s, it implies any type of display device that can produce two- or three-dimensional images. Some theorists categorize video games as an art form, but this designation is controversial. The electronic systems used to play video games are known as platforms; examples of these are personal computers and video game consoles. These platforms range from large mainframe computers to small handheld computing devices. Specialized video games such as arcade games, in which the video game components are housed in a large, coin-operated chassis, while common in the 1980s in video arcades, have gradually declined in use due to the widespread availability of affordable home video game consoles and video games on desktop and laptop computers and smartphones. The input device used for games, the game controller, varies across platforms.                                                            |
    |    2 |       2 |            415890 | /m/07yv9           | Vehicle          | https://en.wikipedia.org/wiki/Vehicle          | Autos & Vehicles      |         nan |         nan | A vehicle is a mobile machine that transports people or cargo. Typical vehicles include wagons, bicycles, motor vehicles, railed vehicles, watercraft, aircraft and spacecraft. Land vehicles are classified broadly by what is used to apply steering and drive forces against the ground: wheeled, tracked, railed or skied. ISO 3833-1977 is the standard, also internationally used in legislation, for road vehicles types, terms and definitions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
    | 3859 |    3824 |               130 | /m/01hbjs          | Look-alike       | https://en.wikipedia.org/wiki/Look-alike       | (Unknown)             |         nan |         nan | A look-alike, or double, is a person who closely resembles another person.  In popular Western culture, a look-alike is a person who bears a close physical resemblance to a celebrity, politician, or member of royalty. Many look-alikes earn a living by making guest appearances at public events or by performing on television or film, playing the person they resemble. A large variety of celebrity look-alike images can be found throughout the web, including images placed by professional agencies that offer their services. Look-alikes have also figured prominently, at least since the 19th century, in literature; and since the 20th century, in films and television programs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
    | 3860 |    3844 |               127 | /m/01vzvy          | Mortar (masonry) | https://en.wikipedia.org/wiki/Mortar_(masonry) | Business & Industrial |         nan |         nan | Mortar is a workable paste used to bind building blocks such as stones, bricks, and concrete masonry units together, fill and seal the irregular gaps between them, and sometimes add decorative colors or patterns in masonry walls. In its broadest sense mortar includes pitch, asphalt, and soft mud or clay, such as used between mud bricks. Mortar comes from Latin mortarium meaning crushed. Cement mortar becomes hard when it cures, resulting in a rigid aggregate structure; however the mortar is intended to be weaker than the building blocks and the sacrificial element in the masonry, because the mortar is easier and less expensive to repair than the building blocks. Mortars are typically made from a mixture of sand, a binder, and water. The most common binder since the early 20th century is Portland cement but the ancient binder lime mortar is still used in some new construction. Lime and gypsum in the form of plaster of Paris are used particularly in the repair and repointing of buildings and structures because it is important the repair materials are similar to the original materials: The type and ratio of the repair mortar is determined by a mortar analysis. |
    | 3861 |    3812 |               123 | /m/03h_4m          | Cylinder         | https://en.wikipedia.org/wiki/Cylinder         | Science               |         nan |         nan | In its simplest form, a cylinder is the surface formed by the points at a fixed distance from a given straight line called the axis of the cylinder. It is one of the most basic curvilinear geometric shapes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

    ### Summary statistics

    |       |   Index |   TrainVideoCount |
    |-------|---------|-------------------|
    | count | 3862    |           3862    |
    | mean  | 1930.5  |           3032.53 |
    | std   | 1115.01 |          21182    |
    | min   |    0    |            123    |
    | 25%   |  965.25 |            234    |
    | 50%   | 1930.5  |            440.5  |
    | 75%   | 2895.75 |           1199.75 |
    | max   | 3861    |         788288    |

    ### Pandas columns with 'converted' dtypes

    | column           | original_dtype   | converted_dtype   |
    |------------------|------------------|-------------------|
    | Index            | int64            | Int64             |
    | TrainVideoCount  | int64            | Int64             |
    | KnowledgeGraphId | object           | string            |
    | Name             | object           | string            |
    | WikiUrl          | object           | string            |
    | Vertical1        | object           | string            |
    | Vertical2        | object           | string            |
    | Vertical3        | object           | string            |
    | WikiDescription  | object           | string            |

    ### Numerical columns

    #### Bins

    | TrainVideoCount          |   count |
    |--------------------------|---------|
    | (-665.165, 131483.833]   |    3850 |
    | (131483.833, 262844.667] |       7 |
    | (262844.667, 394205.5]   |       2 |
    | (394205.5, 525566.333]   |       1 |
    | (525566.333, 656927.167] |       1 |
    | (656927.167, 788288.0]   |       1 |

    ### Missing values

    7,276 nulls/NaNs (20.9% dataset values missing)

    #### 4 columns with no missing values

    - Index
    - TrainVideoCount
    - KnowledgeGraphId
    - Vertical1

    #### Value stats
    | column           | values        | null         | zero     | empty_string   |
    |------------------|---------------|--------------|----------|----------------|
    | TrainVideoCount  | 3862 (100.0%) | 0 (0.0%)     | 0 (0.0%) | 0 (0.0%)       |
    | KnowledgeGraphId | 3862 (100.0%) | 0 (0.0%)     | 0 (0.0%) | 0 (0.0%)       |
    | Vertical1        | 3862 (100.0%) | 0 (0.0%)     | 0 (0.0%) | 0 (0.0%)       |
    | Name             | 3806 (98.5%)  | 56 (1.5%)    | 0 (0.0%) | 0 (0.0%)       |
    | WikiUrl          | 3806 (98.5%)  | 56 (1.5%)    | 0 (0.0%) | 0 (0.0%)       |
    | WikiDescription  | 3806 (98.5%)  | 56 (1.5%)    | 0 (0.0%) | 0 (0.0%)       |
    | Vertical2        | 584 (15.1%)   | 3278 (84.9%) | 0 (0.0%) | 0 (0.0%)       |
    | Vertical3        | 32 (0.8%)     | 3830 (99.2%) | 0 (0.0%) | 0 (0.0%)       |
    | Index            | 3861 (100.0%) | 0 (0.0%)     | 1 (0.0%) | 0 (0.0%)       |

It works on local files too but that is probably more boring
