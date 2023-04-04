import pandas as pd

df = pd.DataFrame(
    {
        'coll': range(10),
        'coll': range(10,20)
    },
    index = list('acgfhibdje')
)

print(df)

import pandas as pd

df = pd.DataFrame(
    {
        'coll': range(10),
        'coll': range(10,20)
    },
    index = list('acgfhibdje')
)

result = df.loc

print(df)

import pandas as pd

df = pd.DataFrame(
    {
        'col1': range(0, 20),
        'col2': range(20, 40),
        'col3': range(40, 60)
    }
)
rows = list(range(0, len(df), 2))

result = df.iloc[rows,[1]]

print(result)




