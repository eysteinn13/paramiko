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
Unit tests for Channel
"""

import unittest

from paramiko.channel import Channel

class ChannelTest(unittest.TestCase):
    def test_get_id(self):
        """
        get_id should return the id of the channel, which is set by the constructor
        """
        channel = Channel(1)
        self.assertEquals(1, channel.get_id())

    def test_get_name(self):
        """
        get_name should return the name of the channel, which is set by the constructor and by set_name
        """
        channel = Channel(1)
        self.assertEquals("1", channel.get_name())
        channel.set_name("abc")
        self.assertEquals("abc", channel.get_name())
