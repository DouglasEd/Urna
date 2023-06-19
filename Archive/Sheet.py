from __future__ import print_function

import pandas as pd
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

SAMPLE_SPREADSHEET_ID = '1ybaiXajW3kYt9tsB_FJV78aiGQiIrhxh-hqOXjYz6Pc'
SRL = 'Log!A:B'
SRM = 'RA!A1:B315'

def EnviarVoto(mat,voto):
    #Offline
    f = open('LOG.txt', 'r')
    cont = f.readlines()
    cont.append(f'{mat} {voto}\n')
    f = open('LOG.txt', 'w')
    f.writelines(cont)
    f.close
    #Online
    creds = None
    try:
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
    
        service = build('sheets', 'v4', credentials=creds)

        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                      range=SRL).execute()
        values = result.get('values', [])
        valor= [[mat,voto]]
        sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,range=f"log!A{len(values)+1}",valueInputOption="USER_ENTERED" , body= {'values': valor}).execute()
    except:
        e=open('Erros.txt', 'r')
        tex= e.readlines()
        tex.append(f'{mat} {voto}')
        e=open('Erros.txt', 'w')
        e.writelines(tex)
        e.close

def AcessarMats(mat):
    Validade = False
    Nome=""
    df = pd.read_excel("RA.xlsx")
    for i in range(0,315):
        if str(df.loc[i,'Matricula']) == mat:
            Nome=df.loc[i,'Nome']
            Validade = True
    return [Validade,Nome]


def VerVotAnt(mat):
    Validade = False
    # creds= None
    # if os.path.exists('token.json'):
    #     creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # if not creds or not creds.valid:
    #     if creds and creds.expired and creds.refresh_token:
    #         creds.refresh(Request())
    #     else:
    #         flow = InstalledAppFlow.from_client_secrets_file(
    #             'credentials.json', SCOPES)
    #         creds = flow.run_local_server(port=0)
    #     with open('token.json', 'w') as token:
    #         token.write(creds.to_json())
    # try:
    #     service = build('sheets', 'v4', credentials=creds)

    #     sheet = service.spreadsheets()
    #     result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
    #                                   range='Log!B2:B316').execute()
    #     values = result.get('values', [])
    #     for i in values:
    #         if i[0] == mat:
    #             Validade = True
    # print(err)
    txt=open('LOG.txt','r')
    log=txt.read()
    txt.close()
    if mat in log:
        Validade = True
    return Validade
