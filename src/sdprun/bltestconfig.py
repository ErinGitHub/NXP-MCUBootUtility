#! /usr/bin/env python

# Copyright (c) 2013 Freescale Semiconductor, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# o Redistributions of source code must retain the above copyright notice, this list
#   of conditions and the following disclaimer.
#
# o Redistributions in binary form must reproduce the above copyright notice, this
#   list of conditions and the following disclaimer in the documentation and/or
#   other materials provided with the distribution.
#
# o Neither the name of Freescale Semiconductor, Inc. nor the names of its
#   contributors may be used to endorse or promote products derived from this
#   software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys
import os
from collections import namedtuple

PeripheralParams = namedtuple('PeripheralParams', 'peripheral, speed, port')

kDefaultPeripheral = 'sdp_uart'

PeripheralPraramsDict = {
        'sdp_uart' : PeripheralParams('sdp_uart', '115200', 'COM40'),
        'sdp_usb'  : PeripheralParams('sdp_usb', '', '')
    }

peripheral = os.environ.get('KIBBLE_PERIPHERAL', PeripheralPraramsDict[kDefaultPeripheral].peripheral)
speed = os.environ.get('KIBBLE_SPEED', PeripheralPraramsDict[kDefaultPeripheral].speed)
port = os.environ.get('KIBBLE_PORT', PeripheralPraramsDict[kDefaultPeripheral].port)
usePing = 'false'

supportUsb = False

loadTarget = False
resetTarget = True

kibble_device = ''
debugger_if = 'SWD'

##
# @brief Define which target to test.
#
# The target is a tri-tuple of CPU, board, compiler, build
# target = 'L4KS', 'fpga', 'iar', 'Release'
# If manual testing, replace the second parameter of os.environ.get() with the target information
##
kibble_cpu = os.environ.get("KIBBLE_CPU", "K32H844P_ROM")           # e.g. os.environ.get("KIBBLE_CPU", "L4KS")
kibble_board = os.environ.get("KIBBLE_BOARD", "none")               # e.g. os.environ.get("KIBBLE_BOARD", "fpga")    
kibble_compiler = os.environ.get("KIBBLE_COMPILER", "none")         # e.g. os.environ.get("KIBBLE_COMPILER", "iar")  
kibble_build = os.environ.get("KIBBLE_BUILD", "none")               # e.g. os.environ.get("KIBBLE_BUILD", "Release")

target = kibble_cpu, kibble_board, kibble_compiler, kibble_build

# @brief Define the test vectors directory.
#
# @note The 'working' directory is one level above the test vectors directory.
vectorsDir = os.path.join(os.path.dirname(__file__), 'working', 'vectors')
