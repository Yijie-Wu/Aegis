# -*- encoding:utf-8 -*-
"""
Author: Yijie.Wu
Email: 1694517106@qq.com
Date: 2020/5/18 21:27
"""

import json
from datetime import datetime
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from graphql import GraphQLError
from requests.exceptions import RequestException


class BaseGraphql(object):
    def __init__(self, api_host, sub_url, http_type, port):
        """
        base for qraphql api resource
        """
        if port and port.strip():
            self.transport_url = '{}://{}:{}/{}'.format(http_type, api_host, port, sub_url)
        else:
            self.transport_url = '{}://{}/{}'.format(http_type, api_host, sub_url)
        self.transport = RequestsHTTPTransport(self.transport_url)

        try:
            self.client = Client(transport=self.transport, fetch_schema_from_transport=True)
        except ConnectionError as connectionError:
            print("ConnectionError occurred")
            # TODO error handling
            self.errors = connectionError
        except RequestException as requestError:
            print("RequestException")
            self.errors = requestError
            raise requestError

    def query(self, query_string, param=None):
        start_time = datetime.now()
        param_string = None
        if param and type(param) is dict:
            param_string = str(json.dumps(param))
        elif param:
            param_string = str(param)
        else:
            pass

        query = gql(query_string)
        response = {}
        try:
            response = {'data': self.client.execute(query, param_string)}
        except GraphQLError as err:
            # TODO error handling
            print("GraphQLError occurred")
            print("Error message: " + err.message)
            response.update({'errors': err})
        start_time_ms = start_time.microsecond
        time = datetime.now().microsecond - start_time_ms
        response['time'] = time
        response['start_time'] = start_time.strftime("%H:%M:%S")
        return response
