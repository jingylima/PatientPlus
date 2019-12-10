import fitbit
import gather_keys_oauth2 as Oauth2
import pandas as pd 
import datetime
import matplotlib.pyplot as plt
import send_sms

CLIENT_ID = '22B5HP'
CLIENT_SECRET = 'ab8e456b16023674bb774354c780fc60'

server = Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
server.browser_authorize()

ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])

auth2_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)

yesterday = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y%m%d"))
yesterday2 = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
today = str(datetime.datetime.now().strftime("%Y%m%d"))

fit_statsHR = auth2_client.intraday_time_series('activities/heart', base_date=yesterday2, detail_level='1sec')

time_list = []
val_list = []

for i in fit_statsHR['activities-heart-intraday']['dataset']:
  val_list.append(i['value'])
  time_list.append(i['time'])
  
heartdf = pd.DataFrame({'Heart Rate':val_list,'Time':time_list})

texting()
'''
val_list = val_list[-30:]
time_list = time_list[-30:]  
  


heartdf.plot(kind = 'line', x = 'Time', y = 'Heart Rate')

plt.show()
'''
heartdf.to_csv('/Users/jingy/Downloads/python-fitbit-master/Heart/heart'+ \
               yesterday+'.csv', \
               columns=['Time','Heart Rate'], header=True, \
               index = False)
fit_statsSl = auth2_client.sleep(date='today')
stime_list = []
sval_list = []
for i in fit_statsSl['sleep'][0]['minuteData']:
    stime_list.append(i['dateTime'])
    sval_list.append(i['value'])
    
sleepdf = pd.DataFrame({'State':sval_list,'Time':stime_list})