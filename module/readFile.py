import pandas as pd
import featuretools as ft

df = pd.read_csv("../data/test.csv")
print(df.head(5))
es = ft.EntitySet(id = "test")
es = es.entity_from_dataframe(entity_id="test",
                              dataframe=df,
                              index="Id"
                              )
print(es)
