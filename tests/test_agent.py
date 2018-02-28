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
Unit tests for Agent
"""

import unittest

from paramiko.agent import (AgentClientProxy, 
                            AgentSSH)

"""
The outcome of connect should be None in AgentCLientProxy when nothing
happens except creation of the agent objects
"""
class AgentTest(unittest.TestCase):
    def test_connect(self):
        agentSSH = AgentSSH()
        agentCL = AgentClientProxy(agentSSH)
        self.assertEquals(None, agentCL.connect())
