`cut` requires numeric data. It sounds like your column might be a factor or string. Maybe you can try this:

    Celiac_Disease_data_age1$diagnosis_age <- as.numeric(as.character(Celiac_Disease_data_age1$diagnosis_age))
