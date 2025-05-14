import re
from datetime import datetime
reg = r"\s+(?=\d{2}(?:\d{2})?-\d{1,2}-\d{1,2}\b)"


current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")

print(current_datetime)