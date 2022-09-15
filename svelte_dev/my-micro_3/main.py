# pylint: disable=import-error
import sys
import threading
import pathlib
import time
import uvicorn
from fastapi import FastAPI
# from fastapi.staticfiles import StaticFiles
# import subprocess
here = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(here.parents[1].absolute()))
sys.path.insert(0, str(here.parents[0].absolute()))
# subprocess.run("npm start", shell=True, cwd=str(here.parents[0].absolute())+"/client")
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
print("str(here.parents[0].absolute())", str(here.parents[0].absolute()))
# client_address = str(here.parents[0].absolute()) + "/client/public/"
# client_address = "./svelte_dev/client/public/" 
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
session = {'value_to_send': '0', 'slider_value': 0.1}


def back_end_data_process_init():
    """ This initialises connection_check_loop as a background thread"""
    x_back_end_data_process = threading.Thread(target=back_end_data_process)
    x_back_end_data_process.start()


def back_end_data_process():

    while True:
        time.sleep(session['slider_value'])
        session['value_to_send'] = "1"
        time.sleep(session['slider_value'])
        session['value_to_send'] = "2"
        time.sleep(session['slider_value'])
        session['value_to_send'] = "3"
        time.sleep(session['slider_value'])
        session['value_to_send'] = "4"
        time.sleep(session['slider_value'])
        session['value_to_send'] = "5"
        time.sleep(session['slider_value'])
        session['value_to_send'] = "6"
        time.sleep(session['slider_value'])
        session['value_to_send'] = "7"
        time.sleep(session['slider_value'])
        session['value_to_send'] = "8"
        time.sleep(session['slider_value'])
        session['value_to_send'] = "9"


back_end_data_process_init()


@app.get("/get_value_to_send")
async def get_value_to_send():
    print("value_to_send", session['value_to_send'])
    return {"value_to_send": session['value_to_send']}


@app.get("/send_time_sleep_to_back_end/{slider_value}")
async def send_time_sleep_to_back_end(slider_value):
    session['slider_value'] = int(slider_value)/1000
    return "slider_value received"

@app.get("/")
async def read_root():
    return {"Hello": "World1234"}

# @app.get("/get_value_to_send")
# async def get_value_to_send():
#     return {"value_to_send": session['value_to_send']}

# Place After All Other Routes
# app.mount('', StaticFiles(directory=client_address, html=True), name="static")
# app.mount('', StaticFiles(directory=public, html=True), name="public")

if __name__ == "__main__":
    uvicorn.run(app, workers=4, host="127.0.0.1", port=8000, log_level="warning")
    # uvicorn.run(app, host="ptc1ap.deta.dev", log_level="warning")

    # uvicorn.run(app, host="127.0.0.1", port=8000)

    # app.run(host='127.0.0.1', port=8000, debug=False)
