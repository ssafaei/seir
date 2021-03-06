SEIR
====

An `OpenCOR <https://opencor.ws/>`_-based Python script to model Covid-19 using the `SEIR model <https://cpb-ap-se2.wpmucdn.com/blogs.auckland.ac.nz/dist/d/75/files/2017/01/Covid19_SEIR_model.pdf>`_.

Install/upgrade
---------------

From OpenCOR's ``Python Console`` window::

 !pip install --upgrade git+https://github.com/ABI-Covid-19/seir.git

Uninstall
---------

From OpenCOR's ``Python Console`` window::

 !pip uninstall --yes seir

Run
---

From OpenCOR's ``Python Console`` window::

 import os, platform; exec(open(os.environ['PYTHONHOME'] + ('/Scripts' if (platform.system() == 'Windows') else '/bin') + '/seir.py').read())

which should result in something like:

.. image:: res/screenshot.png
