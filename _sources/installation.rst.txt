Installation
============


Virtualenv
**********

$ pip install
#############

The preferred way to install **metamock** is by using `pip <https://pypi.org>`_.

::

    $ pip install ec2-metamock



Get the Source Code
###################

Requests is actively developed on `GitHub <https://github.com/pygillier/ec2-metamock/>`_.

You can either clone the public repository:::

	$ git clone git://github.com/pygillier/ec2-metamock.git

Or, download the tarball:::

	$ curl -OL https://github.com/pygillier/ec2-metamock/tarball/master
	# optionally, zipball is also available (for Windows users).

Once you have a copy of the source, you can embed it in your own Python package, or install it into your site-packages easily:::

	$ cd ec2-metamock
	$ pip install .

Docker
******

A docker image will be available for use in a docker-compose setup.
