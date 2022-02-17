import asyncio

from eliasc_pkg.a.default_extension import MyDefaultExtension
from symphony.bdk.core.config.loader import BdkConfigLoader
from symphony.bdk.core.symphony_bdk import SymphonyBdk


async def run():
    async with SymphonyBdk(BdkConfigLoader.load_from_symphony_dir("config.yaml")) as bdk:
        service = bdk.extensions().get_service(MyDefaultExtension)
        session_token_ = await service.get_session_token()
        print("Session token: " + session_token_)


asyncio.run(run())
