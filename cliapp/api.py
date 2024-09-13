from ninja import NinjaAPI
from ninja import Schema
import subprocess

api = NinjaAPI()

class CommandSchema(Schema):
    command: str

@api.post("/execute")
def execute_command(request, payload: CommandSchema):
    command = payload.command
    try:
        result = subprocess.check_output(['python3', '-c', command], stderr=subprocess.STDOUT, text=True)
        return {"result": result}
    except subprocess.CalledProcessError as e:
        return {"result": e.output}, 400
