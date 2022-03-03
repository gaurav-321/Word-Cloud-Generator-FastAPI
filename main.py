import base64
import json
import os
import random
import re
import jieba.posseg as pseg
import jieba
import uvicorn
from fastapi import FastAPI, Request, Body
from fastapi.middleware.cors import CORSMiddleware
from word_gen import create_word_cloud

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/cloud")
async def read_user_me(request: Request):
    params = await request.json()
    filename = os.path.join("output", str(random.randint(1, 10000000000000000)) + ".png")
    create_word_cloud(params['query'], filename)
    encoded = base64.b64encode(open(filename, "rb").read())
    return encoded


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=80)
