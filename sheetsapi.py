# https://developers.google.com/sheets/api/quickstart/python
import os

import httplib2
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'PyTSF'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        credentials = tools.run_flow(flow, store, flags)

        print('Storing credentials to ' + credential_path)
    return credentials





def _get_service():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http, discoveryServiceUrl=discoveryUrl)
    return service


def get_worksheets(spreadsheet_id):
    spreadsheet = _get_service().spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
    return spreadsheet['sheets']


def get_range_data(spreadsheet_id, range):
    return _get_service().spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range).execute()


def get_ranges_batch(spreadsheet_id, ranges):
    return (_get_service().spreadsheets().values().batchGet(spreadsheetId=spreadsheet_id, ranges=ranges).execute())['valueRanges']









def getValueRanges():
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http, discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '1jXygiAnEQ-BzK7ZMkduJMA0QETZ2_-8IE-jUQsmZ7-4'
    # result = service.spreadsheets().values().batchGet(spreadsheetId=spreadsheetId, ranges=ranges).execute()
    result = service.spreadsheets().get(spreadsheetId=spreadsheetId).execute()
    # sheets = result.get('sheets')
    print(result)
    # for sheet in sheets:
        # print(sheet['properties']['title'])

    # result = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range="marzec").execute()
    # print(result['values'])

    # valueRanges = result.get('valueRanges', [])
    # return result


