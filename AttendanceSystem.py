'''
This is Basic Attendance System using bluetooth, it read all connected devices and insert into excel,
this will not work in speaker, wireless microphone , only on laptop Cellphone
Ito ay isang Blueprint para sa near Future Project, may mga lack of features at functionality pa ito.
'''
import asyncio
import pandas as pd
from bleak import BleakScanner
import os

async def get_all_student_devices():
    #Read all Connected Devices
    devices = await BleakScanner.discover()
    device_names = [d.name for d in devices]
    dev = {"Name":device_names}
    data = pd.DataFrame(dev)
    
    #Insert in Excel
    data.to_excel("StudentDeviceAttendance.xlsx",index=False)
  
    #Updated the Excel
    output_file = "StudentDeviceAttendance.xlsx"
    if os.path.exists(output_file):
     os.remove(output_file)

    data.to_excel(output_file, index=False)
    
    #Read Excel
    data = pd.read_excel("StudentDeviceAttendance.xlsx")
    print(data.head())

asyncio.run(get_all_student_devices())#Invoke get_all_student_devices() function