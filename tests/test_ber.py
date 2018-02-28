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

import unittest
from paramiko.ber import ( BER, BERException )


class BerTester(unittest.TestCase):

    def test_encode_with_illegal_types(self):
        """
        Encode should raise exception when used with float
        """
        ber = BER()
        self.assertRaises(BERException, ber.encode, 0.1337)

    def test_encode_works_on_lists_directly(self):
        """
        Encode should raise exception when used with string
        """
        ber = BER()
        original_list = [1, 2, 3, 4, 5]
        ber.encode(original_list)
        self.assertEqual(ber.decode(), original_list)


    def test_encode_decode(self):
        """
        When decoding an encoded integer, the original integer should be returned
        """
        ber = BER()
        ber.encode(1337)
        decoded = ber.decode()
        self.assertEqual(decoded, 1337)


    def test_encode_decode_sequence(self):
        """
        When decoding an encoded list, the original list should be returned
        """
        sequence = [1, 2, 3, 4, 5]
        encoded = BER.encode_sequence(sequence)
        decoded = BER.decode_sequence(encoded)
        self.assertEqual(decoded, sequence)
