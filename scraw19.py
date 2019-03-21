import numpy as np
import pandas as pd
from datetime import datetime 

start = datetime.now()
end = datetime(2019,6,1)

interval = end - start
days = interval.days
print(days)
