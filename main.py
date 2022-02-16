from eliasc_pkg import a
from eliasc_pkg import b
from symphony.bdk.core.symphony_bdk import SymphonyBdk
from symphony.bdk.extension import ExtensionService

if __name__ == '__main__':
    a.a_function()
    b.b_function()

    service = ExtensionService()
    service.register(ValueError())
    print(service._extensions)

    SymphonyBdk()
