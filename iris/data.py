import pandas as pd
import plotly.express as px


def get_iris_data() -> pd.DataFrame:
    return px.data.iris()
