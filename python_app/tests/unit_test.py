import pytest
from freezegun import freeze_time
import pytz
from datetime import datetime, timezone
import random

MOSCOW_TIMEZONE = pytz.timezone('Europe/Moscow')

def generate_random_time():
    # datetime(year, month, day, hour, minute, second, microsecond)
    return  datetime(
            random.randint(1900,2021), 
            random.randint(1,12), 
            random.randint(1,28), 
            random.randint(0,23), 
            random.randint(0,59), 
            random.randint(0,59)).replace(tzinfo=timezone.utc).astimezone(tz=MOSCOW_TIMEZONE)

@pytest.mark.parametrize("frozen_time",
                         [generate_random_time() for i in range(5)])
                         
def test_time(client, frozen_time):
    with freeze_time(frozen_time):
        response = client.get('/')
        assert response.status_code == 200
        assert frozen_time.strftime("%H:%M:%S") in response.data.decode()
        assert frozen_time.strftime("%d-%m-%Y") in response.data.decode()
        
    
    