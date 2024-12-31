from prefect import flow

from module import Params


@flow
def entrypoint(params: Params | None = None):
    print(params)
