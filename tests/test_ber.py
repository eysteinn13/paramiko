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
Some unit tests for the BER encoder / decoder.
"""

import pytest
from paramiko.ber import ( BER, BERException )

def test_encode_decode():
    ber = BER()
    ber.encode(1337)
    ber
    decoded = ber.decode()
    assert decoded == 1337

def test_encode_decode_sequence():
    sequence = [1, 2, 3, 4, 5]
    encoded = BER.encode_sequence(sequence)
    decoded = BER.decode_sequence(encoded)
    assert decoded == sequence
