# pandas 설치 방법 확인하기

import pandas as pd

df = pd.DataFrame({
    '합':[6],
    '평균':[3]
})

df.to_csv('.\\02_week\\1018\\csv\\output.csv', index=False)