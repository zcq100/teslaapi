# Tesla API

    This is a package for connecting to the Tesla API.

## Usage for a vehicle
```
from teslaapi import Connect
if __name__ == '__main__':
    connect=Connect("your email","your password")
    vehicle=connect.vechels[0]
    result=vehicle.nearby_charging_sites()
    print(result)
    
```