import base64

command = b"aW1wb3J0IGxvZ2dpbmcKaW1wb3J0IG9zCmltcG9ydCBzdHJpbmcKCmxvZ2dlciA9IGxvZ2dpbmcu\nZ2V0TG9nZ2VyKF9fbmFtZV9fKQoKCmRlZiBmdW5jMSgpOgogICAgbG9nZ2VyLmluZm8oItCo0LDQ\nsyAxIikKICAgIGxvZ2dlci5kZWJ1Zygi0K3RgtC+INC/0YDQvtGB0YLQviDRgNCw0LfQvNC40L3Q\nutCwIikKCiAgICB3aGlsZSBUcnVlOgogICAgICAgIGRhdGEgPSBpbnB1dCgi0JLQsNGIINC+0YLQ\nstC10YI/ICIpCgogICAgICAgIHRyeToKICAgICAgICAgICAgbnVtYmVyID0gaW50KGRhdGEpCgog\nICAgICAgICAgICBpZiBudW1iZXIgIT0gOTk3MzoKICAgICAgICAgICAgICAgIGxvZ2dlci5kZWJ1\nZygi0J3QsNC8INC90YPQttC90L4g0LzQsNC60YHQuNC80LDQu9GM0L3QvtC1INC/0YDQvtGB0YLQ\nvtC1INGH0LjRgdC70L4g0LzQtdC90YzRiNC10LUg0YfQtdC8IDEwMDAwIikKICAgICAgICAgICAg\nICAgIHByaW50KCLQndC1INC/0YDQsNCy0LjQu9GM0L3QviEiKQogICAgICAgICAgICBicmVhawog\nICAgICAgIGV4Y2VwdCBFeGNlcHRpb246CiAgICAgICAgICAgIHBhc3MKCiAgICBwcmludCgi0KjQ\nsNCzIDEg0L/RgNC+0LnQtNC10L0iKQoKCmRlZiBmdW5jMigpOgogICAgbG9nZ2VyLmluZm8oItCo\n0LDQsyAyIikKCiAgICBsb2dnZXIuZGVidWcoItCX0LDQtNCw0LnRgtC1INC/0LXRgNC10LzQtdC9\n0L3QvtC5INC+0LrRgNGD0LbQtdC90LjRjyBTS0lMTEJPWCDQt9C90LDRh9C10L3QuNC1IGF3ZXNv\nbWUiKQogICAgbG9nZ2VyLmRlYnVnKCLQktGLINC80L7QttC10YLQtSDQt9Cw0LTQsNGC0Ywg0LfQ\nvdCw0YfQtdC90LjQtSDQv9C10YDQtdC80LXQvdC90L7QuSDQvtC60YDRg9C20LXQvdC40Y8g0LLQ\nvtGCINGC0LDQujoiKQogICAgbG9nZ2VyLmRlYnVnKCIkIGV4cG9ydCBWQVJOQU1FPXZhbHVlIikK\nCiAgICB3aGlsZSBUcnVlOgogICAgICAgIGlucHV0KCLQlNC70Y8g0L/RgNC+0LTQvtC70LbQtdC9\n0LjRjyDQvdCw0LbQvNC40YLQtSBFTlRFUi4uLiIpCgogICAgICAgIHRyeToKICAgICAgICAgICAg\naWYgb3MuZW52aXJvblsiU0tJTExCT1giXS5sb3dlcigpID09ICJhd2Vzb21lIjoKICAgICAgICAg\nICAgICAgIGJyZWFrCiAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICAgICAgcGFzcwoK\nICAgICAgICBwcmludCgi0JLRiyDQvdC1INCz0L7RgtC+0LLRiy4uLiIpCgogICAgcHJpbnQoItCo\n0LDQsyAyINC/0YDQvtC50LTQtdC9IikKCgpkZWYgZnVuYzMoKToKICAgIGxvZ2dlci5pbmZvKCLQ\nqNCw0LMgMyIpCgogICAgbG9nZ2VyLmRlYnVnKCLQodC+0LfQtNCw0LnRgtC1INGE0LDQudC7IGh3\nNy50eHQg0YEg0LDQvdCz0LvQuNC50YHQutC40Lwg0L/QsNC70LjQvdC00YDQvtC80L7QvCDQstC9\n0YPRgtGA0LgiKQogICAgd2hpbGUgVHJ1ZToKICAgICAgICB0cnk6CiAgICAgICAgICAgIGlucHV0\nKCLQlNC70Y8g0L/RgNC+0LTQvtC70LbQtdC90LjRjyDQvdCw0LbQvNC40YLQtSBFTlRFUi4uLiIp\nCgogICAgICAgICAgICB3aXRoIG9wZW4oImh3Ny50eHQiLCAiciIpIGFzIGZpOgogICAgICAgICAg\nICAgICAgZGF0YSA9IGZpLnJlYWQoKS5sb3dlcigpCgogICAgICAgICAgICAgICAgZGF0YV9zdHIg\nPSBbaXQgZm9yIGl0IGluIGRhdGEgaWYgaXQgaW4gc3RyaW5nLmFzY2lpX2xvd2VyY2FzZV0KCiAg\nICAgICAgICAgICAgICBpZiBkYXRhX3N0ciA9PSBkYXRhX3N0cls6Oi0xXToKICAgICAgICAgICAg\nICAgICAgICBicmVhawoKICAgICAgICAgICAgICAgIGxvZ2dlci5kZWJ1ZyhmIntkYXRhX3N0cn0g\nIT0ge2RhdGFfc3RyWzo6LTFdfSIpCiAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICAg\nICAgcGFzcwoKICAgICAgICBwcmludCgi0J3QtSDRgNCw0LHQvtGC0LDQtdGCLi4uIikKCiAgICBw\ncmludCgi0KjQsNCzIDMg0L/RgNC+0LnQtNC10L0iKQoKCmRlZiB3aGF0X3dlbnRfd3JvbmcoKToK\nICAgIGZ1bmMxKCkKICAgIGZ1bmMyKCkKICAgIGZ1bmMzKCkKCgp3aGF0X3dlbnRfd3JvbmcoKQo="

if __name__ == "__main__":
    exec(base64.decodebytes(command).decode("utf8"))
#задание посмотрел, не понял, не написано ничего.