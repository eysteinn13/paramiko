# Copyright (C) 2003-2007  John Rochester <john@jrochester.org>
#
# This file is part of paramiko.
#
# Paramiko is free software; you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation; either version 2.1 of the License, or (at your option)
# any later version.
#
# Paramiko is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Paramiko; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA.

"""
Unit tests for Proxy
"""

import unittest

from paramiko.proxy import ProxyCommand

class ProxyCommandTest(unittest.TestCase):
    def test_settimout(self):
        """
        The timeout property should be set to the argument of settimeout()
        """
        proxyCommand = ProxyCommand("ls")
        proxyCommand.settimeout(10)
        self.assertEquals(10, proxyCommand.timeout)
