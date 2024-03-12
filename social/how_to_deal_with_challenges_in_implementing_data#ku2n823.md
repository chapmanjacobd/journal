If the data isn't in a consistent format then every downstream consumer needs to be an expert on the data.

The role of a data engineer is key here. Do your best to talk with stakeholders and write up a data contract. 

- Ideally, data can be concatenated where old rows have null values for new columns. 
- Less ideally, old data can be modified where you would talk with subject matter experts to do your best at combining different datasets so that 1) not everyone needs to be an expert on a specific column value and how it changes over time (with regard to sensor errors, or data type changes, etc) so that they can focus on the actual value change (linear regression, forecasting, etc) and 2) if data *can* be combined someone with less time to investigate the data *will* certainly and blindly concat the datasets without realizing that values need to be adjusted before analysis and so their results and other downstream results will diverge from reality by varying degrees.
- In the worst case where data cannot be combined, even if the schema is the same, they should probably be published as different data products. There should be documentation at a very high level instructing people not to combine the different products rather than having breaking changes buried deep within some Sentinel-2 processing baseline PDF page 113 sub-paragraph C...
