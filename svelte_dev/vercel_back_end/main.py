# pylint: disable=import-error
from fastapi.concurrency import run_in_threadpool
from fastapi.middleware.cors import CORSMiddleware
import sys
import threading
import pathlib
import time
import uvicorn
import asyncio
import string
import random
# from collections import Counter
from fastapi import FastAPI, BackgroundTasks
# from fastapi.staticfiles import StaticFiles
# import subprocess
here = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(here.parents[1].absolute()))
sys.path.insert(0, str(here.parents[0].absolute()))
# subprocess.run("npm start", shell=True, cwd=str(here.parents[0].absolute())+"/client")
# background_tasks = BackgroundTasks()
app = FastAPI()
print("str(here.parents[0].absolute())", str(here.parents[0].absolute()))
# client_address = str(here.parents[0].absolute()) + "/client/public/"
# client_address = "client/public/"
# origins = [
#     "https://ptc1ap.deta.dev/",
#     "http://ptc1ap.deta.dev/",
#     "http://localhost",
#     "http://localhost:8080",
#     "https://get-data-from-back-end.vercel.app/"
#     "http://get-data-from-back-end.vercel.app/"
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
session = {'last_choice': "", 'counter': 0, 'slider_choice': 'Digits',

           'value_to_send': "0", 'slider_value': 0.1, 'started': False, 'start': 0.0, 'end': 0.0}


# def back_end_data_process_init():
#     """ This initialises connection_check_loop as a background thread"""
#     x_back_end_data_process = threading.Thread(target=back_end_data_process)
#     x_back_end_data_process.start()


# class BackgroundRunner:
#     def __init__(self):
#         self.value = 0

#     async def run_main(self):
#         while True:
#             # print("starting")
#             global start
#             global end
#             start = time.time()
#             print("self.value", self.value)
#             await asyncio.sleep(float(session['slider_value']))
#             # session['value_to_send'] = "1"
#             self.value = "1"
#             print("self.value", self.value)
#             # print("starting 2")
#             await asyncio.sleep(float(session['slider_value']))
#             # session['value_to_send'] = "2"
#             self.value = "2"
#             print("self.value", self.value)
#             # print("starting 3")
#             await asyncio.sleep(float(session['slider_value']))
#             # session['value_to_send'] = "3"
#             self.value = "3"
#             print("self.value", self.value)
#             await asyncio.sleep(float(session['slider_value']))
#             # session['value_to_send'] = "4"
#             self.value = "4"
#             print("self.value", self.value)
#             await asyncio.sleep(float(session['slider_value']))
#             # session['value_to_send'] = "5"
#             self.value = "5"
#             print("self.value", self.value)
#             await asyncio.sleep(float(session['slider_value']))
#             # session['value_to_send'] = "6"
#             self.value = "6"
#             print("self.value", self.value)
#             await asyncio.sleep(float(session['slider_value']))
#             # session['value_to_send'] = "7"
#             self.value = "7"
#             print("self.value", self.value)
#             await asyncio.sleep(float(session['slider_value']))
#             # session['value_to_send'] = "8"
#             self.value = "8"
#             print("self.value", self.value)
#             await asyncio.sleep(float(session['slider_value']))
#             # session['value_to_send'] = "9"
#             self.value = "9"
#             print("self.value", self.value)
#             end = time.time()
#             # await asyncio.sleep(1)

# runner = BackgroundRunner()
# def back_end_data_process():

#     while True:
#         global start
#         global end
#         start = time.time()
#         time.sleep(session['slider_value'])
#         session['value_to_send'] = "1"
#         time.sleep(session['slider_value'])
#         session['value_to_send'] = "2"
#         time.sleep(session['slider_value'])
#         session['value_to_send'] = "3"
#         time.sleep(session['slider_value'])
#         session['value_to_send'] = "4"
#         time.sleep(session['slider_value'])
#         session['value_to_send'] = "5"
#         time.sleep(session['slider_value'])
#         session['value_to_send'] = "6"
#         time.sleep(session['slider_value'])
#         session['value_to_send'] = "7"
#         time.sleep(session['slider_value'])
#         session['value_to_send'] = "8"
#         time.sleep(session['slider_value'])
#         session['value_to_send'] = "9"
#         end = time.time()
#         # time.sleep(1)


# back_end_data_process_init()


# def back_end_data_process():
#     while True:
#         # session['started'] = True
#         # print("starting")

#         start = time.time()
#         session['start']= start
#         print("new_value", session['value_to_send'])
#         # time.sleep(float(session['slider_value']))
#         session['value_to_send'] = "1"
#         # value = "1"
#         print("new_value", session['value_to_send'])
#         # print("starting 2")
#         # time.sleep(float(session['slider_value']))
#         session['value_to_send'] = "2"
#         # value = "2"
#         print("new_value", session['value_to_send'])
#         # print("starting 3")
#         # time.sleep(float(session['slider_value']))
#         session['value_to_send'] = "3"
#         # value = "3"
#         print("new_value", session['value_to_send'])
#         # time.sleep(float(session['slider_value']))
#         session['value_to_send'] = "4"
#         # value = "4"
#         print("new_value", session['value_to_send'])
#         # time.sleep(float(session['slider_value']))
#         session['value_to_send'] = "5"
#         # value = "5"
#         print("new_value", session['value_to_send'])
#         # time.sleep(float(session['slider_value']))
#         session['value_to_send'] = "6"
#         # value = "6"
#         print("new_value", session['value_to_send'])
#         # time.sleep(float(session['slider_value']))
#         session['value_to_send'] = "7"
#         # value = "7"
#         print("new_value", session['value_to_send'])
#         # time.sleep(float(session['slider_value']))
#         session['value_to_send'] = "8"
#         # value = "8"
#         print("new_value", session['value_to_send'])
#         # time.sleep(float(session['slider_value']))
#         session['value_to_send'] = "9"
#         # value = "9"
#         print("new_value", session['value_to_send'])
#         end = time.time()
#         session['end']= end
#         session['started'] = True

# # @app.on_event('startup')
# # async def app_startup():
#     # await run_in_threadpool(lambda: back_end_data_process())

#     # asyncio.create_task(back_end_data_process())

# if not session['started']:
#     back_end_data_process_init()

@app.get("/get_value_to_send")
async def get_value_to_send():
    print("session['slider_choice']", session['slider_choice'])
    if session['slider_choice'] == "Digits":

        if session['last_choice'] == "Digits":
            print(session['counter'])
            print(string.digits)
            if session['counter'] not in range(len(string.digits)):
                session['counter'] = 0
            value_to_send = string.digits[session['counter']]
            session['counter'] += 1
        else:
            session['counter'] = 0
            value_to_send = string.digits[session['counter']]
            session['last_choice'] = "Digits"

    elif session['slider_choice'] == "Letters":

        if session['last_choice'] == "Letters":
            if session['counter'] not in range(len(string.ascii_letters)):
                session['counter'] = 0
            value_to_send = string.ascii_letters[session['counter']]
            session['counter'] += 1
        else:
            session['counter'] = 0
            value_to_send = string.ascii_letters[session['counter']]
            session['last_choice'] = "Letters"

    elif session['slider_choice'] == "Punctuation":

        if session['last_choice'] == "Punctuation":
            if session['counter'] not in range(len(string.punctuation)):
                session['counter'] = 0
            value_to_send = string.punctuation[session['counter']]
            session['counter'] += 1
        else:
            session['counter'] = 0
            value_to_send = string.punctuation[session['counter']]
            session['last_choice'] = "Punctuation"

    session['value_to_send'] = value_to_send
    print("value_to_send", session['value_to_send'])
    return {"value_to_send": session['value_to_send']}


# @app.get("/send_time_sleep_to_back_end/{slider_value}")
# async def send_time_sleep_to_back_end(slider_value):
#     session['slider_value'] = int(slider_value)/1000
#     return "slider_value received"


@app.get("/send_slider_choice_to_back_end/{slider_choice}")
async def send_slider_choice_to_back_end(slider_choice):
    if slider_choice == "Digits":

        if session['last_choice'] == "Digits":
            value_to_send = string.digits[session['counter']]
            session['counter'] += 1
        else:
            session['counter'] = 0
            value_to_send = string.digits[session['counter']]
            session['last_choice'] = "Digits"

    elif slider_choice == "Letters":

        if session['last_choice'] == "Letters":
            value_to_send = string.ascii_letters[session['counter']]
            session['counter'] += 1
        else:
            session['counter'] = 0
            value_to_send = string.ascii_letters[session['counter']]
            session['last_choice'] = "Letters"

    elif slider_choice == "Punctuation":

        if session['last_choice'] == "Punctuation":
            value_to_send = string.punctuation[session['counter']]
            session['counter'] += 1
        else:
            session['counter'] = 0
            value_to_send = string.punctuation[session['counter']]
            session['last_choice'] = "Punctuation"

    session['value_to_send'] = value_to_send
    session['slider_choice'] = slider_choice
    return "slider_choice received"


@app.get("/")
async def read_root():
    # total = session['end'] - session['start']
    # return {"Hello": "World1234",
    #         "end-start": total,
    #         "session['end'] ": session['end'],
    #         "session['start']": session['start'],

    #         "session['slider_value']": session['slider_value'],
    #         "session['value_to_send']": session['value_to_send'],
    #         "session['started']": session['started']

    #         }
    return {"Hello": "World1234"}
# @app.get("/get_value_to_send")
# async def get_value_to_send():
#     return {"value_to_send": session['value_to_send']}

# Place After All Other Routes
# app.mount('', StaticFiles(directory=client_address, html=True), name="static")
# app.mount('', StaticFiles(directory=public, html=True), name="public")

# if __name__ == "__main__":
#     back_end_data_process_init()
#     uvicorn.run(app, host="127.0.0.1", port=8000, log_level="warning")
    # uvicorn.run(app, host="ptc1ap.deta.dev", log_level="warning")

    # uvicorn.run(app, host="127.0.0.1", port=8000)

    # app.run(host='127.0.0.1', port=8000, debug=False)
