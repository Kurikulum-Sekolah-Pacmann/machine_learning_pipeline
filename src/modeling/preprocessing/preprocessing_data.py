import pandas as pd
from src.modeling.preprocessing.process.mapping_values import mapping_values_process
from src.modeling.preprocessing.process.one_hot_encoding import ohe_process
from src.modeling.preprocessing.process.mapping_month import mapping_month_process
from src.utils.helper import logging_process
import logging

logging_process()


def preprocessing_process(data: pd.DataFrame) -> pd.DataFrame:
    try:
        logging.info("===== Start Preprocessing Data =====")
        # mapping values
        data = mapping_values_process(data = data)
        
        # one hot encoding process
        data = ohe_process(data = data)
        
        # mapping month
        data = mapping_month_process(data = data)

        logging.info("===== Failed Preprocessing Data =====")
                
        return data
    
    except Exception as e:
        logging.error("===== Failed Preprocessing Data =====")
        raise Exception(e)
