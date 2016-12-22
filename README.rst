config-manager: Read and manage configuration data for your application
=======================================================================


Description
-----------

The **config-manager** package is a basic configuration reader and manager. It reads the configuration data from
an external YAML or JSON file and it injects this data into the application that is called from. It's currently
tested on Python 2.7.

- `Issue tracker`_
- `Changelog`_


Installation
------------

::

  pip install config-manager

or

download the `latest release`_ and run

::

  python setup.py install


Usage
-----

::

  #configs.yaml contains the configuration data

  from  config_manager import ConfigManager
  confman = ConfigManager(config_file_path='/path/to/configs.yaml', defaults={'maintenance':'False'}, required=['maintenance'])
  maintenance = confman['maintenance']


License
-------

This project is licensed under the MIT license.

.. _Changelog: https://github.com/afxentios/config-manager/blob/master/CHANGELOG.md
.. _Issue tracker: https://github.com/afxentios/config-manager/issues
.. _latest release: https://github.com/afxentios/config-manager/releases
