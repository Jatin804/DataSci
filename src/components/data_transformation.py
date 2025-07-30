# to transform data ie cleaning, handling etc

import sys
import os
from dataclasses import dataclass

import pandas as pd
import numpy as np
from pandas.io.xml import preprocess_data
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline

from src.exception import Custom__exception
from src.logger import logging
from src.utils import save_obj


@dataclass
class DataTransFConfig:
    preprocessor_ob_file_path = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransFConfig()

    # data transformation function !
    def get_transformer_ob(self):
        try:
            numerical_col = ['reading_score', 'writing_score']
            categorical_col = ['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']


            # handling num data
            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler())
                ]
            )

            # Handling cat data
            cat_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("onehot", OneHotEncoder()),
                    ("scaler", StandardScaler(with_mean=False)),
                ]
            )

            logging.info(f"Categorical columns {categorical_col} ")
            logging.info(f"Numerical columns {numerical_col}")


            # pipelining both num and cat data
            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, numerical_col),
                    ("cat_pipeline", cat_pipeline, categorical_col),
                ]
            )

            logging.info("Columns transformed completed")

            return preprocessor


        except Exception as e:
            raise Custom__exception(e, sys)


    def initiate_data_transform(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")

            preprocessing_obj = self.get_transformer_ob()

            target_column_name = "math_score"
            numerical_columns = ["writing_score", "reading_score"]

            input_feature_train_df = train_df.drop(columns=[target_column_name], axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=[target_column_name], axis=1)
            target_feature_test_df = test_df[target_column_name]

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            save_obj(

                file_path=self.data_transformation_config.preprocessor_ob_file_path,
                obj=preprocessing_obj

            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_ob_file_path,
            )
        except Exception as e:
            raise Custom__exception(e, sys)