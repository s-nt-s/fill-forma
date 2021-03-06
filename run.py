#!/usr/bin/env python3
import argparse
import sys
from datetime import datetime
import time

from os.path import isfile

from core.util import get_config
from core.web import FF

parser = argparse.ArgumentParser("Rellena y envia un formulario FORMA")
parser.add_argument('--hide', action="store_true", help='Oculta el explorador')
parser.add_argument('config', help='Fichero con los datos del formulario')
pargs = parser.parse_args()

if not isfile(pargs.config):
    sys.exit(pargs.config+" no existe")

c = get_config(pargs.config)

ini, fin = c.get('ini', 0), c.get('fin', 24)
while not(datetime.now().hour>=ini and datetime.now().hour<fin):
    time.sleep(1)
    print("Esperando a [%s-%s]" % (ini, fin), end="\r")
print("")

w = FF(visible=not pargs.hide, tries=4)
w.refresh_until(c.url, list(c.campos.keys())[0], seconds=2)

for k, v in c.campos.items():
    w.val(k, v)
w.click("form_submit")
w.wait(1)
w.click("form_submit")
w.click(".btnGuardarForm")

# w.close()
