from models import User, load_users, save_user 
from api import fetch_uss_data, save_iss_data, iss_location

if __name__ == '__main__':
  new_user = User(username='Markus', password='password')
  save_user(new_user)
  print(load_users())

  iss_data = fetch_uss_data()
  save_iss_data(iss_data)
  print('ISS-data saved')

  iss_location()