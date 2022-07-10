from flask_restful import Resource
from flask import request
from typing import Dict


class Root(Resource):
    def get(self) -> Dict:
        return {
            "service": "Mobility on Service applicationi",
            "version": "development",
            "status": "online"
        }
